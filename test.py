__author__ = "mhoelzer"


"""
this is for testing
because tests are the bests
everything could also be outside the main/on its own and work with same cmdln
"""


from numseq.fib import fib
from numseq.geo import square, triangle, cube
from numseq.prime import primes, is_prime


def main():
    """main function to check each file and function"""
    print("Fibonacci")
    for i in range(10):
        print("{}: {}".format(i, fib(i)))

    print("Geometric numbers (square, triangle, cube)")
    for i in range(10):
        print("{}: {} {} {}".format(i, square(i), triangle(i), cube(i)))

    print("Primes")
    prime_list = primes(1000)
    for p in prime_list[-10:]:
        print(p)
    print("Is 999981 prime? {}".format(is_prime(999981)))
    print("Is 999983 prime? {}".format(is_prime(999983)))


if __name__ == "__main__":
    # example of cmdln: python test.py
    main()
