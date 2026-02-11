from models.Library import Library
from models.Book import Book

import json

library : Library = Library()


with open('books.json', 'r') as file:
    data = json.load(file)

for datum in data:
    book : Book = Book(datum['title'], datum['author'], datum['year'])
    library.add_book(book)

book1 : Book = Book("The Most Awesome Book of All Time", "Julio Caesar R. Tadena", "2026")
book2 : Book = Book("The Most Awesome Book of All Time", "Julio Caesar R. Tadena", "2026")

library.add_book(book1)
library.add_book(book2)

def main():

    #FEATURES : ADD BOOK, BORROW BOOK, RETURN BOOK, DISPLAY INFO, INQUIRE BOOK AVAILABILITY
    


    user_input()
    
    #search_query : str = "Julio"

    #print("Search Results: ")
    #results : list = library.search_book(search_query) 
    
    #for result in results:
        #print(str(result) + " Count: " + str(library.get_book_count(result.get_book_id())))
        #print("Book Pub Year key: " + result.get_book_id())

        #if search_query in result.get_book_id():
        #    print("Search query is a substring of book id")
        #else:
        #    print("Search query is not a substring of book id")

    pass


def user_input():
    done : bool = False
    while not done:
        print("[1] Add Book")
        print("[2] Borrow Book")
        print("[3] Return Book")
        print("[4] Display Book Info")
        print("[5] Inquire Book Availability")
        print("[6] Exit")
        done = handle_input(input("Please the number of the action you want to do: "))
    pass

def handle_input(input : str) -> bool:
    match input:
        case "1":
            add_book()
            return True
        case "2":
            borrow_book()
            return True
        case "3":
            return_book()
            return True
        case "4":
            display_book_info()
            return True
        case "5":
            inquire_book_availability()
            return True
        case "6":
            return True
        case _:
            print("Invalid input, please try again")
            return True
    return False

def add_book():
    done : bool = False
    while not done:
        book_title : str = input("Enter book title: ")
        book_author : str = input("Enter book author: ")
        book_pubyear : str = input("Enter book publication year: ")
        book : Book = Book(book_title, book_author, book_pubyear)
        library.add_book(book)
        done = True
        input("Successfully added book")
        user_input()
        pass
    pass


def borrow_book():
    done : bool = False
    while not done:
        
        search_query = input("Enter book details: ")
        
        print("Please select the book you want to borrow")
        book_to_borrow : Book = handle_search_result(library.search_book(search_query))
        if library.borrow_book(book_to_borrow.get_book_id()):
            print("Successfully borrowed book.")
            input()
        else:
            print("No available copies in stock :(")
            input()
        print(book_to_borrow)
        done = True
        user_input()
        pass
    pass

def return_book():
    done : bool = False
    while not done:
        search_query = input("Enter book details: ")
        
        print("Please select the book you want to return")
        book_to_return : Book = handle_search_result(library.search_book(search_query))
        
        if library.return_book(book_to_return.get_book_id()):
            print("Successfully returned book.")
            input()
        else:
            print("The book you're trying to return does not belong in this library")
            input()
        done = True
        user_input()
        pass
    pass

def display_book_info():
    done : bool = False
    while not done:
        search_query = input("Enter book details: ")

        print("Please select the book you want to see information about...")
        book_to_display : Book = handle_search_result(library.search_book(search_query))

        print("Book Title: " + book_to_display.title)
        print("Book Author: " + book_to_display.author_name)
        print("Book Publication Year: " + book_to_display.publication_year)

        done = True
        user_input()
    pass

def inquire_book_availability():
    done : bool = False
    while not done:
        search_query = input("Enter book details: ")

        print("Please select the book you want to inquire availability")
        book_to_inquire : Book = handle_search_result(library.search_book(search_query))

        if library.is_book_available(book_to_inquire.get_book_id()):
            print("This book is available")
            input()
        else:
            print("This book is unfortunately unavailable")
            input()
        done = True
        user_input()
    pass


def handle_search_result(results : list) -> Book:
    book_id : str = ""
    for result in results:
        index_str : str = str(results.index(result) + 1)
        result_str : str = "[" + index_str + "] " + str(result) + " In stock: " + str(library.get_book_count(result.get_book_id()))
        print(result_str)
        pass
    choice : str = input()
    result_idx : int = int(choice) - 1
    return results[result_idx]



main()