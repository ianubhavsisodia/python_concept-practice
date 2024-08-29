class book:
    def __init__(self, p, name="", auth="", pub="", cp=0):
        self.title = name
        self.author = auth
        self.publisher = pub
        self.price= p
        self.copies = cp
    ## defining getter and setter method for instance variable (attributes of object)
    ## can use property() function to call get and set method by creating private variables 
    def get_title(self):
        return f"Title of the Book is {self.title}"
    def set_title(self,tit=""):
        self.title = tit
        return

    def get_author(self):
        return f"Author of the Book is {self.author}"
    def set_author(self,auth=""):
        self.author = auth
        return
    
    def get_publisher(self):
        return f"Publisher of the Book is {self.publisher}"
    def set_publisher(self,pub=""):
        self.publisher = pub
        return
    
    def get_price(self):
        return f"Price of the book : {self.price}"
    def set_price(self,p):
        self.price=p
        return
    
    def get_copies(self):
        return f"Copies of the book : {self.copies}"
    def set_copies(self,cp):
        self.copies=cp
        return
    # calculating royalty 
    def get_royalty(self):
        if self.copies<=500:
            self.royalty = self.copies*self.price*10/100
        elif self.copies<=1000:
            self.royalty=500*self.price*10/100 + (self.copies-500)*self.price*12.5/100
        else:
            self.royalty=500*self.price*10/100 + 500*self.price*12.5/100 + (self.copies-1000)
        return self.royalty
    
    # def string method to return printable string of the class
    def __str__(self):
        x = f"Title of the Book is {self.title}" +\
              f"\nAuthor of the Book is {self.author}" +\
                  f"\nPublisher of the Book is {self.publisher}" +\
                      f"\nPrice of the book : {self.price}" +\
                          f"\nCopies of the book : {self.copies}"
        return x

# creating an inherit class or sub class from parent class to add "format" attribute and to overrride the royalty method
class ebook(book):
    def __init__(self, p , name="", auth="", pub="", cp=0, form=None):
        super().__init__(p, name, auth, pub, cp)
        self.format=form
    def get_format(self):
        return f"Format in which the book is published: {self.format}"
    def set_format(self, form):
        self.format=form
        return
    def get_royalty(self):
        royalty = super().get_royalty()
        royalty = royalty-royalty*12/100
        self.royalty = royalty
        return self.royalty

##creating object by passing arguments required 

b1=book(120, "Think like a Monk!", "Jay Shetty", "Iconic", 680)
print ("Royalty earned : ", b1.get_royalty())
print("\n")
print ("Royalty after deducting GST")
e1=ebook(120, "Think like a Monk!", "Jay Shetty", "Iconic", 680, "PDF")
print ('Royalty earned' , e1.get_royalty())
print("\n")
print(b1)

# setting price and publisher and printing royalty
print("\n")
b1.set_price(130)
b1.set_publisher("Penguine")
print(b1)
print ("Royalty earned : ", b1.get_royalty())