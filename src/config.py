import json
import os


with open('secrets.json') as json_data:
    d = json.load(json_data)

prefixes = ['>>', 'zawoke ', 'z ']
game: str = '>>'
docker_game: str = 'in her container'
description: str = 'Zawoke rewritten'
docker_status: bool = os.getenv('DOCKER_MODE', False)

owner_id: int = 85467784179351552
