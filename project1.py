name = input("Hey type your name:")
print(f'Hello {name} welcome to the game!')

wanna_play = input('Do you wanna Play? ').lower()

if wanna_play == 'yes' or wanna_play =='y': 
    print('So, lets play!')

    direction = input('Do you wanna left or right? (left/right) ').lower()
    if direction == 'left': 
        print('Wrong choice, you find a bear and die! ')
    elif direction == 'right':
        choice1 = input('Great, we find a bridge! Do you wanna cross or swin? ').lower()
        if choice1 == 'cross':
            print('Good Choice the water its full of crocodiles') 
            choice2 = input('You find two doors, which one do you wanna open? (1/2) ').lower()
            if choice2 == '1': 
                print('Good Job you find the treasure!')
            else: 
                print('The room it full of lions! YOU DIED')
        else: 
            print('You die! Eaten by a crocodile!')         
    else: 
        print('Sorry, this is not a valid value! YOU DIE! ')
else: 
    print('Okay, goodbye!')