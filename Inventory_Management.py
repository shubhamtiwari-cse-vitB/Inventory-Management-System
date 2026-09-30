# INVENTORY MANAGEMENT 
import mysql.connector
import datetime
# Creating Database
mydb=mysql.connector.connect(host="localhost",user="root",password="ilp123" )
mycur=mydb.cursor()
mycur.execute("create database if not exists himalaya")
mycur.execute("use himalaya")
mycur.execute("create table if not exists product(prod_name varchar(30),prod_no int(10),prod_instock int(10),prod_to_be_produced int(10),mrp int(10),rate int(10),mfg date,expiry date)")
mycur.execute("create table if not exists purchase(p_name varchar(30),no_of_unit int(10),_mrp_ int(10),_rate_ int(10), customer_name varchar(30))")
mycur.execute("create table if not exists invoice(p_name varchar(30),no_of_unit int(10),_mrp_ int(10),_rate_ int(10), customer_name varchar(30),amount int(10))")
mydb.commit()
mydb.close()
mycur.close()
# To DISPLAY Products
def DISPLAY():
   while True:
      print("\t\t --------------------------------------------------------------------------------------------------------------")
      print("\t\t          * * * * * Welcome TO HIMALAYA COMPANY PRIVATE LIMITED * * * * *")
      print("\t\t------------------------------------------------------------------------------------------------------------------")
      print("\t\t--------------------YOU HAVE CHOSEN THE OPTION TO display PRODUCT'S DETAILS--------------------")
      print("                                       PRESS 1 TO DISPLAY PRODUCTS INFO")
      print("                                       PRESS 2 FOR EXIT")
      choice=int(input("                       Enter Your Choice"))
      if choice==1:
         data()
      elif choice==2:
         return    # Returns to main menu
      else:
         print("                                      Error :   Invalid Choice try again....")
         conti=input("                             Press any key return to MAIN - MENU..")
# Fetching Data from Table Product         
def data():
   try:
      mydb=mysql.connector.connect(host="localhost",user="root",password="ilp123" ,database="himalaya")
      mycursor=mydb.cursor()
      mycursor.execute("use himalaya")
      mycursor.execute("select * from product")
      result=mycursor.fetchall()
      print("\t\t--NAME ;NUMBER;NO. OF UNITS IN STOCK;NO. OF UNITS ORDERED;MRP; RATE,  ; MANUFACTURE DATE, EXPIRY DATE --")
      for x in result:
         print("                     || ",x,"||")
         print("")
   except:
      print("\\\ ERROR /// UNABLE TO FETCH DATA")
# To  ADD, SHOW AND SEARCH for Products      
def ADD():
   while True:
      print("\t\t-----------------------------------------------------------------------------------------")
      print("\t\t   **** WELCOME TO HIMALAYA COMPANY PRIVATE LIMITED ***")
      print("\t\t-------------------------------------------------------------------------------------------")
      print("\t\t------------------YOU HAVE CHOSEN THE OPTION TO ADD PRODUCT'S DETAILS--------------------")
      print("                                                  1. ADD PRODUCT")
      print("                                                  2. SHOW ADDED PRODUCTS")
      print("                                                  3. SEARCH PRODUCTS")
      print("                                                  4. EXIT")
      print("\t\t------------------------------------------------------------------------------------------------------------------------")
      choice=int(input("             Enter Your Choice"))
      if choice==1:
        add() # Products Being Added
      elif choice ==2:
        show() # Showing Products
      elif choice==3:
        search() # Searching Products
      elif choice ==4:
         return # Returns to Main Menu
      else:
        print("                      Error: Invalid Choice try again......")
        conti=input("                     Press any key return to MAIN MENU..")
