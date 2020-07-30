list1 = [1, 2, 3, 4, 5, 6]
list2 = []

def is_even(list1):
    for list1 in list1:
        if list1 % 2 == 0:
            list2.append(list1)

is_even(list1)
print(list2)