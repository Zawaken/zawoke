import json


with open('secrets.json') as json_data:
    d = json.load(json_data)

prefixes = ['>>', 'zawoke ', 'z ']
game = '>>'
description = 'Zawoke rewritten'

owner_id: int = 85467784179351552
