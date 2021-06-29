# zawoke
Trying my hand at doing a complete rewrite of my discord bot.
<br>[Invite link](https://discordapp.com/oauth2/authorize?client_id=319005959022313483&scope=bot&permissions=2146958591)
<br>`Zawaken#0001`

## Getting started

### Using an existing instance
 - Click the invite link above.
 - type `z help` for an introduction to zawokes commands and prefixes.

### Running Zawoke yourself
Zawoke can be hosted in two different ways.
Do remember to copy src/example_secrets.json to src/secrets.json

#### On bare metal
You can git clone the repo and run it with `python3 alpha.py` in the `/src` directory.

#### Docker

I prefer using docker-compose to achieve this.

```
docker-compose build --no-cache
docker-compose up -d
```
