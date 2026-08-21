class library:
  w = print("\n`````~~WELCOME TO 'THE LIBRARY'~~`````\n")
  for w in range(0, 1):
    if w == 1:
      break
  def __init__(self, listOfBooks):
    self.listOfBooks = listOfBooks

  def availablebooks(self):
    print("\t\t --|---BOOKS AVAILABLE---|--\n")
    for books in self.listOfBooks:
      print('**' + books)
      
  def issueBooks(self,BookName):
    if BookName in self.listOfBooks:
      print('YOU HAVE BEEN ISSUED A BOOK!')
      self.listOfBooks.remove(BookName)
      return True 
    else:
      print('The Books You Want to ISSUE is not found/available or have been issued to another person! Kindly please wait until that person returns the Book\n')
      return False

  def returnBook(self,BookName):
    self.listOfBooks.append(BookName)
    print("Thanks For Returning The Book!\tPlease visit again\n\tTHANKS!")


class Student:
  def getbook(self):
    self.book = input('I want the book called: ')
    return self.book

  def returninbook(self):
    self.book = input('The book i want to return is: ')
    return self.book

if __name__ == '__main__':
    l = library(['Beloved', 'Quite', 'Emma', 'Improvement'])
    s = Student()
    while True:
        c = '''
        CHOOSE OPETIONS:
        1. See BooksList     [Press 1]
        2. Issue Book        [Press 2]
        3. Return Book       [Press 3]
        4. Quit              [Press 4]
        '''
        print(c)
        k = int(input('Enter A Number: '))
        if k == 1:
           l.availablebooks()
        elif k == 2:
           l.issueBooks(s.getbook())
        elif k == 3:
           l.returnBook(s.returninbook())
        elif k == 4:
           print('THANKS FOR VISITING THE LIBRARY! ')
           exit()
        else:
           print('Invalid Option. Enter a valid option!')
