import random, requests, json, re
import asyncio

import discord, praw
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
            hot_link_not_good = True

            while hot_link_not_good:
                try:
                    hot_link = random.choice(hot_links)
                    json_link = "https://www.reddit.com/" + re.search(r"^https:\/\/redd.it\/(.*)$",hot_link).group(1) + ".json"
                    res = requests.get(json_link)
                    res_text = res.text
                    res_data = json.loads(res_text)
                    img_link = res_data[0]['data']['children'][0]['data']['url']
                    img_title = res_data[0]['data']['children'][0]['data']['title']
                    hot_link_not_good = False
                except Exception:
                    hot_link_not_good = True


            em = discord.Embed(title=img_title)
            em.set_author(name="EXECUTE ORDER PREQUEL MEME")
            em.set_image(url=img_link)
            em.url = hot_link

            await client.send_message(message.channel, embed=em)

            

    




    client.run(secrets['bot_token'])