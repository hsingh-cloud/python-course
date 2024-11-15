user_age = int(input('What is your age?'))
if user_age > 30:
    print('You are over 30 years old')
    print('Sorry you do not qualify')
elif user_age == 30:
    print('You are exactly 30 years old')
    print('You will need to meet additional conditions to qualify')
else:
    print('You are 30 years old or younger')
    print('Congratulations! You qualify')

password = input('Do you the secret password?')
if password != '--secret':
    print('not correct')
else:
    print('correct password')


if True:
    print('Condition met')
