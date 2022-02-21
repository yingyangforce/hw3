#+---------------------+
#| hw3a - Isaiah Grace |
#+---------------------+

#---Part A---

usr_name = input("Enter a name: ")
usr_number = int(input("Enter a number: "))

def numberChecker(number):
    if usr_number < 0:
        return "a negative number"
    elif usr_number > 0:
        return "a positive number"
    else:
        return "zero"

print(f"{usr_name} entered {numberChecker(usr_number)}!")

