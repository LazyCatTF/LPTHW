name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
height_cm = height * 2.54
print(f"He's {height_cm} centimetres tall.")

print(f"He's {weight} pounds heavy.")
weight_kg = weight * 0.4536
print(f"He's {weight_kg} kilograms heavy.")

print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

print(round(1.7333)) # 四舍五入为整数
print(round(1.7333, 2)) # 四舍五入到小数点后2位