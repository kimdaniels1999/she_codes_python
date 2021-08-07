# class book:
#     def _init_(self, title, author, pages, current_page):
#         self.title = title
#         self.author = author
#         self.pages = pages
#         self.current_page = 

#     def _str_(self):
#         return f"Title:{self.title}, Author:{self.autor}"

class Book:
    #attributes - size, pages, colour, thickness
    #methods - turning a page, closing, opening

    def __init__(self, title, author, pages, current_page):
        #assignment to object attributes
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = current_page
        self.bookmark = 1  #assign by default
    
    def bookmark_page(self):
        self.bookmark = self.current_page
    
    def turn_page(self):
        self.current_page += 1

    def turnback_page(self):
        self.current_page += -1

    def goto_page(self, page):
        self.current_page = page

    #string representation
    def __str__(self):
        return f"Title:{self.title}, Author:{self.author}, Pages:{self.pages}"
    
    def __len__(self):
        return self.pages

    #create a method turn back the page
    

my_book = Book("A great book", "me", 198, 10)
my_book.goto_page(4)
print(my_book.current_page)
# print(my_book.__str__())
# print(my_book)
# print(my_book.bookmark) #attr
# my_book.turn_page() #method
# print(my_book.turn_page())
# print(my_book.turnback_page())
# my_book.bookmark_page()
# print(my_book.bookmark)

class Vehicle:
    def __init__(self, make, model, colour, capacity, max_speed):
        self.make = make
        self.model = model
        self.color = colour
        self.capacity = capacity
        self.max_speed = max_speed

    def _str_(self):
        return f"Vehicle Summary: Make:{self.make}, Model:{self.model}, Colour:{self.color}, Capacity:{self.capacity}, Max Speed:{self.max_speed}"
        
ford = Vehicle("ford","ute","white",8, 200)
print(ford)