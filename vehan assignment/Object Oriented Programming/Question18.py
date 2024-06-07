class Book:
    def __init__(self ,author, title, pages):
        self.author = author
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"'{self.title}' by {self.author}, {self.pages} pages"
    

book1 = Book("Aravind Adiga", "The White Tiger", 586)
print(book1)