import json

with open("ExampleJSON.json") as file:
    datiJson = json.load(file)
    print(datiJson)
    print()
    print(datiJson["mappe"])


dizinario = {"Paolo": 10, "Giovanni": 20, "Maria": 30}
with open("ScritturaJSON.json", "w") as file:
    json.dump(dizinario, file, indent=4)




