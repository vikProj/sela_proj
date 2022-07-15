# 1
print('##################  Exercise #1 ########################')

#input_str = 'abc123abc123abc456'

input_str = input("Please enter string: ")

counts_dict = {}

for ch in input_str:
    counts_dict[ch] = counts_dict.get(ch, 0) + 1

print(counts_dict)

# a

for key in sorted((counts_dict.keys())):
    print(f'{key}- {counts_dict[key]}')

# b

reversed_dict = {}
for key, value in counts_dict.items():
    reversed_dict[value] = reversed_dict.get(value, []) + [key]

print(reversed_dict)

#############################################################
print(2 * '\n')

print('##################  Exercise #2 ########################')

# 2

lst1 = [11, 7, 5, 8, 5, 37, 11, 5]
lst2 = [22, 8, 10, 1, 11]
lst3 = [71, 3, 22, 8, 2, 14, 1]

repeated_values_lists = []
unique_values_lists = []

# a

if len(lst1) > len(set(lst1)):
    repeated_values_lists.append(lst1)
else:
    unique_values_lists.append(lst1)

if len(lst2) > len(set(lst2)):
    repeated_values_lists.append(lst2)
else:
    unique_values_lists.append(lst2)

if len(lst3) > len(set(lst3)):
    repeated_values_lists.append(lst3)
else:
    unique_values_lists.append(lst3)

print(f'Repeated values lists are : \n{repeated_values_lists}')
print(f'Unique values lists are : \n{unique_values_lists}')

# b
common_values = []

if len(unique_values_lists) > 0:
    common_values = set.intersection(*map(set, unique_values_lists))

print(f'Common values: {common_values}')

################################################################
print(2 * '\n')

print('##################  Exercise #3 ########################')

lst = [31, 99, 3, 1943]
# sort_order = 'asc'
sort_order = 'desc'

distinct_digits = set()

for num in lst:
    while num // 10 > 0:
        distinct_digits.add(num % 10)
        num //= 10

if sort_order == 'desc':
    print(sorted(distinct_digits, reverse=True))
else:
    print(sorted(distinct_digits))

