# This code is based on the following example:
# https://discordpy.readthedocs.io/en/stable/quickstart.html#a-minimal-bot

import discord
from discord.ext import commands
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id = os.getenv('SPOTIPY_CLIENT_ID')
client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')
bot_token = os.getenv('BOT_TOKEN')


intents = discord.Intents.default()  # Create an instance of Intents
intents.typing = False  # Disable typing events, if desired
intents.presences = False  # Disable presence events, if desired

bot = commands.Bot(command_prefix='/', intents=intents)
client = discord.Client(intents=intents)

logic_uri = 'https://open.spotify.com/artist/4xRYI6VqpkE3UwrDrAZL8L?si=sqOCFbjFRx6jpHaWogSVrg'

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

results = sp.artist_albums(logic_uri, album_type='album')
albums = results['items']
while results['next']:
    results = sp.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])

id_list = []

tracks = sp.album_tracks('https://open.spotify.com/album/7viNUmZZ8ztn2UB4XB3jIL?si=CoKXRho2SOuD5FByREFw9A')

# if 'items' in tracks:
#     for track in tracks['items']:
#         id_list.append(tracks['id'])
# else:
#     print("No tracks found for the given album ID.")
# print(tracks['uri'])

# @bot.event
# async def on_ready():
#     print(f'Bot connected as {bot.user.name}')

sp.start_playback(device_id=None, uris= ['spotify:artist:6l3HvQ5sa6mXTsMTB19rO5'], offset=None)

# client.run(os.getenv(bot_token))