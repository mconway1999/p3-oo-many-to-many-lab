class Author:
    def __init__(self, name):
        self.name=name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if type(value) == str:
            self._name = value
    def contracts(self):
        return [contract for contract in Contract.all if contract.author is self]
    def books(self):
        return [contract.book for contract in Contract.all if contract.author is self]
    def sign_contract(self, book, date,royalties):
        return Contract(author= self, book=book, date=date, royalties=royalties)
    def total_royalties(self):
        return sum(contract.royalties for contract in Contract.all if contract.author is self)


class Book:
    def __init__(self, title):
        self.title=title 
    def contracts(self):
        return [contract for contract in Contract.all if contract.book is self]
    def authors(self):
        return [contract.author for contract in Contract.all if contract.book is self]


class Contract:
     all=[]
     
     @classmethod
     def contracts_by_date(cls, date):
         return [contract for contract in cls.all if contract.date == date]

     def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise ValueError("author must be an instance of Author class")
        if not isinstance(book, Book):
            raise ValueError("book must be an instance of Book class")
        if not isinstance(date, str):
            raise ValueError("date must be a string")
        if not isinstance(royalties, int):
            raise ValueError("royalties must be an integer")

        self.author=author 
        self.book=book
        self.date=date
        self.royalties=royalties
        Contract.all.append(self)
        


      