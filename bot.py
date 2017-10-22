import discord
import asyncio

import praw
import random
import yaml

with open('.secrets') as f:
    secret_file = f.read()
    f.close()

    secrets = yaml.load(secret_file)

    client = discord.Client()
    reddit = praw.Reddit(client_id=secrets['client_id'], client_secret=secrets['client_secret'], user_agent=secrets['user_agent'])

    @client.event
    async def on_ready():
            print('Logged in as')
            print(client.user.name)
            print(client.user.id)
            print('------------')
        
    @client.event
    async def on_message(message):
        message_string = message.content

        if 'prequel' in message_string and 'meme' in message_string:
            hot_memes = reddit.subreddit('prequelmemes').hot()
            hot_links = [meme.shortlink for meme in hot_memes]
            await client.send_message(message.channel, random.choice(hot_links))

    client.run(secrets['bot_token'])