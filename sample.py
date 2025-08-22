users=[]
books=[{"bookid":101,"bookname":'Adujeevitham',"bookprice":300,"author":'Benyamin',"status":"available"}]
admin={}
while(True):
      print('''
          1.Admin
          2.User
          3.exit''')
      ch=int(input("Enter your choice : "))
      if (ch==1):
            print('''1.Admin signup
                     2.Admin login
                     3.back''')
            admin_ch=int(input("enter choise : "))
            if admin_ch==1:
                  if admin:
                        print("admin exists : ")
                  else:
                        uname=input("enter admin name : ")
                        pwd=input("enter pswd : ")
                        admin={"username":uname,"password":pwd}
                        print("admin added : ")
            elif admin_ch==2:
                  if not admin:
                        print("no admin registered : ")
                  else:
                        uname=input("enter username ")
                        pwd=input("enter password ")
                        if uname==admin["username"]and pwd==admin["password"]:
                              print("login succesfull ")
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
                                          bid=int(input("enter book id : "))
                                          for i in books:
                                                # if books[i][bookid]==key:
                                                if i['bookid']==bid:
                                                      # print(books[i])
                                                      print(i)
                                                else:
                                                      print("book not found")
                                    elif ch1==3:
                                          delete=int(input("enter book id to delete : "))
                                          for i in books:
                                                if books[i][bookid]==delete:
                                                      books.remove(i)
                                                else:
                                                      print("id not found to delete : ")
                                          
                                    elif ch1==6:
                                          break
                        elif admin_ch==3:
                              continue
      elif ch==3:
             break