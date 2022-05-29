import os
import json
import time

def calculateHighScores():

    # read input and delete file
    # sample input = {"name": "AAA", "round": "5"}
    with open("gameover.json", "r") as input:
        recieved = json.load(input)
    
    os.remove("gameover.json")

    with open('highscores.json','r') as prevHigh:
        try:
            prevScores = json.load(prevHigh)
        except Exception as e:
            print("Creating highscores.json file for the first time")
            prevScores = {}

    scores = {}
    for j in prevScores.values():
        scores[j[0]] = j[1]
    scores[recieved['name']] = recieved['round']
    items = sorted(scores.items(), key=lambda item: int(item[1]))
    items = items[::-1]
    outputDict = {}
    for i in range(len(items)):
        outputDict[i+1] = items[i]
    
    output = json.dumps(outputDict, indent = 4)

    with open('highscores.json', 'w') as curHigh:
        curHigh.write(output)

def main():
    while True:
        # List all files in the current directory that the game is running from
        path = "."
        dir_list = os.listdir(path)

        # create highscores.json in current dir if not present
        if 'highscores.json' not in dir_list:
            with open('highscores.json', 'w'): pass

        if 'gameover.json' in dir_list:
            calculateHighScores()
        time.sleep(5)

if __name__ == '__main__':
    main()