#!/usr/bin/env python

"""
I intend to make a script that would give me books and pages of an author.
That's all because I, personally, need that quite a lot.
"""
import argparse
from config import config
from goodreads import client

# gc = client.GoodreadsClient(config['key'], config['secret'])
# book = gc.book(1)
# print(book.title)


parser = argparse.ArgumentParser(description="Books Information")
parser.add_argument('--auth', '-a', type=int, required=True, help="author number")

args = parser.parse_args()
print(args.auth)