from datetime import datetime
from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

billboard_url = 'https://www.billboard.com/charts/hot-100/'

def get_input_date():
    try:
        day = int(input("Enter day (1-31): "))
        month = int(input("Enter month (1-12): "))
        year = int(input("Enter year (e.g., 2023): "))
        return datetime(year, month, day)
    except ValueError:
        print("Invalid date. Please try again.")
        return get_input_date()

def fetch_billboard_data(input_date):
    formatted_date = input_date.strftime('%Y-%m-%d')
    url = f"{billboard_url}{formatted_date}/"
    
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch Billboard data. Status code: {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    song_entries = soup.select("li.o-chart-results-list__item h3")

    songs = [entry.get_text(strip=True) for entry in song_entries if entry.get_text(strip=True) != '']
    
    return songs

# Run
input_date = get_input_date()
songs = fetch_billboard_data(input_date)

# Show Top 10
print("\nTop Songs:")
for idx, song in enumerate(songs[:100], 1):
    print(f"{idx}. {song}")

# Spotify Authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id="YOUR_UNIQUE_CLIENT_ID",
        client_secret="YOUR_UNIQUE_CLIENT_SECRET",
        show_dialog=True,
        cache_path="token.txt",
        username="YOUR_SPOTIFY_DISPLAY_NAME", 
    )
)
user_id = sp.current_user()["id"]