# To ADD Products        
def add():
   mydb=mysql.connector.connect(host="localhost",user="root", password="ilp123", database="himalaya")
   mycursor=mydb.cursor()
   prod_name=input("                      ENTER PRODUCT NAME   :")
   prod_no=int(input("                     ENTER PRODUCT NUMBER   :"))
   prod_instock=int(input("              ENTER NO. OF PRODUCTS INSTOCK   :"))  
   prod_to_be_produced=int(input("   ENTER NO. OF PRODUCTS ORDERED"))
   mrp=int(input("                             ENTER PRODUCT MRP :"))
   rate=int(input("                             ENTER PRODUCTS SELLING RATE :"))
   mfg=input("                                   ENTER PRODUCT'S DATE OF MANUFACTURE : ")
   expiry=input("                               ENTER PRODUCT'S DATE OF EXPIRY: ") 
   mycursor.execute("INSERT INTO product(prod_name,prod_no,prod_instock,prod_to_be_produced,mrp,rate,mfg,expiry)VALUES('{}',{},{},{},{},{},'{}','{}')".format(prod_name,prod_no,prod_instock,prod_to_be_produced,mrp,rate,mfg,expiry))
   mydb.commit()
   mydb.close()
   mycursor.close()
   print ("                         RECORDS ADDED")
# To SHOW Products   
def show():
   mydb=mysql.connector.connect(host="localhost",user="root", password="ilp123", database="himalaya")
   mycursor=mydb.cursor()
   mycursor.execute("select * from product")
   data=mycursor.fetchall()
   print("\t\tNAME ;NUMBER;PRODUCTS NO. OF UNITS IN STOCK; PRODUCTS ORDERED;MRP; RATE,  ; MANUFACTURE DATE, EXPIRY DATE --")
   for row in data:
      print("\t\t",row)
# To SEARCH for Products      
def search():
   mydb=mysql.connector.connect(host="localhost",user="root",password="ilp123",database="himalaya")
   mycursor=mydb.cursor()
   pno=int(input("                     ENTER PRODUCT NUMBER: "))
   mycursor.execute("select * from product where prod_no=%s"%pno)
   data=mycursor.fetchall()
   print("\t\t NAME , PRODUCT NUMBER; NO. OF UNITS IN STOCK; PRODUCTS ORDERED;MRP; RATE,MANUFACTURE DATE, EXPIRY DATE")
   print("")
   print("\t\t",data)
   mydb.commit()
   mydb.close()
   mycursor.close()
# To DELETE Products   
def DELETE():
   while True:
      print("\t\t----------------------------------------------------------------------------------------------------------------")
      print("\t\t     * * * * * Welcome TO HIMALAYA COMPANY PRIVATE LIMITED * * * * *")
      print("\t\t-------------------------------------------------------------------------------------------------------------------")
      print("\t\t --------------YOU HAVE CHOSEN THE OPTION TO DELETE PRODUCT'S DETAILS ---------------")
      print("                           SELECT ONE OF THESE OPTIONS TO DELETE PRODUCT'S DETAILS")
      print("                                           PRESS 1 USING PRODUCT NAME")
      print("                                           PRESS 2 USING PRODUCT NUMBER")
      print("                                           PRESS 3 FOR EXIT")
      choice=int(input("                         Enter Your Choice :-"))
      if choice==1:
         pn() # Products being Deleted by Product Name
      elif choice==2:
         pno() # Products being Deleted by Product No.
      elif choice==3:
         return # Returns to Main Menu
      else:
         print("                  Error: Invalid Choice try again....")
         conti-input("                 Press any key return to MAIN MENU..")
# To DELETE Products Using Product Name         
def pn():
   mydb=mysql.connector.connect(host="localhost",user="root",password="ilp123", database="himalaya")
   mycursor=mydb.cursor()
   y=input("                          ENTER PRODUCT NAME TO BE DELETED :- ")
   mycursor.execute("select * from product where prod_name = '%s'"%y)
   data=mycursor.fetchall()
   print("                       ",data)
   print("                       Is Being DELETED")
   sql=("delete from product where prod_name=%s")
   mycursor.execute(sql,(y,))
   print("                               RECORD DELETTEd")
   mydb.commit()
   mydb.close()
   mycursor.close()
# To DELETE Products Using Product No.   
def pno():
   mydb=mysql.connector .connect(host="localhost",user="root",password="ilp123",database="himalaya")
   mycursor=mydb.cursor()
   y=int(input("                                  ENTER PRODUCT NUMBER TO BE DELETED :- "))
   mycursor.execute("select * from product where prod_no = %s"%y)
   data=mycursor.fetchall()
   print("                       ",data)
   print("                       Is Being DELETED")   
   sql=("delete from product where prod_no=%s")
   mycursor.execute(sql,(y,))
   print("                                                RECORD DELETTED")
   mydb.commit()
   mydb.close()
   mycursor.close()
