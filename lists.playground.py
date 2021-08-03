# The group of elements is called a list
# A list in python can also contain lists inside it as elements, these nested lists are called sublists.


chilli_wishlist = ["igloo", "chicken", "donut toy", "cardboard box"]

#indexing
print(len(chilli_wishlist)) #4 elements in this list
print(chilli_wishlist)  # Prints all elements in the list
print(type(chilli_wishlist)) # shows that Class = 'list'

print(chilli_wishlist[0]) #"igloo"
print(chilli_wishlist[1]) #"chicken"
print(chilli_wishlist[-1]) #"cardboard box"
print(chilli_wishlist[0:2]) #['igloo', 'chicken']
print(chilli_wishlist[1:3]) #['chicken', 'donut toy']
chilli_wishlist[1] = 'carrot'  
print(chilli_wishlist) # ['igloo', 'carrot', 'donut toy', 'cardboard box']
chilli_wishlist[0] = "blue button"
print(chilli_wishlist[2:4]) #['donut toy', 'cardboard box']
print(chilli_wishlist[-3]) #['carrot']
print(chilli_wishlist) #['blue button', 'chicken', 'donut toy','cardboard box']


letters = ["a","b","c","d","e"]
letters.append("f") # add to the end
letters.extend(["g","m"]) # extend the list out
letters.insert(1, "z") # inserting a value using index/position
print(letters)

letters.pop(2) # position or index removal
letters.remove("d")  # value removal
print(letters)

foods = [
    "orange",
    "apple",
    "banana",
    "strawberry",
    "grape",
    "blueberry",
    ["carrot", "cauliflower", "pumpkin"],
    "passionfruit",
    "mango",
    "kiwifruit"
]

print(foods[0])
print(foods[2])
print(foods[-1])
print(foods[0:3])
print(foods[7:10])
print(foods[6][-1])

mailing_list = [
    ["Chilli", "chilli@thechihuahua.com"],
    ["Roary", "roary@moth.catchers"],
    ["Remus", "remus@kapers.dog"],
    ["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],
    ["Ivy", "noreply@goldendreamers.xyz"],
]

print(mailing_lis[0:4])
list2 = (mailing_list[1])
list3 = (mailing_list[2])
list4 = (mailing_list[3])
list5 = (mailing_list[4])



mail = (f"{mailing_list[0]}: {mailing_list[1]}")
print(mail)


for i in mailing_list:
    print(f"{i[0]}: {i[1]}")
    print(*i) # will print nested list without brackets, comma and separators

print(f"{mailing_list[0]}: {mailing_list[1]}")
print(*mailing_list[0], sep=",")  # chilli, chilli@thechihuahua.com


phone = ["Samsung","Apple","Huawei","Nokia","Windows"]
separator = ","
print(phone) # normal list
print(*phone, sep=",") # removes brackets
print(','.join(phone)) # removes brackets
print(separator.join(phone)) # removes brackets


name = input("What is your name?")
name2 = input("What is your mothers name?")
name3 = input("What is you fathers name?")
list = [name, name2, name3]
print(list)

a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]
d = []
e = []

list = [a, b, c]
print(list)
list2 = [*a, *b, *c]
print(list2)

a, s, c = "blue", "yellow", "red"
print(a)
print(s)
print(c)
a = s = c = "blue"
print(a)
print(s)
print(c)

fruits = ["apples", "berries", "oranges"]
a, s, c = fruits
print(a)
print(s)
print(c)

x = "awesome"
y = "Python is "
z = y + x
print(z)

a = " Hello, World! "
print(a.upper())
print(a.lower())
print(a.strip())
print(a.replace("H","J")) # Jello, World!
print(a.split(",")) # add contents innto a list if items are separated using a comma

a = "Hello"
b = "World"
c = a + " " + b
print(c)
c = a + b
print(c)

age = 36
txt = "My name is John and I am {}"
print(txt.format(age))

quantity = 3
item = 567
price = 49.95
my_order = "I want {2} peices of item {0} for {1} dollars"
print(my_order.format(quantity, item, price))

txt = "We are the so-called \"Vikings\" from the North" 
print(txt)

txt = "Hello\nWorld!"
print(txt) 

txt = "This will insert one \\ (backslash)."
print(txt) 

# you can combine string with a string, number with a number and float with a float
# if you try to combine a string with a number python will give you an error


