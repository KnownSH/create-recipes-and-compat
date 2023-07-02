import os
import json

directory = "data/compat/recipes/blockus/cutting/"

for filename in os.listdir(directory):
    filedir = os.path.join(directory, filename)
    item = ""

    if os.path.isfile(filedir):
        with open(filedir, 'r+') as f:
            data = json.load(f)
            item = data['results'][0]['item']
            if item.endswith("slab"):
                data['results'][0]["count"] = 2
            else:
                data['results'][0]["count"] = 1
            r, item = item.rsplit(':', 1)
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
        os.rename(filedir, '{}{}.json'.format(directory, item))