# To UPDATE Products   
def UPDATE():
   while True:
      print("\t\t---------------------------------------------------------------------------------------------------------------")
      print("\t\t            * * * * * Welcome TO HIMALAYA COMPANY PRIVATE LIMITED * * * * * ")
      print("\t\t--------------------------------------------------------------------------------------------------------------------")
      print("\t\t---------------------------YOU HAVE CHOSEN THE OPTION TO UPDATE PRODUCT DETAILS ---------------------")
      print("                                                  WHAT DO YOU WANT TO UPDATE")
      print("                                                         press 1 For Product Name")
      print("                                                         press 2 For Product No")
      print("                                                         press 3 For Product in Stock")
      print("                                                         press 4 For No of units Ordered")
      print("                                                         press 5 For MRP")
      print("                                                         press 6 For Selling Rate")
      print("                                                         press 7. EXIT")
      choice=int(input("                                         Enter Your Choice :- "))
      if choice==1:
         pn1() # Updating Product Name
      elif choice==2:
         pno1() # Updating Product No.
      elif choice==3:
          nof1() # Updating Product in stock
      elif choice==4:
          ntp1() # Updating No. of Units Ordered
      elif choice==5:
          pis1() # Updating MRP of a Product
      elif choice==6:
          price1() # Updating Selling rate of a Product
      elif choice==7:
         return # Returns to Main Menu
      else:
         print("                               Error: Invalid Choice try again...")
         conti=input("                     Press any key return to MAIN - MENU..")
# To UPDATE Product Name         
def pn1():
   mydb=mysql.connector.connect(host="localhost",user="root", password="ilp123", database="himalaya")
   mycursor=mydb.cursor()
   x=input("                                           ENTER PRODUCT NAME TO BE UPDATED: - ")
   mycursor.execute("select * from product where prod_name='%s'"%x)
   data=mycursor.fetchall()
   print("                                           ",data)
   y=input("                                           ENTER PRODUCT NAME TO BE UPDATED WITH:-")
   sql=("update product set prod_name=%s where prod_name=%s")
   mycursor.execute(sql,(y,x))
   mydb.commit()
   sq=("select * from product where prod_name='%s'"%(y))
   mycursor.execute(sq)
   data=mycursor.fetchall()
   print( "UPDATE DETAILS||",data,'||')
   mydb.close()
   mycursor.close()
   print("                                        RECORDS UPDATED!!!!!")
# To UPDATE Product No.   
def pno1():
   mydb=mysql.connector.connect(host="localhost",user="root",password="ilp123",database="himalaya")
   mycursor=mydb.cursor()
   x=input("                                  ENTER PRODUCT NAME WHOSE PRODUCT NUMBER IS TO BE UPDATED: -")
   mycursor.execute("select * from product where prod_name='%s'"%x)
   data=mycursor.fetchall()
   print("                                           ",data)    
   y=int(input("                                  ENTER PRODUCT NUMBER TO BE UPDATED WITH: - "))
   sql=("update product set prod_no=%s where prod_name=%s")
   mycursor.execute(sql,(y,x))
   mydb.commit()
   sq=("select * from product where prod_no=%s"%(y))
   mycursor.execute(sq)
   data=mycursor.fetchall()
   print("UPDATE DETAILS||" ,data,'||')
   mydb.close()
   mycursor.close()
   print("                                            RECORDS UPDATED!!!!")
# To UPDATE Product Avaialable in Stock   
def nof1():
   mydb=mysql.connector.connect(host="localhost", user="root", password="ilp123", database="himalaya")
   mycursor=mydb.cursor()
   x=input("            ENTER PRODUCT NAME WHOSE TOTAL INSTOCK VALUE IS TO BE UPDATED:-")
   mycursor.execute("select * from product where prod_name='%s'"%x)
   data=mycursor.fetchall()
   print("                                           ",data)
   y=input("            ENTER THE NEW INSTOCK VALUE :-")
   sql=("update product set prod_instock=%s where prod_name=%s")
   mycursor.execute(sql,(y,x))
   mydb.commit()
   sq="select * from product where prod_instock=%s"%(y)
   mycursor.execute(sq)
   data=mycursor.fetchall()
   print(' UPDATE DETAILS || ',data,'||')
   mydb.close()
   mycursor.close()
   print("                         RECORDS UPDATED!!!!")
