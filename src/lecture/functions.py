__author__ = 'ehan'

def add_one(x):
    y = x + 1
    print "i added " + str(x) + " to y"
    return y

def return_boolean():
    return True

def return_string():
    return "hello!"

def return_five():
    return 5

def bar():
    print "now i'm in the bar function"

def foo():
    print "now i'm in the foo function"

def main():
    print "now i'm at the main function"

if __name__ == "__main__":
    print "program starts here"
    main()
    foo()
    bar()

    five = return_five()
    print "i can also return a number: " + str(five)

    text = return_string()
    print "i can also return a string: " + str(text)

    bool = return_boolean()
    print "return a boolean: " + str(bool)

    y = add_one(5)
    print "value of y: " + str(y)