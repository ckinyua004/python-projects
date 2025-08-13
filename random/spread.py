# epidemic_sim.py
import pygame
import random
import math
from collections import deque

# -----------------------
# Simulation parameters
# -----------------------
WIDTH, HEIGHT = 1000, 700
POPULATION = 2000            # number of agents
INITIAL_INFECTED = 3       # patient zeros
SPEED = 1.4                # movement speed
INFECTION_RADIUS = 12      # pixels
INFECTION_PROB = 0.25      # probability on contact per frame (0-1)
RECOVERY_TIME = 12 * 60    # frames until recovery (here ~12 seconds if 60 FPS)
FPS = 60

# Visuals
SUS_COLOR = (100, 200, 255)    # susceptible - light cyan
INF_COLOR = (220, 50, 50)      # infected - red
REC_COLOR = (100, 220, 120)    # recovered - green
BG_COLOR = (30, 30, 35)
TEXT_COLOR = (230, 230, 230)
GRAPH_BG = (20, 20, 25)
GRAPH_LINE = (200, 200, 200)

# -----------------------
# Agent class
# -----------------------
class Agent:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        angle = random.random() * 2 * math.pi
        self.vx = math.cos(angle) * SPEED
        self.vy = math.sin(angle) * SPEED
        self.status = "S"  # 'S' susceptible, 'I' infected, 'R' recovered
        self.infected_timer = 0

    def move(self):
        self.x += self.vx
        self.y += self.vy

        # bounce off walls
        if self.x <= 2 or self.x >= WIDTH - 2:
            self.vx *= -1
            self.x = max(2, min(self.x, WIDTH - 2))
        if self.y <= 2 or self.y >= HEIGHT - 160:  # leave space bottom for HUD/graph
            self.vy *= -1
            self.y = max(2, min(self.y, HEIGHT - 160))

    def try_infect(self, other):
        if self.status != 'I' or other.status != 'S':
            return False
        dx = self.x - other.x
        dy = self.y - other.y
        if dx*dx + dy*dy <= INFECTION_RADIUS**2:
            if random.random() < INFECTION_PROB:
                other.status = 'I'
                other.infected_timer = 0
                return True
        return False

    def step_recovery(self):
        if self.status == 'I':
            self.infected_timer += 1
            if self.infected_timer >= RECOVERY_TIME:
                self.status = 'R'

# -----------------------
# Simulation setup
# -----------------------
def create_population(n, initial_infected):
    pop = []
    for _ in range(n):
        x = random.uniform(10, WIDTH - 10)
        y = random.uniform(10, HEIGHT - 170)
        pop.append(Agent(x, y))
    # Infect some
    for i in random.sample(range(n), min(initial_infected, n)):
        pop[i].status = 'I'
        pop[i].infected_timer = 0
    return pop

# -----------------------
# Drawing helpers
# -----------------------
def draw_agent(screen, agent):
    color = SUS_COLOR if agent.status == 'S' else (INF_COLOR if agent.status == 'I' else REC_COLOR)
    pygame.draw.circle(screen, color, (int(agent.x), int(agent.y)), 4)

def draw_hud(screen, font, counts, frame_count, paused):
    sus, inf, rec = counts
    hud_y = HEIGHT - 150
    # background rect
    pygame.draw.rect(screen, (15, 15, 18), (0, hud_y, WIDTH, 150))
    # stats text
    txt = [
        f"Frame: {frame_count}",
        f"Population: {POPULATION}",
        f"Susceptible: {sus}",
        f"Infected: {inf}",
        f"Recovered: {rec}",
        f"Infection radius: {INFECTION_RADIUS}px  Prob: {INFECTION_PROB:.2f}",
        f"Recovery time: {RECOVERY_TIME/FPS:.1f}s",
        "Space: Pause/Resume   R: Reset   Up/Down: Infection Prob   +/-: Radius"
    ]
    for i, line in enumerate(txt):
        surf = font.render(line, True, TEXT_COLOR)
        screen.blit(surf, (10 + (i//4)*380, hud_y + 8 + (i % 4) * 22))
    if paused:
        p = font.render("PAUSED", True, (255, 200, 70))
        screen.blit(p, (WIDTH - 120, hud_y + 8))

def draw_graph(screen, history):
    # draw simple SIR graph inside HUD area
    graph_rect = pygame.Rect(WIDTH - 420, HEIGHT - 140, 400, 120)
    pygame.draw.rect(screen, GRAPH_BG, graph_rect)
    if len(history) < 2:
        return
    max_len = len(history)
    w = graph_rect.width
    h = graph_rect.height
    step = w / max_len
    # find max population for scaling (should be POPULATION)
    scale = h / POPULATION
    # draw lines (S=cyan, I=red, R=green)
    points_S = []
    points_I = []
    points_R = []
    for i, (s, inf, r) in enumerate(history):
        x = graph_rect.x + i * step
        points_S.append((int(x), int(graph_rect.y + h - s*scale)))
        points_I.append((int(x), int(graph_rect.y + h - inf*scale)))
        points_R.append((int(x), int(graph_rect.y + h - r*scale)))
    if len(points_S) > 1:
        pygame.draw.lines(screen, SUS_COLOR, False, points_S, 2)
        pygame.draw.lines(screen, INF_COLOR, False, points_I, 2)
        pygame.draw.lines(screen, REC_COLOR, False, points_R, 2)

# -----------------------
# Main loop
# -----------------------
def run():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Epidemic Spread Simulation — Agent-based")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("consolas", 18)

    population = create_population(POPULATION, INITIAL_INFECTED)
    running = True
    paused = False
    frame_count = 0

    # history of (S, I, R) for graph (store up to WIDTH points)
    history = deque(maxlen=400)

    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = not paused
                elif event.key == pygame.K_r:
                    population = create_population(POPULATION, INITIAL_INFECTED)
                    history.clear()
                    frame_count = 0
                elif event.key == pygame.K_UP:
                    global INFECTION_PROB
                    INFECTION_PROB = min(1.0, INFECTION_PROB + 0.05)
                elif event.key == pygame.K_DOWN:
                    INFECTION_PROB = max(0.0, INFECTION_PROB - 0.05)
                elif event.key == pygame.K_PLUS or event.key == pygame.K_EQUALS:
                    global INFECTION_RADIUS
                    INFECTION_RADIUS += 1
                elif event.key == pygame.K_MINUS:
                    INFECTION_RADIUS = max(1, INFECTION_RADIUS - 1)

        if not paused:
            # move agents
            for a in population:
                a.move()

            # infection checks (naive O(n^2) — fine for a few hundred agents)
            for i, a in enumerate(population):
                if a.status == 'I':
                    for j in range(len(population)):
                        if i == j:
                            continue
                        b = population[j]
                        a.try_infect(b)

            # recovery step
            for a in population:
                a.step_recovery()

            frame_count += 1

        # draw
        screen.fill(BG_COLOR)
        # agents
        for a in population:
            draw_agent(screen, a)

        # counts
        s_count = sum(1 for a in population if a.status == 'S')
        i_count = sum(1 for a in population if a.status == 'I')
        r_count = sum(1 for a in population if a.status == 'R')

        history.append((s_count, i_count, r_count))

        # HUD + graph
        draw_hud(screen, font, (s_count, i_count, r_count), frame_count, paused)
        draw_graph(screen, list(history))

        # if epidemic died out, show message
        if i_count == 0 and frame_count > 10:
            msg = font.render("No active infections. Press R to reset.", True, (240, 240, 240))
            screen.blit(msg, (WIDTH//2 - 160, HEIGHT - 60))

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    run()
