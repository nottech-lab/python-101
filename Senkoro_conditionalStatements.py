#using if statement
#The program displays what to wear on a hot day
#and displays a wonderfull day despite the weather
hot=True
if hot:
  print('Wear light clothes')
print('Its a wonderful day')


#using if else statement
#The program displays what to do if its hot and when its not hot
#and displays its a wonderfull day despite the weather
is_hot_day=True
if is_hot_day:
    print('Drink alot of water')
else:
    print('Wear a sweater')
print("it's a wonderfull day")


#using elif
#The program displays what to wear if its a cold or a hot day
#and  display that its a wonderfull day if neither hot or cold
is_hot=False
is_cold=True
if is_hot:
    print('Wear light clothes')
elif is_cold:
    print('Wear warm clothes')
else:
    print('Its a wonderfull day')