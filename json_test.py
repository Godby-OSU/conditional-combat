import json

with open('highscores.json', 'r') as read:
    data = json.load(read)

print(data)

text = (1, '.)', 'Bob', 0)
string = ''.join(map(str, text)) # https://www.geeksforgeeks.org/python-program-to-convert-a-tuple-to-a-string/
print(string)

for n in range(5):
    try:
        print(n+1)
        print(data[str(n+1)][0], data[str(n+1)][1]) #
    except:
        pass
