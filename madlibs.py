# def madLib():
#     print("Please fill in the blanks below:")
#     print("___(name)___'s favorite subject in school is ___(subject)___")
#     input1 = input("What is name? ")
#     input2 = input("What is subject? ")
#     print(input1 + "'s favorite subject in school is " + input2 + ".")


# madLib()

def madLib(name, subject):
    the_madlib = "Your name is %s and your favorite subject is %s." % (name, subject)
    return the_madlib

my_story = madLib("Luke", "History")
print(my_story)