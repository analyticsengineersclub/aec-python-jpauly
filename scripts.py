# Write a loop that uses `while` instead of the built-in looping structure
x = 0
while x < 3:
    x+=1
print(x) # expect x = 3 at end of loop 

# Write a loop that loop over the keys in a dictionary and prints the values
units = 'inches'
snow_forecast = {'Monday': 0, 'Tuesday': 3, 'Wednesday': 1, 'Thursday': 13, 'Friday': 4, 'Saturday': 0, 'Sunday': 0}
for day in snow_forecast:
    print(f"{day} snow forecast is {snow_forecast[day]} {units}")

# Write the functions `is_odd` and `is_even` that are shown in the lecture
def is_odd(number):
    if number%2 == 1:
        return True
    else: 
        return False

def is_even(number):
    if number%2 == 0:
        return True
    else: 
        return False

# Loop over `my_first_list` and square the value if the value is a number, and print the calories of the fruit if it’s a fruit (hint: use the dictionary to look up the calories)

def square_int(number):
	squared = number**2
	return squared

my_first_list = ['apple', 1, 'banana', 2]
cal_lookup = {'apple': 95, 'banana': 105, 'orange': 45}

for item in my_first_list:
    item_data_type = type(item)
    if item_data_type == int:
        squared = square_int(item)
        print(f"{item} squared = {squared}")
    elif item in cal_lookup:
        calories = cal_lookup[item]
        print(f"The {item} has {calories} calories")


"""
Write a function that:
    - Takes a dictionary as an argument
    - Loops over the keys in the dictionary
    - Prints the square of the value in the value
    - Hint: use the `cal_lookup` dictionary for testing.
"""

def square_dict(dictionary):
    for key, value in dictionary.items():
        squared = square_int(value)
        print(f"{key} squared = {squared}")

square_dict(cal_lookup)