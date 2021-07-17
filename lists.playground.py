# chilli_wishlist = ["igloo", "chicken", "donut toy", "cardboard box"]

#indexing
# print(len(chilli_wishlist)) #4 elements in this list
# print(chilli_wishlist)  # Prints all elements in the list
# print(type(chilli_wishlist)) # shows that Class = 'list'

# print(chilli_wishlist[0]) #"igloo"
# print(chilli_wishlist[1]) #"chicken"
# print(chilli_wishlist[-1]) #"cardboard box"
# print(chilli_wishlist[0:2]) #['igloo', 'chicken']
# print(chilli_wishlist[1:3]) #['chicken', 'donut toy']
# chilli_wishlist[1] = "carrot"  
# print(chilli_wishlist) # ['igloo', 'carrot', 'donut toy', 'cardboard box']
# chilli_wishlist[0] = "blue button"
# print(chilli_wishlist[2:4]) #['donut toy', 'cardboard box']
# print(chilli_wishlist[-3]) #['cardboard box']
# print(chilli_wishlist) #['blue button', 'chicken', 'donut toy','cardboard box']

letters = ["a","b","c","d","e"]
letters.append("f")
letters.extend(["g","m"])
letters.insert(1, "z")
print(letters)

letters.pop(2)
letters.remove("d")
print(letters)