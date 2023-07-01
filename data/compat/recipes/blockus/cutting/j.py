inputs = ["tag", 
         "c:compat/blockus/skulk_bricks", 
         "blockus", 
         "", 
         "1"]

while True:
    block = input('block: ')

    if block == "":
        break

    inputs[3] = block

    f = open("data/compat/recipes/blockus/cutting/" + inputs[3] + ".json", "x")
    f.write("""{{
    "type": "create:cutting",
    "ingredients": [
        {{
            "{0}": "{1}"
        }}
    ],
    "results": [
        {{
            "item": "{2}:{3}",
            "count": {4}
        }}
    ],
    "processingTime": 50,
    "fabric:load_conditions": [
        {{
            "condition": "fabric:all_mods_loaded",
            "values": [
                "blockus"
            ]
        }}
    ]
    }}""".format(*inputs))
    f.close()