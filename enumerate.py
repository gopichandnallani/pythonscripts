matrix = [[1,2,3], [2,3,5], [4,8,9]]

for i, row in enumerate(matrix):
    for j, element in enumerate(row):
        if element % 2 == 0: # then the element will be even 
            print(f"The even number {element} is at position ({i}, {j}) in the matrix")
