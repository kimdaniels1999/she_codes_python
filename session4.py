# def ask_name(): # Name of function (what variable the function will take)
#     name = input("Whats your name") # variable or paramater = object strftime
#     return name

# kims_name = ask_name()
# print(kims_name)

# def create_greeting(name):
#     greeting = f"Hello" {name}"
#     return greeting

# print(create_greeting("Chilli"))
# print(create_greeting("Angela"))

# def ask_integer():
#     integer = int(input("How old are you?"))
#     return integer

# print(ask_integer()*3)

# def times_three(num):
#     return num * 3

# print(times_three(5))
# print(times_three(32))
# print(times_three(2)+6)
# print(times_three("Hello")

# def convert_cm_to_in(length_cm):
#     length_in_inch = length_cm / 2.54
#     return length_in_inch

# print(convert_cm_to_in(20))

# def convert_in_to_cm(length_in):
#     length_in_cm = length_in * 2.54
#     return length_in_cm

# print(convert_in_to_cm(10))

# def add(a,b):
#     result = a + b
#     return result
#     return a + b
#     print(a + b)

# print(add(2,3))

# def calculate_mean(a, b):
#     total = a + b
#     mean = total/2
#     return mean

# print(calculate_mean(3,4))

# #temp in farenheight to return it celcius

# def temp_in_cel(temp_in_f):
#     temp_in_cel = (temp_in_f - 32) * (5/9)
#     return temp_in_cel

# print(temp_in_cel(32))
# print(temp_in_cel(10.10))

# def is_odd(num):
#     if num % 2 == 0:
#         return False
#     else: 
#         return True

# print(is_odd(8))
# print(is_odd(17))
    
# def mean(num_list):
#     mean = sum(num_list) / len(num_list)
#     return mean

# print(mean([4,3,2,6]))
# print(type(mean))

# def mean(num_list):
#     return sum(num_list) / len(num_list)
#     return mean

# print(mean([10,5,6]))


# def total_cost(price,quantity):
#     return price * quantity 

# print(f"${total_cost(4.25,3)}")
# print(f"${total_cost(3.79,1)}")
# print(f"${total_cost(1.49,7)}")

from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"

my_date = datetime.now()
print(my_date.isoformat())
print(type(my_date)) # datetime.datetime

def convert_f_to_c(temp_in_farenheit):
    convert_f_to_c = (temp_in_farenheit - 32.0) * (5/9)
    return convert_f_to_c

print(convert_f_to_c(150))

def calculate_mean(weather_data):
    # return sum(weather_data) / len(weather_data)
    calculate_mean = sum(weather_data) / len(weather_data)
    return float(calculate_mean)

print(calculate_mean([1,2,3]))

# iso_string = "2021-07-05T07:00:00+08:00"
def convert_date(iso_string):
    x = datetime.strptime(iso_string, "%Y-%m-%dT%I:%M:%S%z")
    return x
    # return x.strftime(%A %d %m %Y)

iso_string ="2021-07-05T07:00:00+08:00"
print(convert_date)
print(type(convert_date)