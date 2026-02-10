class Book():

    def __init__(self, title : str, author_name : str, publication_year : str):
        self.title : str = title
        self.author_name : str = author_name
        self.publication_year : str = str(publication_year)
        pass

    #Pseudo hash function
    def get_book_id(self) -> str:
        author_id : str = self.get_author_key()
        title_id : str = self.get_title_key()
        pubyear_id : str = self.get_pubyear_key()
        id : str = author_id + "_" + title_id + "_" + pubyear_id
        return id

    def get_author_key(self) -> str:
        return self.author_name.replace(" ", "").lower()
    
    def get_title_key(self) -> str:
        return self.title.replace(" ", "").lower()
    
    def get_pubyear_key(self) -> str:
        return self.publication_year.replace(" ", "").lower()
    
    def __str__(self):
        return ("Book: " + self.title + " By: " + self.author_name + " Published in: " + self.publication_year)