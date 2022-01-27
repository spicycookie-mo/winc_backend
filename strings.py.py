# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

#----part 1
player_1='Ruud Gullit'
player_2='Marco van Basten'
goal_0=32
goal_1=54
scorers=player_1+' '+str(goal_0)+', '+player_2+' '+str(goal_1)
print(scorers)
report=f'{player_1} scored in the {goal_0}nd minute\n{player_2} scored in the {goal_1}th minute'
print(report)

#----part 2
player='Ruud Gullit'

###intermediate steps
#x=player.find('Ruud') 
#y=player.find(' ')
#print(x)
#print(y)
first_name=player[player.find('Ruud'):player.find(' ')]
print(first_name)

# tried to do it like this in one line 
# last_name_len=len(player[player.find('Gullit'):])
# output is correct but
""" wincpy returned error Error: Can't import strings from directory[..]
We got this error: name 'last_name' is not defined"""
z=player.find('Gullit')
print(z)
last_name=player[z:]
print(last_name)
last_name_len=len(last_name)    
print(last_name_len)

name_short=f'{first_name[0:1]}. {last_name}'
print(name_short)

#chant_0=(' '+first_name+'!')*len(first_name) - intermediate step
chant=((' '+first_name+'!')*len(first_name))[1:]
print(chant)

good_chant=chant[-1]!=' '
print(good_chant)