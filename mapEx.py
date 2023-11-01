def square(x):
    return x ** 2


numbers = [2, 3, 4, 5, 6, 7]
map_obj = list(map(square, numbers))
print(map_obj)


list_1 = [1, 2, 3]
list_2 = [2, 3, 4]
list_3 = [3, 4, 5]
zip_obj = list(zip(list_1, list_2, list_3))
# print(list(zip_obj))
zip_final = [list(x_l) for x_l in zip_obj]
print(zip_final)