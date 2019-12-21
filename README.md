# Book-Worm
Given author name get all the books, pages, and information related.

## How to Use

- Clone the repository as `git clone https://github.com/techcentaur/Book-Worm.git`
- Move into the folder `cd Book-Worm`
- Install the requirements as `pip install requirements.txt --user`
- Get the Goodreads-ID of the author
	- If you search Albert Camus Goodreads the line would be `https://www.goodreads.com/author/show/957894.Albert_Camus`
	- So you can see: `957894` is the author ID
- Run the script as `python3 worm.py -a 957894 -n "Albert Camus"`
- Result would be:

```console
 solanki@hobbes   ~/GitHub/Book-Worm     master    python3 worm.py -i 957894 -n "Albert Camus"         1 ↵  11    915  17:24:19  
Name: Caligula 
	Pages: ['224 pages'] 
	No-of-Ratings: ['8100'] 
	Avg Ratings:   4.08
Name: The Myth of Sisyphus 
	Pages: ['192 pages'] 
	No-of-Ratings: ['18841'] 
	Avg Ratings:   4.15
Name: The Fall 
	Pages: ['147 pages'] 
	No-of-Ratings: ['63920'] 
	Avg Ratings:   4.04
Name: The Rebel 
	Pages: ['320 pages'] 
	No-of-Ratings: ['11045'] 
	Avg Ratings:   4.14
Name: The Stranger 
	Pages: ['123 pages'] 
	No-of-Ratings: ['623800'] 
	Avg Ratings:   3.97
Name: Exile and the Kingdom 
	Pages: ['213 pages'] 
	No-of-Ratings: ['9363'] 
	Avg Ratings:   3.89
Name: The Myth of Sisyphus and Other Essays 
	Pages: ['212 pages'] 
	No-of-Ratings: ['37483'] 
	Avg Ratings:   4.20
Name: The Plague 
	Pages: ['308 pages'] 
	No-of-Ratings: ['137315'] 
	Avg Ratings:   3.98
Name: The First Man 
	Pages: ['359 pages'] 
	No-of-Ratings: ['5935'] 
	Avg Ratings:   3.96
Name: A Happy Death 
	Pages: ['144 pages'] 
	No-of-Ratings: ['9753'] 
	Avg Ratings:   3.82
```
Well, so I will select `A Happy Death`  in this case, as of my reason to study books with less pages. Don't blah me! It's a fantastic book, spoiler alert!

## Argparse Help
```bash
 solanki@hobbes   ~/GitHub/Book-Worm     master    python3 worm.py -h                                      11    915  17:24:35  
usage: worm.py [-h] --auth AUTH --name NAME

Books Information

optional arguments:
  -h, --help            show this help message and exit
  --auth AUTH, -i AUTH  author number
  --name NAME, -n NAME  author name
```

## Issues and Contribution

I wanted to read books with less pages and good ratings of a particular author, and I am super lazy to do it manually for all the books, that is undeniable. So python is here for the rescue.

If you have an issue, put up one, I will do it. Or if you have already done it, make a PR, happy to get you in.

## Goodreads

I am on goodreads. Add me if you will: [Here Linketh](https://www.goodreads.com/ankitsolanki) 

