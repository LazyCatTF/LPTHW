from sys import argv

script, user_name, gender = argv
prompt = 'input your answer please:'

print "Hi %s %s, I'm the %s script." % (gender, user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print "What color is your clothes now"
color = raw_input(prompt)

print """ 
Alright, so you said %r about like me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
Wish you have a nice day with your %r clothes~~
""" % (likes, lives, computer, color)