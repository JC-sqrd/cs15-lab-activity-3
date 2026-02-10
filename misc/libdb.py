from models.Book import Book
from typing import TypedDict


class AuthorDict(TypedDict):
    author : int
    books : list

class TitleDict(TypedDict):
    title : int
    books : list

class PubYearDict(TypedDict):
    publication_year : str
    books : list
    
class BookCountDict(TypedDict):
    book_id : str
    count : dict = {"max" : 0, "stock" : 0}

class BookDict(TypedDict):
    book_id : str
    book : Book

