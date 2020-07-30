num = int(input("Please enter a number: "))
def is_even(num):
    if num % 2 != 0:
        return False
    else:
        return True

print(is_even(num))