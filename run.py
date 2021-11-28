import os, json
from src.tweet_bot import Scrapper
from dotenv import load_dotenv

def load_environment() -> None:
    if os.path.exists("config/config.env"):
        load_dotenv(dotenv_path="config/config.env")
    else:
        raise FileNotFoundError("\"config/config.env\" not found. Please set your credentials as shown in config.env.example")


def main():
    scrapper = Scrapper()
    scrapper.tweet_bot()



if __name__ == "__main__":
    load_environment()
    main()