import json
from sprite_groups import score_sprites

def update_highscores():
    """Uses JSON file to generate a list of highscores."""
    # Access JSON
    with open('highscores.json', 'r') as read:
        data = json.load(read)

    # Update Highscores Table
    n = 1
    for sprite in score_sprites:
        try:
            new_text = (n, '.)', ' ', data[str(n)][0], '  ---', ' ', 'Round: ', data[str(n)][1])
            string = ''.join(map(str, new_text))    # https://www.geeksforgeeks.org/python-program-to-convert-a-tuple-to-a-string/
            sprite.change_text(string)
        except:
            pass
        n += 1