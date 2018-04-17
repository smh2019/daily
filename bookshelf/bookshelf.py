#!/usr/bin/python3

import sys

if len(sys.argv) < 2:
	print("Syntax: ./bookshelf.py <filename>")
	exit()

print("Bookshelf problem")

#path = 'example_input'
ci = open(sys.argv[1],'r')
line = ci.readline()

# Sort bookshelves from largest to smallest
shelves = line.split()
shelves = [int(x) for x in shelves]
shelves.sort()
shelves.reverse()

# Create and sort list of books
books = []
line = ci.readline()
while line:
	tmp = line.split()
	books.append(tmp[0])
	line = ci.readline()

books = [int(x) for x in books]
books.sort()
books.reverse()
ci.close()

print("\tShelves: " + str(len(shelves)))
print("\tBooks: " + str(len(books)))

# How many Shelves
total_shelves = 0

for shelf in shelves:
	if len(books) <= 0:
		break
	total_shelves += 1

	total_books = len(books)
	i = 0
	while True:
		if shelf > books[i]:
			shelf -= books[i]
			books.remove(books[i])
			total_books -= 1
		else:
			i += 1

		if i >= total_books:
			break

if len(books) == 0:
	print("\tShelves Used: " + str(total_shelves))
else:
	print("\timpossible")
