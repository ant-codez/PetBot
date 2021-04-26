# Discord Pet Bot :dog::cat::unicorn:
Collect, hatch and raise pets with this discord bot!

## Adding To Your Server :factory:
To add the bot to your server use this link:
* [Discord Math Bot](https://discord.com/api/oauth2/authorize?client_id=832152940420661250&permissions=8&scope=bot)

## Usage :newspaper:
To use this bot type in a channel that give the bot permission to read and write.

Commands:

* `$hatch` - Give your pet a name and hatch your egg!
* `$stats <petname>` - Check out the stats of your Favorite Pet!

## Program Flow :alien:
This program starts at `bot.py` and uses `abstract_pet_factory.py` to generate pets and `database.py` to inteface with out PostgreSQL database

## Running This Program :running:
If you are trying to run this program on your machine then you need
a bot `token` from discord. Once you get one, go to the bottom of `bot.py` and paste your token there in the `token` variable

## Dependencies :milky_way:
python 3.6 or above


`https://www.python.org/downloads/`

discord

`python3 -m pip install discord`


psycopg2

`python3 -m pip install psycopg2`


PyYAML

`python3 -m pip install pyyaml`

emoji

`python3 -m pip install emoji`

flask

`python3 -m pip install flask`

flask-sqlalchemy

`python3 -m pip install flask-sqlalchemy`

flask-migrate

`python3 -m pip install flask-migrate`

flask-wtf

`python3 -m pip install flask-wtf`
