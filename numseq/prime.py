#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Numseq Assessment--Prime Numbers
because we've had the prime of our lives
"""

__author__ = "mhoelzer"


import sys
import argparse


def primes(n):
    """"finds list of primes < n because n hates being copied"""
    return [num for num in range(1, n) if is_prime(num)]


def is_prime(m):
    """"checks if a num is prime because we're too lazy to do the math"""
    if m == 0 or m == 1:
        return False
    for num in range(2, m):
        if m % num == 0:
            return False
    return True


def create_parser():
    """Creates and returns an argparse cmd line option parser"""
    parser = argparse.ArgumentParser(
        description="Perform transformation on input text.")
    parser.add_argument(
        "num", help="include a number to find the ")
    return parser


def main(args):
    """main function used to run primes/is_prime()"""
    parser = create_parser()
    namespace = parser.parse_args()
    if not namespace:
        parser.print_usage()
        sys.exit(1)
    n = int(namespace.num)
    return primes(n), is_prime(n)


if __name__ == "__main__":
    # example of cmdln: python prime.py <integerHere>
    # need to be inside numseq folder
    print(main(sys.argv[1:]))
