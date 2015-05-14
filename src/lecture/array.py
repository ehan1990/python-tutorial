__author__ = 'ehan'


def main():
    even_numbers = [0, 2, 4, 6, 8]
    odd_numbers = [1, 3, 5, 7, 9]
    cities = ["vancouver", "beijing"]
    print even_numbers
    print odd_numbers
    print cities
    print "I was born in " + cities[1] + " but now I live in " + cities[0]
    length_of_even_numbers = len(even_numbers)
    print "there are " + str(length_of_even_numbers) + " in the array: " + str(even_numbers)
    even_numbers.append(10)
    even_numbers.append(12)
    even_numbers.append(14)
    print "You can add more numbers to the array: " + str(even_numbers)

if __name__ == "__main__":
    main()