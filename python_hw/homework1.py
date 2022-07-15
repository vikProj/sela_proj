# exercise 1

lst = [3, 7, 2]

histo = ['*' * i for i in lst]

print(histo)

# exercise 2

lst_1 = ['a', 'b', 'c', 'd', 'e']
lst_2 = ['x', 'y', 'z', 'n', 'm']

# version 1
# assumption that 2 list have the same length
length = len(lst_1)
lst_res = []
for ind in range(length):
    lst_res.append(lst_1[ind] + lst_2[length - 1 - ind])

print(lst_res)

# version 2
lst_res_2 = [i + j for i, j in zip(lst_1, lst_2[::-1])]
print(lst_res_2)

