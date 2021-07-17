# is_raining = False
# is_cold = True

# print(is_raining) #F
# print(not is_raining) #T
# print(is_raining or is_cold) #T
# print(is_raining and not is_cold) #F
# print(is_raining or not is_cold) #F
# print(not is_raining and not is_cold) #F

# is_raining = True
# is_cold = True

# print(is_raining) #T
# print(not is_raining) #F
# print(is_raining or is_cold) #T 
# print(is_raining and not is_cold) #F = and is false singular
# print(is_raining or not is_cold) #T = or is true singular
# print(not is_raining and not is_cold) #F

#And is False singluar
#Or is True singular 
#Not is Opposite

# print(not is_raining)
# print(is_raining and is_cold)
# print(is_raining and not is_cold)
# print(type(is_raining))
# print(is_cold)
# print(type(is_cold))

# is_sunny = False
# have_shoes = True
# is_gym_open = True
# print(is_sunny and have_shoes)
# print(is_sunny or is_gym_open)
# print(not is_sunny)

# print(5 < 3) #F
# print(5 > 3) #T
# print(10 >= 10) #T
# print(4 <= 10) #T
# print(5 == 5) #T
# print(5 != 4) #T
# print(5.1 > 2.4) #T
# print("Kim" == "kim") #F
# print("Kim" != "kim") #T

# temperature = 16
# print(temperature < 18) #T
# wind_chill = 3
# print(wind_chill > 4) #F
# print(temperature - wind_chill <16) #T

# name = "Hayley"
# print(name == "Hayley") # True - compares two data sets
# print(name != "Hayley") # False - != agrues data is different, however its the same so answer is false

# name = "Holly"
# print(name == "Hayley") # False - two data sets not comparable
# print(name != "Hayley") # True - argument is correct as the data in fact is not equal

# print("A" > "a")
# print("A" == "A")
# print(ord("A"))
# print(ord("A") == 65)
# print(ord("a"))

# var1 = 5

# if var1 > 3:
#     print("hello")

# name = input("What is your name?")

# if name == "Kim":
#     print ("Hello Kim")
# elif name == "Randall":
#     print("Hi Randall")
# else:
#     print("Hello")

# name = input("What is your name?")

# if name == "Kim":
#     print ("Hello Kim")
# elif name != "Kim":
#     print("Hello")

# if statements
# is_raining = True

# if is_raining:
#     print("Take an umbrella")

# is_raining = False

# if is_raining:
#     print("Take an umbrella")

# else:
#     print("Do not take an umbrella")

#if, elif, else
# temperature = 16
# wind_chill = 3
# if temperature - wind_chill <16:
#     print("Take a jumper")
# elif temperature - wind_chill >30:
#     print("Yuck, it's hot today, go outside later")
# else:
#     print("Wow, what a lovely day")

# temperature = 25
# wind_chill = 1
# if temperature - wind_chill <16:
#     print("Take a jumper")
# elif temperature - wind_chill >30:
#     print("Yuck, it's hot today, go outside later")
# else:
#     print("Wow, what a lovely day")


# #nested if
# if temperature - wind_chill <16 and is_raining:
#     print("Just stay home")
# else: 
#     if is_raining:
#         print("You will need an umbrella today")
#     if temperature - wind_chill <16:
#         print("You will need a jumper today")

# moths_in_house = False

# if moths_in_house:
#     print("Get the Moths")
# else:
#     print("No threats detected.")

# moths_in_house = False
# mitch_is_home = True

# if moths_in_house and mitch_is_home:
#     print("Hoooman! Help me get the moths!")
# elif not moths_in_house and not mitch_is_home: #otherwise do this
#     print("No threats detected")
# elif moths_in_house and not mitch_is_home:  #otherwise do this
#     print("Meooooow! Hisssss!")
# elif not moths_in_house and mitch_is_home: #otherwise do this
#     print("Climb on Mitch")
# else:
#     print("Code needs checking")

# light_colour_Red = False
# light_colour_Green = False
# light_colour_Amber = True
# car_detected = True

# if light_colour_Red and not car_detected:
#     print("Do nothing1")
# elif light_colour_Red and car_detected:
#     print("Flash")
# elif light_colour_Green and not car_detected:
#     print("Do nothing2")
# elif light_colour_Green and car_detected:
#     print("Do nothing3")
# elif light_colour_Amber and not car_detected:
#     print("Do nothing4")
# elif light_colour_Amber and car_detected:
#     print("Do nothing5")

height = int(input("Please input your height in cms"))

if height in range(120, 300):
    print("Hop on!")
elif height in range(1, 119):
    print("Sorry, not today :(")

# username = input("Enter username")
# password = input("Enter password")

# if username == "fluer" and password =="password123":
#     print("Correct!")
# else:
#     print("Incorrect!")

email = input("Please enter your email address")

if '@' in email and '.' in email:
    print("Valid email address.")
else:
    print("Invalid email address.")


