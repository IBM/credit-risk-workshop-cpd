#! /usr/bin/env python
import argparse
import time

parser = argparse.ArgumentParser(description="Converts WKC categories to be unique "
            "by prepending a Tag or initials are required as a parameter."
            "Default tag is time.time().")
parser.add_argument("-T" ,"--tag", 
                    help="Tag or initials to prepend to category.")

args = parser.parse_args()

prepend = args.tag or time.time()
IN_FILE = "glossary-organize-categories.csv"
OUT_FILE = prepend + "-glossary-organize-categories.csv"
categories = ['Data Privacy', 'Payment Card Industry', 'Mortgage Default Analysis',
                'Sensitive Information']

with open(IN_FILE, newline="") as in_file:
    with open(OUT_FILE, "w") as out_file:
        for line in in_file:
            words = line.split(",")
            for i, word in enumerate(words):
                if words[i] in categories:
                    word = prepend + "-" + word
                    words[i] = word

            out_file.write(','.join(words))

            

