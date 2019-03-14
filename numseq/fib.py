#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Numseq Assessment--Fibonacci Numbers"""

__author__ = "mhoelzer"


import sys
import argparse


def fib(n):
    """"finds the nth fib num because we don't care about the other numbers"""
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


def create_parser():
    """Creates and returns an argparse cmd line option parser"""
    parser = argparse.ArgumentParser(
        description="Perform transformation on input text.")
    parser.add_argument(
        "num", help="add a number to find the nth fib of")
    return parser


def main(args):
    """main function used to run fib()"""
    parser = create_parser()
    namespace = parser.parse_args()
    if not namespace:
        parser.print_usage()
        sys.exit(1)
    n = int(namespace.num)
    return fib(n)


if __name__ == "__main__":
    # example of cmdln: python fib.py <integerHere>
    # need to be inside numseq folder
    print(main(sys.argv[1:]))
