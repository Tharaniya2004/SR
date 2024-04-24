import json

with open('ex5.json', 'r') as f:
    ex5 = json.load(f)


for donut in ex5:
    if donut['name'] == 'Old Fashioned':
        donut['batters']['batter'].append({'type': 'Tea', 'id': '5000'})


with open('ex5.json', 'w') as f:
    json.dump(ex5, f, indent=4)

print("Updated ex5.json file successfully!")