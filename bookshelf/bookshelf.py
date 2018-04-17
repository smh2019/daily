#!/usr/bin/python3

print("Bookshelf problem")

path = 'challenge_input'
ci = open(path,'r')
line = ci.readline()

# Sort bookshelves from largest to smallest
shelves = line.split()
shelves = [int(x) for x in shelves]
shelves.sort()
shelves.reverse()

#print("Shelves")
# Print sorted shelves
#for shelf in shelves:
	#print(shelf)

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
#print("Books")
#for book in books:
	#print(book)

ci.close()

print("Shelves: " + str(len(shelves)))
print("Books: " + str(len(books)))
# How many Shelves
total_shelves = 0

c = 0
for shelf in shelves:
	print("books: " + str(len(books)))
	print("shelf: " + str(shelf))
	if len(books) <= 0:
		break
	total_shelves += 1

	total_books = len(books)
	i = 0
	while True:
		print("i:" + str(i))
		print("tb:" + str(total_books))
		if shelf < books[i]:
			shelf -= books[i]
			books.remove(books[i])
			total_books -= 1
		else:
			i += 1

		if i < total_books:
			break


#for shelf in shelves:
#	if len(books) <= 0:
#		break
#	if len(shelves) <= 0:
#		impossible = 1
#		break
#	total_shelves += 1
#
#	while shelf > 0:
#		for i in range(0,len(books)):
#			if books[i] < shelf:
#				shelf -= book
#				books.remove(book)
#				break
#		shelves.remove(shelf)
#		break

if len(books) == 0:
	print("Shelves Used: " + str(total_shelves))
else:
	print("impossible")
