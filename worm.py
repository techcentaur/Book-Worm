#!/usr/bin/env python

"""
I intend to make a script that would give me books and pages of an author.
That's all because I, personally, need that quite a lot. 
PS: short book as of less time.
"""

import requests
import argparse
from lxml import html

parser = argparse.ArgumentParser(description="Books Information")
parser.add_argument('--auth', '-i', type=int, required=True, help="author number")
parser.add_argument('--name', '-n', type=str, required=True, help="author name")
args = parser.parse_args()

namelist = (args.name).split()
name = "_".join([x.capitalize() for x in namelist])

query_name = str(args.auth) + "." + name
query_url = "https://www.goodreads.com/author/show/" + query_name

page = requests.get(query_url)
webpage = html.fromstring(page.content)

links = webpage.xpath('//a/@href')
booklinks = list(set([x for x in links if x.startswith("/book/show/")]))

url_add = "https://www.goodreads.com"
books_data = []
for bl in booklinks[:2]:
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

for bd in books_data:
	print("Name: {a} \n\tPages: {b} \n\tNo-of-Ratings: {c} \n\tAvg Ratings: {d}".format(a=bd['name'], b=bd['pages'], c=bd['ratings'], d=bd['avg_ratings']))


