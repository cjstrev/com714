# question 1 ------------------------------------------
print('Who broke my heart?')

user_input = input('')

print('My first love, ' + user_input + ', broke my heart for the first time.')
print('And I was like baby, baby, baby oh.')

# question 2 ------------------------------------------

print('\nWho sees me rolling? (cops, wardens, other)')

user_input = input('')

if user_input == 'cops':
    print('They see me rolling. I am ashamed of myself.  I have to apologise to them!')
if user_input == 'wardens':
    print('My musics so loud. Im was distracted. They reprimanded me')
if user_input == 'other':
    print('The warden was just smiling!')

# question 3 ------------------------------------------

print('\nHow many times should I break free?')

user_input = int(input(''))
breaking_free = 1

for i in range(user_input, 0, -1):
    print('{0}: this is the part where I break free'.format(i))
    breaking_free = breaking_free + 1

print('\nCause I can\'t resist it no more!')

# question 4 ------------------------------------------


def explain(what, where):
    if what == 'monster' and where == 'bed':
        print('\ni\'m friends with the monster that\'s under my bed')
    elif what == 'doctor' and where == 'hospital':
        print('You\'re trying to save me, stop holding you\'re breath')
    else:
        print('You think i\'m crazy, yeah, you think i\'m crazy')


explain('monster', 'bed')
explain('doctor', 'hospital')
explain('stranger', 'street')

# question 5 ------------------------------------------

points = 0

print('\n...Baby, how do you sleep when you lie to me?')

for i in range(4):
    user_input = input('\nLets find out how you sleep... ')
    if user_input == 'very well':
        points = points - 10
        print('I\'m hopin\' that my love will keep you up tonight.')
    elif user_input == 'poorly':
        points = points + 10
        print('All that fear and all that pressure.')
    else:
        print('Love to you is just a game.')

print('\nYou achieved {0} points'.format(points))

# question 6 ------------------------------------------


def describe_friend(friend):
    if friend == '50 cent':
        return 'He be getting rich or die trying'
    elif friend == 'dr dre':
        return 'He be needing California love'
    elif friend == 'rihanna':
        return 'She be needing an umbrella'
    else:
        return 'They be cool'


def display_friend(friend):
    print('\n{} can be described as follows: '.format(friend))
    print(describe_friend(friend))


print('Friend: 50 cent, dr dre, rihanna')


def run():
    user_input = input('\nPlease enter a friend (e.g. \'50 cent\'): ')
    user_command = input('\nWould you like to \'describe\' or \'display\'?: ')
    if user_command == 'describe':
        print(describe_friend(user_input))
    elif user_command == 'display':
        print(display_friend(user_input))
    else:
        print('Invalid command')


run()

