#  This is Hangman, you know what it is...

import random
import math

drawing = ['''
    _ _ _
    |   |
    |   |
        |
        |
        |
   - - - - - -

''',
'''
    _ _ _
    |   |
    |   |
    0   |
        |
        |
   - - - - - -
''',
'''

    _ _ _
    |   |
    |   |
    0   |
    |   |
        |
   - - - - - -
   
''',
'''

    _ _ _
    |   |
    |   |
    0   |
    | \ |
        |
   - - - - - -
   
''',
'''
    _ _ _
    |   |
    |   |
    0   |
  / | \ |
        |
   - - - - - -

''',
'''
    _ _ _
    |   |
    |   |
    0   |
  / | \ |
     \  |
   - - - - - -
''',
'''
    _ _ _
    |   |
    |   |
    0   |
  / | \ |
   / \  |
   - - - - - -
''']
done = False
used_list = []

correct = 0


words = ["gamers", "Harp", "didgeridoo", "africa", "Hamburger", "Sixteen", "Baseball", "Chicago", "Tarkov", "Zombies"]
current_word = words.pop(random.randrange(len(words)))


missed = 0



while not done:


    print(drawing[missed])
    print("Used letters:", used_list)

    for letter in current_word:
        if letter in used_list:
            print(letter, end=" ")
        else:
            print("_", end=" ")

    x = input("Pick a letter: ")
    if len(x) >= 2:
        print("It has to be a letter!")
    elif x.lower() in used_list:
        print("You already guessed this!")
    else:
        used_list.append(x.lower())
        if x.lower() in current_word:
            print("\nCorrect!")
            correct += current_word.count(x.lower())
        else:
            if missed == 5:
                print(drawing[6])
                print('''You lose!
                The word was: ''', current_word)
                done = True
            else:
                missed += 1
                print("\nIncorrect!")




    if len(current_word) == correct:
        print('''You solved the Hangman!
        The word was: ''', current_word)
        done = True








