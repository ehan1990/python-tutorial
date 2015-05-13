"""
4 types of common variables: integer, float, string, text

int + int = int
float + int = float
float + string = error, str(float) + string = good
int + string  = error, str(int) + string = good

int + boolean = error
float + boolean = error
string + boolean = error, string + str(boolean) = good
"""

__author__ = 'ehan'

if __name__ == "__main__":
    # ----- integer -----
    # set x = 1
    x = 1
    # set y = x + 1
    y = x + 1
    # prints value of x
    print x
    # prints value of y
    print y

    # ----- float -----
    # set a = 10
    a = 10.0
    # set b = 10
    b = 8.0
    # set c = a - b
    c = a - y
    # prints the value of c
    print c

    # ----- String -----
    # set value of name to "Edward"
    name = "Edward"
    # set value of age to 24
    age = 24
    # the + sign means you are adding the text together
    print "My name is " + name
    # the str() means you are making the age variable to a string because string + int = error
    print "I am " + str(age) + " years old"

    # ----- Boolean -----
    # set is_raining variable to false
    is_raining = False
    print "Is it raining today: " + str(is_raining)
    # if is_raining is true
    if is_raining == True:
        # print this line
        print "Yes, it is raining"
    # otherwise (is_raining is set to false)
    else:
        # print this line
        print "No, it is not raining"

    # ----- Boolean ----