# To UPDATE No. of UNITS ORDERED    
def ntp1():
   mydb=mysql.connector.connect(host="localhost",user="root",password="ilp123",database="himalaya")
   mycursor=mydb.cursor()
   x=input("ENTER PRODUCT NAME WHOSE NO. OF UNITS ORDERED IS TO BE UPDATED :- ")
   mycursor.execute("select * from product where prod_name='%s'"%x)
   data=mycursor.fetchall()
   print("                                           ",data)
   y=input(" ENTER THE NEW  NO. OF UNITS ORDERED TO BE UPDATED WITH:-")
   sql=("update product set prod_to_be_produced=%s where prod_name=%s")
   mycursor.execute(sql,(y,x))
   mydb.commit()
   sq="select * from product where prod_to_be_produced=%s"%(y)
   mycursor.execute(sq)
   data=mycursor.fetchall()
   print('UPDATE DETAILS||',data, '||')
   mydb.close()
   mycursor.close()
   print("                                 RECORDS UPDATED!!!!")
# To UPDATE Product's MRP   
def pis1():
   mydb=mysql.connector.connect(host="localhost",user="root",password="ilp123", database="himalaya")
   mycursor=mydb.cursor()
   x=input("                        ENTER PRODUCT NAME WHOSE MRP IS TO BE UPDATED")
   mycursor.execute("select * from product where prod_name='%s'"%x)
   data=mycursor.fetchall()
   print("                                           ",data)   
   y=input("                        ENTER THE NEW MRP OF THE PRODUCT")
   sql=("update product set mrp=%s where prod_name=%s")
   mycursor.execute(sql,(y,x))
   mydb.commit()
   sq="select * from product where mrp=%s"%(y)
   mycursor.execute(sq)
   data=mycursor.fetchall()
   print('UPDATE DETAILS || ',data,'||')
   mydb.close()
   mycursor.close()
   print("                          RECORDS UPDATED!!!!")
# To UPDATE Product's Selling Rate   
def price1():
   mydb=mysql.connector.connect(host="localhost",user="root",password="ilp123", database="himalaya")
   mycursor=mydb.cursor()
   x=input("                       ENTER PRODUCT NAME WHOSE SELLING RATE IS TO BE UPDATED :-")
   mycursor.execute("select * from product where prod_name='%s'"%x)
   data=mycursor.fetchall()
   print("                                           ",data)   
   y=int(input("                       ENTER THE NEW SELLING RATE :-") )
   sql=("update product set rate=%s where prod_name=%s")
   mycursor.execute(sql,(y,x))
   mydb.commit()
   mydb.commit()
   sq="select * from product where rate='%s'"%(y)
   mycursor.execute(sq)
   data=mycursor.fetchall()
   print('UPDATE DETAILS || ',data, '|| ')
   mydb.close()
   mycursor.close()
   print("                              RECORDS UPDATED!!!!")
# To SORT Products   
def SORT():
   while True:
      print("\t\t   * * * * * Welcome TO HIMALAYA COMPANY PRIVATE LIMITED   * * * * * ")
      print("\t\t ---------------------------------------------------------------------------------------------------------------")
      print("\t\t -------------------- YOU HAVE CHOSEN THE OPTION TO SORT PRODUCT'S RECORDS ----------------") 
      print("                                          press 1 by Product Name")
      print("                                          press 2 by Product No.")
      print("                                          press 3.by MRP")
      print("                                          press 4.to EXIT")      
      print("\t\t-----------------------------------------------------------------------------------------------------------")
      choice=int(input("                       Enter Your Choice:"))
      if choice==1:
         spn1() # Sorting by Product Name
      elif choice== 2:
         spr1() # Sorting by Product No.
      elif choice==3:
         spm1() # Sorting By Mrp
      elif choice ==4:
          return # Returns to Main Menu
      else:
         print("               Error: Invalid Choice try again....")
         conti= input("                 Press any key return to MAIN - MENU..")
