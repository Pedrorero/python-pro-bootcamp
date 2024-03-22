##append elements to a list
# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)
# motorcycles.append('ducati')
# print(motorcycles)

# motorcycles = []
# motorcycles.append('honda')
# motorcycles.append('yamaha')
# motorcycles.append('suzuki')
# print(motorcycles)

##insert elements to a list
# motorcycles = ['honda', 'yamaha', 'suzuki']
# motorcycles.insert(0, 'ducati')
# print(motorcycles)

##removing an item from a list using the del statement
# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)
# del motorcycles[0]
# print(motorcycles)

##Removing an Item Using the pop() Method
# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)
# popped_motorcycle = motorcycles.pop()
# print(motorcycles)
# print(popped_motorcycle)
# last_owned = motorcycles.pop()
# print(f"The last motorcycle I owned was a {last_owned.title()}.")

###Popping Items from Any Position in a List
##If you’re unsure whether to use the del statement or the pop() method, 
##here’s a simple way to decide: when you want to delete an item from a 
##list and not use that item in any way, use the del statement; if you want 
##to use an item as you remove it, use the pop() method.

##Removing an item by value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
#motorcycles.remove('ducati')
#print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")
