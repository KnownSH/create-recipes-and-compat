import os
import json

directory = "data/compat/recipes/blockus/cutting/"

for filename in os.listdir(directory):
    filedir = os.path.join(directory, filename)
    item = ""

    if os.path.isfile(filedir):
        with open(filedir, 'r') as f:
            data = json.load(f)
            item = data['results'][0]['item']
            r, item = item.rsplit(':', 1)
        os.rename(filedir, '{}{}.json'.format(directory, item))