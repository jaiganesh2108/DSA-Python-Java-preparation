my_array = [64, 34, 25, 5, 22, 11, 90, 12]

n = len(my_array)

for i in range(n-1):
    min_index = i
    for j in range(i+1, n):
        if my_array[j] < my_array[min_index]:
            min_index = j
        min_value = my_array.pop(min_index)
        my_array.insert(i, min_value)

print("sorted array is:", my_array) 