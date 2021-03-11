import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR)
latest = "21/03/11"

with open(os.path.join(test, 'news.json'), 'w+',encoding='utf-8') as json_file:
    json.dump(latest, json_file, ensure_ascii = False)
