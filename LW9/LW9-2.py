def sum_of_number():
    suma = 0
    for i in arr_in:
        while i > 0:
            suma = suma + (i % 10)
            i = i // 10
        arr_out.append(suma)
        suma = 0
    return arr_out
arr_in = [12, 23, 34, 45]
arr_out = list()
print(sum_of_number())
