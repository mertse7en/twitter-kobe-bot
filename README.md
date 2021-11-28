# twitter-kobe-bot

Kobe-twitter-bot is simple twitter-bot to post reminder tweets daily.
Check : https://twitter.com/KobeReminder

## Stepts to follow

- Create config.env file under config folder
- Enter the credentials as shown in config.env.example
- Set message to be sent. Check tweet_bot.py/ set_tweet method 


## How to run
```
docker rm -f twitter_bot

docker build --tag tweet_bot:latest .

docker create --name twitter_bot tweet_bot:latest .

docker start twitter_bot

docker logs -f twitter_bot
```

## Run daily @cronjob
0 9 * * *  docker start twitter_bot 
