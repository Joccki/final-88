# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

#Assignment part one
first_goalscorer = 'Ruud Gullit'
second_goalscorer = 'Marco van Basten'
goal_0 = 32
goal_1 = 54

scorers = first_goalscorer + " " + str(goal_0) + ", " + second_goalscorer + " " + str(goal_1)
report = f"{first_goalscorer} scored in the {goal_0}nd minute\n{second_goalscorer} scored in the {goal_1}th minute"

print(report)

#Assignment part two
player = 'Frank Rijkaard'
first_name = player[:5]
last_name = player[6:]
last_name_len = len(last_name)
name_short = first_name[:1]+ ". " + last_name
chant = (first_name + "! ") * 4 + (first_name + "!")
good_chant = chant != " "