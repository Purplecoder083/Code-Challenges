"""
Name: Dana Thomas
Date: July 29, 2025
Assignment: Code Challenge 6 
Description: This code explores the use of dictionary methods in Python and their purpose. 
"""
def greeting():
    return "Hello, welcome to Code Challenge 6!"
print(greeting())


# clear()
# Input: Key: value(string, int)
# Return: returns an empty dictionary. 
# Purpose: to remove all items from a dictionary because the owner sold his horse. 
# Example: 
horse = {
    "breed": "Quarter Horse", 
    "age": 6, 
    "color": "Dapple Gray"
}
horse.clear()  # removes all the items from this dictionary. 
print(horse)   # Output: {}

# copy()
# Input: Key: value(string, int)
# Return: returns a copy of the dictionary. 
# Purpose: to return a copy of the specified dictionary because the owner needs to give a copy to the vet.
# Example: 
dog = {
    "breed": "Labrador Retriever",
    "age": 2,
    "color": "black"
}
dog_copy = dog.copy()
print(dog_copy) 

# fromkeys()
# Input: Key: value(string, int)
# Return: returns a dictionary with specified keys and a specific value.
# Purpose: to return a dictionary with specified keys and a specific value because the farmer wants to sell his new fruits but at a default price. 
# Example:
my_key = ("plum", "cherry", "pear")
number = (50)  #50 cents per pound

def create_dict():
    return dict.fromkeys(my_key, number)  #Output: {"plum": 50, "apple": 50, "pear": 50}

print(create_dict())

# get()
# Input: key: value(string, int)
# Return: returns the value associated with the key. 
# Purpose: to return the value of a specified key because the woman wants to know the age of her chicken. 
# Example:
chicken = {
    "breed": "White Leghorn",
    "age": 1,    #years
    "color": "white"
}
def get_breed():
    return chicken.get("age")   #Output: 1 (year)

print(get_breed()) 

# items()
# Input: Key: value(string, int)
# Return: returns key-value pairs in the dictionary. 
# Purpose: to return a view object showing a list of dictionary's key-value pairs because the teacher is reviewing Bob's information. 
# Example:
student = {
    "name": "Bob",
    "age": 14,        #years
    "favorite_subject": "Computer Programming"
}
def get_items():
    return student.items()  #Output: dict_items([('name', 'Bob'), ('age', 14), ('favorite_subject', 'Computer Programming')])

print(get_items())

# keys()
# Input: Keys: value(string, int)
# Return: returns a list of all the keys in the dictionary. 
# Purpose: to return a view object showing a list of all the keys in the dictionary because the students want to ask the teacher these facts and learn more about him. 
# Example:
teacher = {
    "name": "Mr. Smith",
    "age": 35,
    "subject": "Rhetoric"
}
def get_keys():
    return teacher.keys()  #Output: dict_keys(['name', 'age', 'subject'])

print(get_keys())

# pop()
# Input: Key: value(string, int)
# Return: returns value associated with the key
# Purpose: remove "age" from the dictionary because the owner does not want to tell people how old his car is anymore. 
# Example:
car = {
    "make": "Chevrolet",
    "model": "Camaro", 
    "age": 20
}
def remove_age():
    return car.pop("age")  #Output: 20, dictionary is now {"make": "Chevrolet", "model": "Camaro"}

print(remove_age())  #Output: 20
print(car)           #Output: {'make': 'Chevrolet', 'model': 'Camaro'}

# popitem()
# Input: Key: value(string, float)
# Return: returns the last key-value pair in the dictionary. 
# Purpose: to remove the last key-value pair from the dictionary because the baker wants to take the price of the cookie off the menu. 
# Example:
cookie = {
    "type": "Chocolate Chip",
    "size": "Large",
    "price": 2.50
}
def remove_price():
    return cookie.popitem() #Output: ('price', 2.5), dictionary is now {"type": "Chocolate Chip", "size": "Large"}

print(remove_price())  #Output: ('price', 2.5)
print(cookie) 

# setdefault()
# Input: Key: value(string, int)
# Return: returns the value associated with key, but if the key does not exist, the default value is returned. 
# Purpose: to set a default value for a key in the dictionary because the librarian wants to add The Lion the Witch and the Wardrobe, but she 
#but she does not know if it is already at her libray or not. 
# Example:
book = {
    "title": "The Lion the Witch and the Wardrobe",
    "author": "C.S. Lewis",
    "published": 1950
}
def set_default_genre():
    return book.setdefault("genre", "Fantasy") #Output: {"title": "The Lion the Witch and the Wardrobe", "author": "C.S. Lewis", "published": 1950, "genre": "Fantasy"}

print(set_default_genre()) 
print(book)

# update()
# Input: Key: value(string, float)
# Return: returns the updated dictionary of (string, int) values. 
# Purpose: to update a specified item in the dictionary because the plant grew taller and the owner wants to update the new height. 
# Example:
plants = {
    "type": "Fern",
    "age": 2,          #years
    "height": 12.5     #inches
}

def update_height():
    plants.update({"height": 18})
    return plants

print(update_height()) #Output: {'type': 'Fern', 'age': 2, 'height': 18}

# values()
# Input:
# Return:
# Purpose:
# Example:
hair = {
    "color": "Blonde",
    "Length": "Long",
    "type": "curly"
}
def get_values():
    return hair.values()  #Output: dict_values(['Blonde', 'Long', 'curly'])

print(get_values())  


def goodbye():
    return "Goodbye, thank you for completing Code Challenge 6!"
print(goodbye())