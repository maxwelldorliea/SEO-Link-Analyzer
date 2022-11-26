#!/bin/env python3

"""
Link Analyzer Main Module
"""

from sys import argv


def main(args) -> None:
    if len(args) < 2:
        print("Error: missing url\nUsage: ./main.py <weburl>")
        return;
    if len(args) > 2:
        print("Error: Too many argument\nUsage: ./main.py <weburl>")
        return;
    print("Please Hold On We Are Generating Your Result..")

main(argv)