# To Sort Products by Product Name         
def spn1():
   mydb =mysql.connector.connect(host="localhost", user= "root", password="ilp123", database="himalaya")
   mycursor=mydb.cursor()
   sql=("select * from product order by prod_name asc")
   mycursor.execute(sql)
   data=mycursor.fetchall()
   print("\t\t--NAME ;NUMBER;NO. OF UNITS IN STOCK;NO. OF UNITS ORDERED;MRP; RATE,  ; MANUFACTURE DATE, EXPIRY DATE --")
   for row in data:
      print("\t\t",row)
      print("")
   mydb.commit()
   mydb.close()
   mycursor.close()
# To Sort Products by Product No.   
def spr1():
   mydb=mysql.connector.connect(host= "localhost",user= "root", password="ilp123" ,database ="himalaya")
   mycursor=mydb.cursor()
   sql=("select * from product order by prod_no asc")
   mycursor.execute(sql)
   data=mycursor.fetchall()
   print("\t\t--NAME ;NUMBER;NO. OF UNITS IN STOCK;NO. OF UNITS ORDERED;MRP; RATE, MANUFACTURE DATE, EXPIRY DATE --")
   for row in data:
      print("\t\t",row)
      print("")
   mydb.commit()
# To Sort Products by Product's MRP   
def spm1():
   mydb=mysql.connector.connect(host= "localhost",user= "root", password="ilp123" ,database ="himalaya")
   mycursor=mydb.cursor()
   sql=("select * from product order by mrp asc")
   mycursor.execute(sql)
   data=mycursor.fetchall()
   print("\t\t--NAME ;NUMBER;NO. OF UNITS IN STOCK;NO. OF UNITS ORDERED;MRP; RATE,  ; MANUFACTURE DATE, EXPIRY DATE --")
   for row in data:
      print("\t\t",row)
      print("")
   mydb.commit()
# To Give ORDER for Products   
def ORDER():
   while True:
      print("\t\t------------------------------------------------------------------------------------------------------")
      print("\t\t   * * * * * WELCOME TO HIMALAYA COMPANY PRIVATE LIMITED * * * * * ")
      print("\t\t---------------------------------------------------------------------------------------------------------")
      print("                                                                          OUR PRODUCTS!")
      print(data())
      print("\t\t                                              YOU HAVE CHOSEN THE OPTION TO ORDER PRODUCT(s)")
      print("                                                                       ENTER 1. TO ORDER PRODUCT(s)")
      print("                                                                       ENTER 2. EXIT")
      choice=int(input("                                                             Select Your Choice -"))
      if choice==1:
         pur() # Ordering Products
      elif choice==2:
         return # Returns to Main Menu
      else:
         print("                      Error: Invalid Choice try again....")
         conti=input("                Press any key return to MAIN - MENU..")
# To ORDER Products         
def pur():
   mydb=mysql.connector.connect(host="localhost",user= "root", password="ilp123", database="himalaya")
   mycursor=mydb.cursor()
   x=input("ENTER PRODUCT NAME :")
   y=int(input("ENTER PRODUCT QUANTITY :"))
   z=int(input("ENTER MRP:"))
   r=int(input("ENTER PRODUCT'S RATE:"))
   a=input("ENTER YOUR COMAPNY NAME: ")
   mycursor.execute("INSERT INTO purchase(p_name, no_of_unit,_mrp_,_rate_,customer_name)values('{}',{},{},{},'{}')".format(x,y,z,r,a))
   s="update product set prod_to_be_produced=prod_to_be_produced+%s where prod_name=%s"
   mycursor.execute(s,(y,x)) # Updating units Ordered in "Product" Table
   mydb.commit()
   print("                                      ORDERED SUCCESFULLY !!!!!!!!")
   print("                                      T H A N K      Y O U !!!!")
   sq="select * from purchase where customer_name='%s'"%(a)
   mycursor.execute(sq)
   data=mycursor.fetchall()
   print(               "YOUR ORDER DETAILS||",data,' ||')
   amount = y*r
   # GENERATING INVOICE
   sq1=("INSERT INTO invoice(p_name, no_of_unit,_mrp_,_rate_,customer_name,amount)values('{}',{},{},{},'{}',{})".format(x,y,z,r,a,amount))
   mycursor.execute(sq1)
   ql="select * from invoice where customer_name='%s'"%(a)
   mycursor.execute(ql)
   d=mycursor.fetchall()
   print(                                           "P.NAME, QUANTITY, MRP, RATE, CUSTOMER NAME, AMOUNT TO BE PAID")
   print(" YOUR INVOICE", d)
   print("AMOUNT TO BE PAID :  ",amount)
   mydb.commit()
   mydb.close()
   mycursor.close()
   
