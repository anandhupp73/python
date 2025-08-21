users=[]
books=[]

while(True):
      print('''
          1.Admin
          2.User
          3.exit''')
      ch=int(input("Enter your choice:"))
      if (ch==1):
            print('Welcome admin ')
            while(True):
                  print('''
                  1.Add book
                  2.Search book
                  3.Delete book
                  4.View all books
                  5.view all users
                  6.exit''')
                  ch1=int(input('Enter your choice :'))
                  if ch1==1:
                        print('Add book')
                        bookid=input("enter book id : ")
                        bookname=input("enter book name : ")
                        bookprice=int(input("enter book price : "))
                        author=input("enter author name")
                        books.append({"bookid":bookid,"bookname":bookname,"bookprice":bookprice,"author":author,"status":"available"})
                        print("book added succesfully")
                  elif ch1==2:
                        key=int(input("enter book id "))
                        for i in books:
                              if books[i][bookid]==key:
                                    print(books[i])
                              else:
                                    print("book not found")
                  elif ch1==3:
                        delete=int(input("enter book id to delete"))
                        for i in books:
                              if books[i]==delete:
                                    books.pop(i)
                              else:
                                    print("id not found to delete")
                        
                  elif ch1==6:
                        break
      elif ch==3:
            break