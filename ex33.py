numbers = []

def add_numbers(n, inc = 1):
    i = 0 # not needed when using for-loops, does not affect for-loops
    while i < n:
    # for i in range(0, n, inc):
        print(f"At the top i is {i}")
        numbers.append(i)
        
        i = i + inc # not needed when using for-loops, does not affect for-loops
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

add_numbers(6)

print("The numbers: ")

for num in numbers:
    print(num)