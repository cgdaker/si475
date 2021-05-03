import json

with open('start.json') as f1:
    start = json.load(f1)

#print(data)
#print(data['RED'])

with open('simple.json') as f2:
    goal = json.load(f2)

print(start)
print(goal)
