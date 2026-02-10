from models.Book import Book
from typing import TypedDict
from misc.libdb import BookDict, BookCountDict 

class Library():
    
    #FEATURES : ADD BOOK, BORROW BOOK, RETURN BOOK, DISPLAY INFO, INQUIRE BOOK AVAILABILITY

    def __init__(self):
        self.book_dict : BookDict = {}
        self.book_count_dict : BookCountDict = {}
        pass

    def add_book(self, book : Book):
        book_id : str = book.get_book_id()
        
        #Check if book is currently in the book dictionary using its unique book id
        if book_id in self.book_dict:
            #Book currently exists in dictionary, add a count
            self.book_count_dict[book_id]["max"] += 1
            self.book_count_dict[book_id]["stock"] += 1
            pass
        #If book currently does not exist in the book dictionary, add its count and record its data
        else:
            self.book_dict[book_id] = book
            
            self.book_count_dict[book_id] = {"max" : 1, "stock" : 1}
        pass
    
    def borrow_book(self, book_id : str) -> Book:
        book : Book = None 
        if book_id in self.book_dict:
            if self.book_count_dict[book_id]["stock"] > 0:
                self.book_count_dict[book_id]["stock"] -= 1
                book = self.book_dict[book_id]
        return book

    def return_book(self, book_id : str) -> bool:
        if book_id in self.book_dict:
            current_count : int = self.book_count_dict[book_id]["stock"] 
            max_count : int = self.book_count_dict[book_id]["max"]
            if (current_count + 1) <= max_count:
                self.book_count_dict[book_id]["stock"] += 1
                return True
        return False

    def display_book_info(self, book_id : str):
        if book_id in self.book_dict:
            return self.book_dict[book_id]
        pass

    def is_book_available(self, book_id : str) -> bool:
        if book_id in self.book_dict:
            book_count : int = self.book_count_dict[book_id]["stock"]
            if book_count > 0:
                return True
        return False
    
    def get_book_count(self, book_id : str) -> int:
        if book_id in self.book_count_dict:
            return self.book_count_dict[book_id]["stock"]
        return -1


    def search_book(self, query : str) -> list:
        #Normalize the query
        query = query.lower()
        #Separate into tokens
        search_tokens : list = query.split()

        results : list = []

        #Search for relevant books based on tokens 
        for search_token in search_tokens:
            for key in self.book_dict.keys():
                if search_token in key:
                    book : Book = self.book_dict[key]
                    if book in results:
                        continue
                    results.append(self.book_dict[key])
        return results
    
