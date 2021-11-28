# twitter-kobe-bot

```
docker build --tag tweet_bot:latest .

docker rm -f twitter_bot

docker create --name twitter_bot tweet_bot:latest .

docker start twitter_bot

docker logs -f twitter_bot
```
