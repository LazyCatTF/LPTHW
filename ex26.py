from sys import argv                                # missing line

print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()                                    # missing line
print("How much do you weigh?", end=' ')            # missing )
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

script, filename = argv

txt = open(filename)                                # mis-spelling 'filename'

print(f"Here's your file {filename}:")              # format string missing 'f'
print(txt.read())                                   # mis-spelling 'txt'

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())                             # mistaking . for _


print("Let's practice everything.")                 # mis-using ' in a string
print('You\'d need to know \'bout escapes')         # wrong multi-line printing
print('with \\ that do \n newlines and \t tabs.')   # wrong multi-line printing

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("--------------")                             # missing "
print(poem)
print("--------------")                             # missing "


five = 10 - 2 + 3 - 6                               # missing number
print(f"This should be five: {five}")               # missing )

def secret_formula(started):                        # missing :
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100                             # missing operator
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)   # missing variable

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)               # missing _
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))



people = 20
cats = 30                                           # mis-spelling 'cats'
dogs = 15


if people < cats:
    print("Too many cats! The world is doomed!")    # missing ()

if people > cats:                                   # wrong operator
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:                                   # missing :
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:                                  # missing :
    print("People are less than or equal to dogs.") # missing "


if people == dogs:                                  # wrong operator
    print("People are dogs.")

