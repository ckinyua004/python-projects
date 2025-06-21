import vpython
from vpython import sphere, vector, color, rate

ball = sphere(pos=vector(0,10,0), radius=1, color=color.red, make_trail=True)
g = vector(0,-9.8,0)
v = vector(2,0,0)
dt = 0.01

while ball.pos.y >= 0:
    rate(100)
    v += g * dt
    ball.pos += v * dt
    if ball.pos.y < 0:
        ball.pos.y = 0
        v.y *= -0.8  # Bounce with some energy loss
        v.x *= 0.8   # Dampen horizontal speed on bounce
        ball.make_trail = True  # Enable trail after first bounce