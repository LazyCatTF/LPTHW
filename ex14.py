from sys import argv

script, adj, user_name = argv
prompt = '>>>'

print(f"Hi {adj} {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print("What color is your clothes now?")
color = input(prompt)

print(f""" 
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
Wish you have a nice day with your {color} clothes~~
""")