while True:
# MAIN MENU :   
     print("\t\t=================================================================")
     print("\t\t       * * * * * WELCOME TO HIMALAYA WELLNESS * * * * *")
     print("\t\t                                SINCE -- 1930")    
     print("=====================================================================================")
     print("                            TODAY'S DATE   ", datetime.datetime.today())
     print("                           WE ARE OF TYPE PRIVATE")
     print("                            WE DEAL IN PRODUCTS:-")
     print("                                     CONSUMER GOODS")
     print("                                     HERBAL GOODS")
     print("                                     PERSONAL CARE")
     print("                                     CHILD CARE")
     print("===========================================================================")
     print("                                PRESS   1. TO DISPLAY PRODUCT RECORD FROM THE COMPANY'S STOCK       ")
     print("                                PRESS   2. TO ADD PRODUCT RECORD TO THE COMPANY'S STOCK                     ")
     print("                                PRESS   3. TO DELETE PRODUCT RECORD FROM THE COMPANY'S STOCK         ")
     print("                                PRESS   4. TO UPDATE PRODUCT RECORD TO THE COMPANY'S STOCK               ")
     print("                                PRESS   5. TO SORT PRODUCT RECORD FROM THE COMPANY'S STOCK              ")
     print("                                PRESS   6. TO GIVE ORDER FOR PRODUCT")
     print("                                PRESS   7. TO SEE ORDER HISTORY")
     print("                                PRESS   8. TO SEE  ORDER INVOICES ")
     print("                                PRESS   9. TO CANCEL ORDER")
     print("                                PRESS  10. TO DELETE INVOICES")
     print("                                PRESS  11. TO EXIT")
     print("\t\t=====================================================================================")
     choice=int(input("                              SELECT YOUR CHOICE:-"))
     if choice==1:
        DISPLAY() # DISPLAYING Products Info
     elif choice==2:
        ADD()        # ADDING Products
     elif choice==3:
        DELETE() # DELETING Products
     elif choice ==4:
        UPDATE() # UPDATING Products
     elif choice==5:
        SORT()      # SORTING Products
     elif choice==6:
        ORDER()   # ORDERING Products
     # Displaying ORDER HISTORY        
     elif choice==7:
           mydb=mysql.connector.connect(host="localhost", user="root", password="ilp123", database="himalaya")
           mycursor=mydb.cursor()
           mycursor.execute("select * from purchase")
           data=mycursor.fetchall()
           print("\t\t--PRODUCT NAME ;UNITS ORDERED;MRP; RATE,COMPANY NAME")
           for row in data:
              print("\t\t", row)
           mydb.commit()
           mydb.close()
           mycursor.close()
     # Displaying Generated INVOICES      
     elif choice==8:
           mydb=mysql.connector.connect(host="localhost", user="root", password="ilp123", database="himalaya")
           mycursor=mydb.cursor()
           mycursor.execute("select * from invoice")
           data=mycursor.fetchall()
           print("\t\t--PRODUCT NAME ;UNITS ORDERED;MRP; RATE,COMPANY NAME , AMOUNT TO PAY")           
           for row in data:
              print("\t\t",row)
           mydb.commit()
           mydb.close()
           mycursor.close()
     # Cancelling ORDER      
     elif choice==9:
           mydb=mysql.connector.connect(host="localhost", user="root", password="ilp123", database="himalaya")
           mycursor=mydb.cursor()
           mycursor.execute("delete from purchase")
           mydb.commit()
           print("                             ################# ORDER CANCELLED #######################")
           mydb.close()
           mycursor.close()
     # Deleting INVOICES      
     elif choice==10:
           mydb=mysql.connector.connect(host="localhost", user="root", password="ilp123", database="himalaya")
           mycursor=mydb.cursor()
           mycursor.execute("delete from invoice")
           mydb.commit()
           print("                             ######################INVOICE DELETED######################")
           mydb.close()
           mycursor.close()
     # TERMINATING PROGRAM      
     elif choice==11:
           break # Terminates Program
     else:
       print("                                          Error: Invalid Choice try again....")
       conti=input("                               Press any key return to MAIN MENU..")  
