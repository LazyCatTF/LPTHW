print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

print("Now, give me an integer and I'll double it.", end=' ')
x = int(input())
print(x * 2)

# new way to use it:
name = input("What is your name? ")
print(f"Nice to see you {name}!")