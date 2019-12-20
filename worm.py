#!/usr/bin/env python

"""
I intend to make a script that would give me books and pages of an author.
That's all because I, personally, need that quite a lot.
"""
import argparse
from config import config
from goodreads import client

parser = argparse.ArgumentParser(description="Books Information")
parser.add_argument('--auth', '-a', type=int, required=True, help="author number")

args = parser.parse_args()

gc = client.GoodreadsClient(config['key'], config['secret'])
author = gc.author(args.auth)

name = author.name
name = name.replace(' ', '_')

query_name = str(args.auth) + "." + name

query_url = "https://www.goodreads.com/author/show/" + query_name

from lxml import html
import requests

page = requests.get(query_url)
webpage = html.fromstring(page.content)

links = webpage.xpath('//a/@href')

booklinks = list(set([x for x in links if x.startswith("/book/show/")]))

url_add = "https://www.goodreads.com"
books_data = []
for bl in booklinks[:4]:
	d = {}

	bigurl = url_add + bl
	page = requests.get(bigurl)
	webpage = html.fromstring(page.content)
	
	d['name'] = ((bl.split("/")[-1]).split(".")[-1]).replace('_',  ' ')
	d['pages'] = webpage.xpath("//span[@itemprop='numberOfPages']/text()")
	d['avg_ratings'] = webpage.xpath("//span[@itemprop='ratingValue']/text()")[0].replace('\n', '')
	d['reviews'] = webpage.xpath("//meta[@itemprop='reviewCount']/@content")
	d['ratings'] = webpage.xpath("//meta[@itemprop='ratingCount']/@content")
	
	books_data.append(d)
	# break

# print(books_data)
for bd in books_data:
	print("Name: {a} | Pages: {b} | No-of-Ratings: {c} | Avg Ratings: {d}".format(a=bd['name'], b=bd['pages'], c=bd['ratings'], d=bd['avg_ratings']))


