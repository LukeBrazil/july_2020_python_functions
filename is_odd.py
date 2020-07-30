num = int(input("Please enter a number: "))
def is_odd(num):
    if num % 2 == 0:
        return False
    else:
        return True

print(is_odd(num))