class Publisher:
    def __init__(self,publisher):
        self.publisher=publisher
    def display(self):
         print("publishername :",self.publisher)
class Book(Publisher):
    def __init__(self,title,author):
         self.title=title
         self.author=author
    def display(self):
         super().display()
         print("title of the book :",self.title)
         print("author of the book :",self.author)
class Python(Book):
    def __init__(self,publi,author,title,price,numb):
         self.price=price
         self.noofpages=numb
         Book.__init__(self,title,author)
         Publisher.__init__(self,publi)
    def display(self):
         super().display()
         print("price of the book:",self.price)
         print("number of pages in the book:",self.noofpages)
b1 = Python("SPD","Brain Johnes","Python Cookbook:Recipies Mastering Python",1670,1230)
b1.display()
