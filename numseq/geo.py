#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Numseq Assessment--Geometric Numbers"""

__author__ = "mhoelzer"


import sys
import argparse


def square(n):
    """"finds the square of a number because cloning has gone too far"""
    return n**2


def triangle(n):
    """"finds the nth triangular number because it has 3 good points"""
    # total_n = 0
    # while n > 0:
    #     total_n += n
    #     n -= 1
    # return total_n
    return (n * (n + 1))/2


def cube(n):
    """"finds the cube of a number because squares are too basic"""
    return n**3  # or n*n*n


def create_parser():
    """Creates and returns an argparse cmd line option parser"""
    parser = argparse.ArgumentParser(
        description="Perform transformation on input text.")
    parser.add_argument(
        "num", help="add a number to find the nth square/triangle/cube of")
    return parser


def main(args):
    """main function used to run square/triangle/cube()"""
    parser = create_parser()
    namespace = parser.parse_args()
    if not namespace:
        parser.print_usage()
        sys.exit(1)
    n = int(namespace.num)
    return square(n), triangle(n), cube(n)


if __name__ == "__main__":
    # example of cmdln: python fib.py <integerHere>
    # need to be inside numseq folder
    print(main(sys.argv[1:]))
