import random

words = ['About','Above','Abuse','Actor','Acute','Admit','Adopt','Adult','After','Again','Agent','Agree','Ahead','Alarm','Album','Boost','Booth','Bound','Brain','Brand','Bread','Break','Breed','Brief','Bring','Broad','Broke','Brown','Build','Built','Debut','Delay','Depth','Doing','Doubt','Dozen','Draft','Drama','Drawn','Dream','Dress','Drill','Drink','Drive','Drove','Dying','Eager','Early','Earth','Eight','Elite','Empty','Enemy','Enjoy','Enter','Judge','Known','Label','Large','Laser','Later','Laugh','Layer','Learn','Lease','Least','Leave','Legal','Level','Light','Limit','Peace','Panel','Phase','Phone','Photo','Piece','Pilot','Pitch','Place','Plain','Plane','Plant','Plate','Point','Pound','Sheet','Shelf','Shell','Shift','Shirt','Shock','Shoot','Short','Shown','Sight','Since','Sixty','Sized','Skill','Sleep','Slide','Small','Smart','Smile','Smith','Smoke','Solid','Solve','Sorry','Sound','South','Space','Upset','Urban','Usage','Usual','Valid','Value','Video','Virus','Visit']

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

stages = [
    '____\n|  |\n|\n|\n|\n|____\n', 
    '____\n|  |\n|  o\n|\n|\n|____\n', 
    '____\n|  |\n|  o\n|  |\n|\n|____\n', 
    '____\n|  |\n|  o\n| /| \n|\n|____\n', 
    '____\n|  |\n|  o\n| /|\ \n|\n|____\n', 
    '____\n|  |\n|  o\n| /|\ \n| / \n|____\n', 
    '____\n|  |\n|  o\n| /|\ \n| / \ \n|____\n'
]

while(1):
    word_to_guess = random.choice(words).upper()
    word_progress = '_' * len(word_to_guess)
    words_left = alphabet
    stage = 0

    while('_' in word_progress):
        if stage > len(stages)-2:
            print(stages[len(stages)-1])
            print('You lost!')
            print('The word was: ', word_to_guess)
            break
        print(stages[stage])
        print(word_progress)
        print(words_left)

        current_letter = input('\nGuess a letter: ').upper()
        print()
        words_left = words_left.replace(current_letter, '_')

        if current_letter in word_to_guess:
            for i in range(len(word_to_guess)):
                if current_letter == word_to_guess[i]:
                    word_progress = word_progress[:i] + current_letter + word_progress[i+1:]
        else:
            stage += 1

        print('\n========================\n')
        
    else:
        print(stages[stage])
        print(word_progress)
        print(words_left)
        print()
        print('You won!')
    
    input('\nPress enter to play again...')
    print('\n========================\n')