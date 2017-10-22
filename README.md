# Subreddit Discord Bot

In order to use this bot, you need a yaml file named ".secrets" in your main directory with the following entries:

```

user_agent : <your_reddit_API_username>
client_id : <your_discord_client_id>
client_secret : <your_discord_client_secret_key>
bot_token : <your_bot_token>
post_title : <the_title_of_all_your_posts>
subreddit : <the_name_of_your_subreddit>
keywords : 
    - <required_keyword_1>
    - <required_keyword_2>
    - <required_keyword_3>

```

It basically works by scanning everything everyone types, and if they happen to type all the required keywords in a single message, the bot goes to your desired subreddit and picks randomly from the current hot posts. 

Example post:

![EXECUTE ORDER SEXY SEX](https://i.imgur.com/FXJnPJA.png)

Enjoy!
