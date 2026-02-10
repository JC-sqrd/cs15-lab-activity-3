from models.Book import Book
from typing import TypedDict

    
class BookCountDict(TypedDict):
    book_id : str
    count : dict = {"max" : 0, "stock" : 0}

class BookDict(TypedDict):
    book_id : str
    book : Book

