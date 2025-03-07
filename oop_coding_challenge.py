# Challenge 1 - Book Class
"""
 Attributes: title, author, book_no, is_borrowed
 Methods:
 __init__(self, title, author, book_no): Initializes the book with the given title, author, and book_no.
 borrow(self): Marks the book as borrowed.
 return_book(self): Marks the book as returned.
 __str__(self): Returns a string representation of the book.
"""

class Book:
    """This class represent a borrowing account where a person can borrow 
    books
    Attributes: titles, authors, book_no
    Behaviours: borrow(), return_book()"""
    
    def __init__(self, title, author, book_no):
        self.title = title
        self.author = author
        self.book_no = book_no

    def __str__(self):
        return f"'{self.title}' by {self.author}"
    
    def borrow(self, is_borrowed):
        if is_borrowed == True:            
            print("You are currently borrowing a book")
        elif is_borrowed == False:
            print("You are not borrowing any book at the moment")
        else:
            print("Invalid argument")
    
    def return_book(self, is_returned):
        if is_returned == True:
             print("You have no books that need returning")
        elif is_returned == False:
            print("You haven't return your borrowed book")
        else: 
            print("Invalid argument")


# Challenge 2 - Member Class

""" Attributes: name, member_id, borrowed_books (a list of borrowed books)
    Methods:
    __init__(self, name, member_id): Initializes the member with the given name and ID.
    borrow_book(self, book): Adds the book to the member's borrowed books and marks the book as borrowed.
    return_book(self, book): Removes the book from the member's borrowed books and marks the book as returned.
    __str__(self): Returns a string representation of the member.
"""

class Member(Book): 
    """This class represent a member account where a member borrow books from the 
        library
       Attributes: name, member_id, borrowed_books
       Behaviours: borrow_book(self, book), return_books(self, book)
    """
    def __init__(self, name, member_id, borrowed_books):

        self.name = name 
        self.member_id = member_id
        self.borrowed_books = borrowed_books

    def __str__(self):
        return f"{self.name} with id: {self.member_id} is a member of the library" 


    def borrow_book(self, borrow_book):
            print(f"These books/ books are currently being borrowed by this member:")
            for book in borrow_book:
                print ( book)
            return f"Number of borrowed books: {len(borrow_book)}"
            
               

    def return_book(self, books):
        return (f"These books/ books have been returned by this member: \n Book : {books}")

# Challenge 3- Library Class

        """ Attributes: books (a list of all books), members (a list of all members)
            # Methods:
            # __init__(self): Initializes the library with empty books and members lists.
            # add_book(self, book): Adds a new book to the library.
            # register_member(self, member): Registers a new member to the library.
            # find_book(self, book_no): Finds a book by its book_no.
            # find_member(self, member_id): Finds a member by their ID.
            # borrow_book(self, member_id, book_no): Allows a member to borrow a book.
            # return_book(self, member_id, book_no): Allows a member to return a book.
            # __str__(self): Returns a string representation of the library’s current state."""


class Library(Member):
    
    """ 
    This is a library class that tracks the members and books in the    
    library system  

    """
   
    def __init__(self, name, member_id, borrowed_books, books, members):
        Member.__init__(self, name, member_id, borrowed_books)
        self.books = books
        self.members = members
    def add_book(self, book):
        return f"The book '{book}' has been added to the library system"
    def register_member(self, member):
        return f"{member} has been added as a member to the library system"
    def find_book(self, book_no):
         return f"Looking for '{book_no}' in the library system"
    def find_member(self, member_id):
        return f"Looking for member id no:'{member_id}' in the library system"
    def borrow_book(self, member_id, book_no):
        return f"The member with id no:'{member_id}' can borrow '{book_no}' book from the library"
    def return_book(self, member_id, book_no):
        return f"The member with id no:'{member_id}' has returned '{book_no}' book back to the library"


