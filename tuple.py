# A tuple is a collection which is ordered and unchangeable.
# allows deplicate values.
# 
veggies = ("carrot", "beet", "broccoli", "tomato", "cabbage")
print(type(veggies))

tuple = (1,2,3, True, False, "devops", "cloud", "aws")
print(veggies[:3])

y = list(veggies)
y[1] = "lettuce"
print(y)
veggies = tuple(y)
# print(veggies())