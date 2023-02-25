# python list
# lists can have the Duplicate values
# list is changeable, we can add and delete the items after creating the list.
fruits = ["apple", "banana", "grapes", "oranges", "watermelon", "apple" ]
print(len(fruits))

mylist = [True, False, 1,2,3,4,5, "cherry", "bittergourd"]
print(type(mylist))
# access list items
print(fruits[:4])
# changesing the items in the list
fruits[5] = "blackcurrent"
print(fruits)

fruits.insert(3, "kiwi")
print(fruits)

tuple = ("berry", "cherry")
fruits.extend(tuple)
print(fruits)

fruits.remove("apple")
print(fruits)

fruits.pop(4)
print(fruits)

for x in fruits:
    print(x)

new_fruits = [x for x in fruits if x != "apple"]
print(new_fruits)
new_fruits.sort(reverse = True)
print(new_fruits)
