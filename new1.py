book_borrowed={
    "ram":['c programmer','python','c'],
    "Faran":['c++','java'],
    "Pranay":['c'],
    "shreyash":[],
    "shivam":["c programmer"]
}
print(book_borrowed)

# find average
member=0
for i in book_borrowed.keys():
  member+=1
print("Total number if member:",member)

total_values=0
for value in book_borrowed.values():
  total_values += len(value)

print("Total number of values:",total_values)
average=total_values/member
print("Average number of books borrowed by a member:",average)

#most borrowed and list borrowed book
all_books=[]
for books in book_borrowed.values():
  all_books.extend(books)
print(all_books)
from collections import Counter
all_books_counter=Counter(all_books)
print(
    all_books_counter
)
max_count= max(all_books_counter.values())
min_count=min(all_books_counter.values())
most_borrowed_books=[book for book,count in all_books_counter.items() if count==max_count]
least_borrowed_books=[book for book,count in all_books_counter.items() if count==min_count]
print("Max count:",most_borrowed_books)
print("Min count:",least_borrowed_books)
print(book_borrowed.values())
memeber_zero_borrowing=[member for member,books in book_borrowed.items() if not books]
print("member that have no borrowed a book",memeber_zero_borrowing)