import random

def is_valid_play(play):
    return play in ['rock', 'paper', 'scissors']

def random_play():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_game_result(human, computer):
# Returns str with 'tie', 'computer', 'human'
    
    if human == computer:
        return 'tie'

    elif human+computer in 'rockpaperscissorsrock':
        return 'computer'

    else:
        return 'human'


def main(input=input): # fce main bere argument input a výchozí hodnota je, když není jiný tak ten input níže
    human = ''

    while not is_valid_play(human):
       human = input('rock, paper or scissors?')     

    computer = random_play()

    print(computer)

    result = determine_game_result(human, computer)
    if result == 'tie':
        print('It is a tie')
    else:
        print(result, 'wins')

if __name__ == '__main__': #magická proměnná, která obsahuje název modulu, ve kterém jsme; zajistí, aby se ta hlavní fce volala pouze, když to člověk pustí; a ne při importu, který máme v testovém souboru
    main()



if False: 
    human = input('rock, paper or scissors? ')

    while human not in ['rock', 'paper', 'scissors']:
        human = input('rock, paper or scissors? ')

    computer = random.choice(['rock', 'paper', 'scissors'])

    print(computer)

    if human == computer:
        print('Its a tie!')

    elif human+computer in 'rockpaperscissorsrock':
        print('computer wins')

    else:
        print('human wins') 
