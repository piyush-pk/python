import datetime
class Library:

    def __init__(self, username, books):
        self.username = username
        self.books =books
        self.lend_books = []
        self.return_books = []
        user_file = f"{username}.txt"
        f = open(user_file,"a")
        f.write("----------------------*Program Open*----------------------\n")
        f.write("----------------------------------------------------------\n\n")
        f.write(f"At {datetime.datetime.now()}")
        f.write(f"-----------------\nInitial Books: {books}\n")
        f.close()
        print(books)
    
    def lendbook(self, bookname):
        b = str(self.books)
        if b.find(bookname) != -1:
            self.lend_books.append(bookname)
            self.books.remove(bookname)
            user_file = f"{self.username}.txt"
            f = open(user_file,"a")
            f.write(f"\nAt {datetime.datetime.now()}\n")
            f.write(f"Lend Book: {bookname}\n")
            f.write(f"Now Available Books: {self.books}\n")
            f.close()
            return print(f"{bookname} is Successfully Issued To {self.username}\n\n")
        else:
            return print(f"{bookname} is Not Available In Our Library\n\n")

    def returnbook(self, bookname):
        r = str(self.lend_books)
        if r.find(bookname) != -1:
            self.return_books.append(bookname)
            self.books.append(bookname)
            self.lend_books.remove(bookname)
            user_file = f"{self.username}.txt"
            f = open(user_file,"a")
            f.write(f"\nAt {datetime.datetime.now()}\n")
            f.write(f"Return Book: {bookname}\n")
            f.close()
            return print(f"{bookname} is Successfully Returned By {self.username}\n\n")
        else:
            return print(f"{bookname} is Not Issued {self.username} By Our Library\n\n")


    def abooks(self):
        return print(self.books,"\n\n")

    def lended(self):
        return print(self.lend_books,"\n\n")

    def all_Details(self):
        return print(f"Lended Books: {self.lend_books} \nReturn Books: {self.return_books}\n\n")

    



name = input('Enter Your Name: ')
b = input('Enter Your Books (Saprate Using ,) : ')
books = b.split(',')
user = Library(name, books)
while True:
    print('Enter Your Choice: ')
    print('1.Lend Book')
    print('2.Return Book')
    print('3.Available Books')
    print('4.Lened Books')
    print('5.All Details')
    print('6.Exit')
    try:
        n = int(input('Enter Your Choice: '))
        if n == 1:
            print('Choose Bookname: ',end=" ")
            user.abooks()
            b_n = input("Enter Bookname: ")
            user.lendbook(b_n)
        elif n == 2:
            print('Choose Bookname: ',end=" ")
            user.lended()
            r_n = input("Enter Bookname: ")
            user.returnbook(r_n)
        elif n == 3:
            user.abooks()
        
        elif n == 4:
            user.lended()
        
        elif n == 5:
            user.all_Details()
        
        elif n == 6:
            print("Thanks For Using Our Program")
            break
        else:
            print('\n! Please Enter Correct Choice\n')
    except:
        print("\n\n! ! !Please Enter An Number ! ! !\n\n")

# def program_exit(self):
user_file = f"{name}.txt"
f = open(user_file,"a")
f.write(f"\nAt {datetime.datetime.now()}\n")
f.write("----------------------*Program Exit*----------------------\n")
f.write("----------------------------------------------------------\n\n")
f.close()
exit()