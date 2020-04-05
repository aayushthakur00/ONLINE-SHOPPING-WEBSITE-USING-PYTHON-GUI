from tkinter import*
import random
from tkinter import messagebox


def new():
        
        import sqlite3
        import os
        import random
        window=Tk()
        window.geometry("600x300")
        window.configure(bg="pink")




        def login():
                
                def login_database():
                        conn=sqlite3.connect("1.db")
                        cur=conn.cursor()
                        cur.execute("SELECT * FROM test WHERE email=? AND password=?",(e1.get(),e2.get()))
                        row=cur.fetchall()
                        conn.close()
                        print(row)
                        if row!=[]:
                                user_name=row[0][1]
                                l3.config(text="user name found with name: "+user_name)
                                window.destroy()
                                login_window.destroy()
                                
						
                        else:
                                l3.config(text="user not found ")

                

	
                login_window=Tk()
                login_window.geometry("500x450")
                login_window.configure(bg="light green")
                l1=Label(login_window,text="EMAIL",font=('Times', 16, 'bold'),bg="light green")
                l1.place(x=10,y=50)
                l2=Label(login_window,text="PASSWORD",font=('Times', 16, 'bold'),bg="light green")
                l2.place(x=10,y=100)
                l3=Label(login_window,font=('Times', 16, 'bold'),bg="light green")
                l3.place(x=50,y=300)

                email_text=StringVar()
                e1=Entry(login_window,textvariable=email_text,font=('Times', 16, 'bold'),bg="light green")
                e1.place(x=200,y=50)
                password_text=StringVar()
                e2=Entry(login_window,textvariable=password_text,font=('Times', 16, 'bold'),bg="light green")
                e2.place(x=200,y=100)


                b1=Button(login_window,text="login",width=20,font=('Times', 16, 'bold'),bg="goldenrod",command=login_database)
                b1.place(x=100,y=200)
                login_window.mainloop()




        def signup():


                def signup_database():
                        conn=sqlite3.connect("1.db")
                        cur=conn.cursor()
                        cur.execute("CREATE TABLE IF NOT EXISTS test(id INTEGER PRIMARY KEY,name text,email text, password text)")
                        cur.execute("INSERT INTO test Values(Null,?,?,?)",(e1.get(),e2.get(),e3.get()))
                        l4=Label(signup_window,text="account created",font="times 15")
                        l4.grid(row=6,column=2)
                        conn.commit()
                        conn.close()





	
                signup_window=Tk()
                signup_window.geometry("600x400")
                signup_window.configure(bg="light green")
                l1=Label(signup_window,text="USE NAME",font="times 25",bg="light green")
                l1.grid(row=1,column=1)
                l2=Label(signup_window,text="USER EMAIL",font="times 25",bg="light green")
                l2.grid(row=2,column=1)
                l3=Label(signup_window,text="USER PASSWORD",font="times 25",bg="light green")
                l3.grid(row=3,column=1)


                name_text=StringVar()
                e1=Entry(signup_window,textvariable=name_text,font=('Times', 16, 'bold'))
                e1.grid(row=1,column=2)
                email_text=StringVar()
                e2=Entry(signup_window,textvariable=email_text,font=('Times', 16, 'bold'))
                e2.grid(row=2,column=2)
                password_text=StringVar()
                e3=Entry(signup_window,textvariable=password_text,font=('Times', 16, 'bold'))
                e3.grid(row=3,column=2)

                b1=Button(signup_window,text="login",width=20,font=('Times', 16, 'bold'),bg="goldenrod",command=signup_database)
                b1.grid(row=4,column=1)
                window.mainloop()

        def contact():
        	root = Tk()
        	root.geometry("500x400")
        	root.resizable(0,0)
        	h1 = Label(root,text = "Contact Us",fg="blue",font=('arial', 30,"bold"),bd=15).pack(side= TOP)
        	h1 = Label(root,text = "Name:",fg="black",font=('arial', 20,"bold"),bd=15).place(x=130,y=130,anchor=CENTER)
        	h2 = Label(root,text = "Ayush",fg="goldenrod",font=('arial', 20,"bold"),bd=15).place(x=240,y=130,anchor=CENTER)
        	h2 = Label(root,text = "Mobile No:",fg="black",font=('arial', 20,"bold"),bd=15).place(x=130,y=190,anchor=CENTER)
        	h3 = Label(root,text = "4568424742",fg="goldenrod",font=('arial', 20,"bold"),bd=15).place(x=290,y=190,anchor=CENTER)
        	h3 = Label(root,text = "Email:",fg="black",font=('arial', 20,"bold"),bd=15).place(x=70,y=250,anchor=CENTER)
        	h4 = Label(root,text = "starcdeveloper@gmail.com",fg="goldenrod",font=('arial', 20,"bold"),bd=15).place(x=310,y=250,anchor=CENTER)
        	root.mainloop()






        l1=Label(window,text="Online Shoppping Store",font="times 30")
        l1.grid(row=1,column=2,columnspan=2)

        b1=Button(window,text="LOGIN",width=20,font=('Times', 16, 'bold'),command=login,bg="goldenrod")
        b1.grid(row=5,column=2)

        b2=Button(window,text="SIGNUP",width=20,font=('Times', 16, 'bold'),command=signup,bg="goldenrod")
        b2.grid(row=5,column=3)
        b3=Button(window,text="Contact us",width=20,font=('Times', 16, 'bold'),command=contact,bg="goldenrod")
        b3.grid(row=6,column=2)
        b4=Button(window,text="EXIT",width=20,font=('Times', 16, 'bold'),command=window.destroy,bg="goldenrod")
        b4.grid(row=6,column=3)



        window.mainloop()






        
new()
root=Tk()
root.geometry("1600x8000")
root.title("Online Shopping")
root.configure(bg='light green')
Tops=Frame(root, width=1600)
Tops.pack()

f1=Frame(root,width=800,height=700,relief=SUNKEN,bg="light green")
f1.pack()



lblInfo=Label(Tops,font=('Times',50,'bold'),text="Online Shopping Store",fg="Black",bg="bisque2",bd=15,anchor='w')
lblInfo.grid(row=0,column=0)




  

def Ref():
    x=random.randint(10908,500876)
    randomRef=str(x)
    rand.set(randomRef)
    print(x)

    if (Fries.get()==""):
        CoFries=0
    else:
        CoFries=float(Fries.get())


    
    if (Noodles.get()==""):
        CoNoodles=0
    else:
        CoNoodles=float(Noodles.get())



    if (Soup.get()==""):
        CoSoup=0
    else:
        CoSoup=float(Soup.get())



    if (Burger.get()==""):
        CoBurger=0
    else:
        CoBurger=float(Burger.get())

        
    if (Sandwich.get()==""):
        CoSandwich=0
    else:
        CoSandwich=float(Sandwich.get())

     

        
    if (Pizza.get()==""):
        CoPizza=0
    else:
        CoPizza=float(Pizza.get())
        
    if (Drinks.get()==""):
        CoD=0
    else:
        CoD=float(Drinks.get())

    if (Coffee.get()==""):
        CoCoffee=0
    else:
        CoCoffee=float(Coffee.get())

    if (Donut.get()==""):
        CoDonut=0
    else:
        CoDonut=float(Donut.get())

    if (Popcorn.get()==""):
        CoPopcorn=0
    else:
        CoPopcorn=float(Popcorn.get())

    if (Fajitas.get()==""):
        CoFajitas=0
    else:
        CoFajitas=float(Fajitas.get())

    if (Dumplings.get()==""):
        CoDumplings=0
    else:
        CoDumplings=float(Dumplings.get())

    if (Pasta.get()==""):
        CoPasta=0
    else:
        CoPasta=float(Pasta.get())

    if (Hot_Dog.get()==""):
        CoHotDog=0
    else:
        CoHotDog=float(Hot_Dog.get())

    if (Ice_Cream.get()==""):
        CoIceCream=0
    else:
        CoIceCream=float(Ice_Cream.get())

                   
    CostofFries =CoFries * 13999
    CostofDrinks=CoD * 7999
    CostofNoodles = CoNoodles* 23999
    CostofSoup = CoSoup * 14999
    CostBurger = CoBurger* 17999
    CostSandwich=CoSandwich * 61900
    CostofPizza=CoPizza*5999
    CostofCoffee=CoCoffee*13990
    CostofDonut=CoDonut*14999
    CostofPopcorn=CoPopcorn*34999
    CostofFajitas=CoFajitas*99999
    CostofDumplings=CoDumplings*16990
    CostofPasta=CoPasta*5499
    CostofHotDog=CoHotDog*21999
    CostofIceCream=CoIceCream*7999



    CostofMeal= "Rs", str('%.2f' % (CostofFries+CostofDrinks+CostofNoodles+CostofSoup+CostBurger+CostSandwich+CostofPizza+CostofCoffee+CostofDonut+CostofPopcorn+CostofFajitas+CostofDumplings+CostofPasta+CostofHotDog+CostofIceCream))

    PayTax=((CostofFries+CostofDrinks+CostofNoodles+CostofSoup+CostBurger+CostSandwich+CostofPizza+CostofCoffee+CostofDonut+CostofPopcorn+CostofFajitas+CostofDumplings+CostofPasta+CostofHotDog+CostofIceCream) * 0.05)

    TotalCost=(CostofFries+CostofDrinks+CostofNoodles+CostofSoup+CostBurger+CostSandwich+CostofPizza+CostofCoffee+CostofDonut+CostofPopcorn+CostofFajitas+CostofDumplings+CostofPasta+CostofHotDog+CostofIceCream)
 
    

   

    OverAllCost ="Rs", str ('%.2f' % (PayTax+TotalCost))

    PaidTax= "Rs", str ('%.2f' % PayTax)

    
    Cost.set(CostofMeal)
    Tax.set(PaidTax)
    Total.set(OverAllCost)

    
    
def qExit():
    root.destroy()

def Reset():
    rand.set("") 
    Fries.set("")
    Noodles.set("")
    Soup.set("")
    
    Total.set("")
    Drinks.set("")
    Tax.set("")
    Cost.set("")
    Burger.set("")
    Sandwich.set("")
    Pizza.set("")
    Coffee.set("")
    Donut.set("")
    Popcorn.set("")
    Fajitas.set("")
    Dumplings.set("")
    Pasta.set("")
    Hot_Dog.set("")
    Ice_Cream.set("")
    
    


rand = StringVar()
Fries=StringVar()
Noodles=StringVar()
Soup=StringVar()
Total=StringVar()
Drinks=StringVar()
Tax=StringVar()
Cost=StringVar()
Burger=StringVar()
Sandwich=StringVar()
Pizza=StringVar()
Coffee=StringVar()
Donut=StringVar()
Popcorn=StringVar()
Fajitas=StringVar()
Dumplings=StringVar()
Pasta=StringVar()
Hot_Dog=StringVar()
Ice_Cream=StringVar()

import sqlite3
def database():
    n1=rand.get()
    n2=Fries.get()
    n3=Noodles.get()
    n4=Soup.get()
    n5=Drinks.get()
    n6=Burger.get()
    n7=Sandwich.get()
    n8=Pizza.get()
    n9=Coffee.get()
    n10=Donut.get()
    n11=Popcorn.get()
    n12=Fajitas.get()
    n13=Dumplings.get()
    n14=Pasta.get()
    n15=Hot_Dog.get()
    n16=Ice_Cream.get()
    conn=sqlite3.connect("re2.db")
    #conn.execute("create table Lis(rand varchar(50), Fries varchar(50), Noodles  varchar(50), Soup varchar(50), Drinks  varchar(50),Burger  varchar(50),Sandwich  varchar(50),Pizza varchar(50),Coffee varchar(50),Donut varchar(50),Popcorn varchar(50),Fajitas varchar(50),Dumplings varchar(50),Pasta varchar(50),Hot_Dog varchar(50),Ice_Cream varchar(50));")
    conn.execute("insert into Lis(rand,Fries,Noodles,Soup,Drinks,Burger,Sandwich,Pizza,Coffee,Donut,Popcorn,Fajitas,Dumplings,Pasta,Hot_Dog,Ice_Cream)values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12,n13,n14,n15,n16,))
    c=conn.execute("select * from Lis ")
    for i in c:
                print("n1",i[0])
                print("n2",i[1])
                print("n3",i[2])
                print("n4",i[3])
                print("n5",i[4])
                print("n6",i[5])
                print("n7",i[6])
                print("n8",i[7])
                print("n9",i[8])
                print("n10",i[9])
                print("n11",i[10])
                print("n12",i[11])
                print("n13",i[12])
                print("n14",i[13])
                print("n15",i[14])
                print("n16",i[15])
                conn.commit()

    

def wish():
    def qui():
            allwin.destroy()
    allwin=Tk()
    allwin.title("CART")
    allwin.geometry("1000x550")
    allwin.configure(bg='light green')
    Label(allwin,text="PAYMENT",bg="light green",font=('Times', 40, 'bold')).place(x=200,y=0)
    t = Text(allwin)
    conn=sqlite3.connect("re2.db")
    for i in conn.execute('SELECT * FROM Lis'):
        t.insert(INSERT, i)
        t.insert(INSERT,'\n')

    t.pack()
    Button(allwin,padx=16,pady=8,bd=16,fg="black",font=('Times',16,'bold'),width=10,text="PAY",bg="goldenrod",command=paymnt).place(x=280,y=430)
    Button(allwin,padx=16,pady=8,bd=16,fg="black",font=('Times',16,'bold'),width=10,text="EXIT",bg="goldenrod",command=qui).place(x=600,y=430)
    
def paymnt():
        window=Tk()
        window.geometry("1100x800")
        window.configure(bg='light green')
        def exi():
                window.destroy()
        def pay():
                messagebox.showinfo("PAYMENT", "Payment Successfull")
                window.destroy()

        
                
        Label(window,text="PAYMENT",bg="light green",font=('Times', 40, 'bold')).place(x=200,y=0)
        Label(window, font=('Times', 16, 'bold'),text="NAME",bd=16,bg="light green",anchor="w").place(x=0,y=100)
        
        Entry(window, font=('Times',10,'bold'),bd=10,insertwidth=2,bg="cyan",justify='right').place(x=250,y=100)
       

        Label(window, font=('Times', 16, 'bold'),text="ADDRESS",bd=16,bg="light green",anchor="w").place(x=0,y=200)
        
        Entry(window, font=('Times',10,'bold'),bd=10,insertwidth=2,bg="cyan",justify='right').place(x=250,y=200)
        


        Label(window, font=('Times', 16, 'bold'),text="MOBILE NUMBER",bd=16,bg="light green",anchor="w").place(x=0,y=300)
        
        Entry(window, font=('Times',10,'bold'),bd=10,insertwidth=2,bg="cyan",justify='right').place(x=250,y=300)
        Label(window, font=('Times', 16, 'bold'),text="UPI ID",bd=16,bg="light green",anchor="w").place(x=0,y=400)
        
        Entry(window, font=('Times',10,'bold'),bd=10,insertwidth=2,bg="cyan",justify='right').place(x=250,y=400)
        Button(window,padx=16,pady=8,bd=16,fg="black",font=('Times',16,'bold'),width=10,text="PAY",bg="goldenrod",command=pay).place(x=500,y=200)
        
        Button(window,padx=16,pady=8,bd=16,fg="black",font=('Times',16,'bold'),width=10,text="EXIT",bg="goldenrod",command=exi).place(x=500,y=300)
        
        



lblReference= Label(f1, font=('Times', 16, 'bold'),text="ORDER ID",bd=16,bg="light green",anchor="w")
lblReference.grid(row=0, column=0)
txtReference=Entry(f1, font=('Times',10,'bold'),textvariable=rand,bd=10,insertwidth=2,bg="cyan",justify='right')
txtReference.grid(row=0,column=1)

lblFries= Label(f1, font=('Times', 16, 'bold'),text="Samsung M30",bd=16,bg="light green",anchor="w")
lblFries.grid(row=1, column=0)
txtFries=Entry(f1, font=('Times',10,'bold'),textvariable=Fries,bd=10,insertwidth=2,bg="cyan",justify='right')
txtFries.grid(row=1,column=1)


lblNoodles= Label(f1, font=('Times', 16, 'bold'),text="iPhone 6s",bd=16,bg="light green",anchor="w")
lblNoodles.grid(row=2, column=0)
txtNoodles=Entry(f1, font=('Times',10,'bold'),textvariable=Noodles,bd=10,insertwidth=2,bg="cyan",justify='right')
txtNoodles.grid(row=2,column=1)


lblSoup= Label(f1, font=('Times', 16, 'bold'),text="realme 5 pro",bd=16,bg="light green",anchor="w")
lblSoup.grid(row=3, column=0)
txtSoup=Entry(f1, font=('Times',10,'bold'),textvariable=Soup,bd=10,insertwidth=2,bg="cyan",justify='right')
txtSoup.grid(row=3,column=1)

lblBurger= Label(f1, font=('Times', 16, 'bold'),text="Redmi Note 10",bd=16,bg="light green",anchor="w")
lblBurger.grid(row=4, column=0)
txtBurger=Entry(f1, font=('Times',10,'bold'),textvariable=Burger,bd=10,insertwidth=2,bg="cyan",justify='right')
txtBurger.grid(row=4,column=1)

lblSandwich= Label(f1, font=('Times', 16, 'bold'),text="Samsung S10",bd=16,bg="light green",anchor="w")
lblSandwich.grid(row=5, column=0)
txtSandwich=Entry(f1, font=('Times',10,'bold'),textvariable=Sandwich,bd=10,insertwidth=2,bg="cyan",justify='right')
txtSandwich.grid(row=5,column=1)




lblDrinks= Label(f1, font=('Times', 16, 'bold'),text="Motorola E6s",bd=16,bg="light green",anchor="w")
lblDrinks.grid(row=0, column=2)
txtDrinks=Entry(f1, font=('Times',10,'bold'),textvariable=Drinks,bd=10,insertwidth=2,bg="cyan",justify='right')
txtDrinks.grid(row=0,column=3)

lblPizza= Label(f1, font=('Times', 16, 'bold'),text="realme C2",bd=16,bg="light green",anchor="w")
lblPizza.grid(row=1, column=2)
txtPizza=Entry(f1, font=('Times',10,'bold'),textvariable=Pizza,bd=10,insertwidth=2,bg="cyan",justify='right')
txtPizza.grid(row=1,column=3)

lblCoffee= Label(f1, font=('Times', 16, 'bold'),text="vivo Z1 Pro",bd=16,bg="light green",anchor="w")
lblCoffee.grid(row=2, column=2)
txtCoffee=Entry(f1, font=('Times',10,'bold'),textvariable=Coffee,bd=10,insertwidth=2,bg="cyan",justify='right')
txtCoffee.grid(row=2,column=3)

lblDonut= Label(f1, font=('Times', 16, 'bold'),text="POCO F1",bd=16,bg="light green",anchor="w")
lblDonut.grid(row=3, column=2)
txtDonut=Entry(f1, font=('Times',10,'bold'),textvariable=Donut,bd=10,insertwidth=2,bg="cyan",justify='right')
txtDonut.grid(row=3,column=3)

lblPopcorn= Label(f1, font=('Times', 16, 'bold'),text="Samsung S9",bd=16,bg="light green",anchor="w")
lblPopcorn.grid(row=4, column=2)
txtPopcorn=Entry(f1, font=('Times',10,'bold'),textvariable=Popcorn,bd=10,insertwidth=2,bg="cyan",justify='right')
txtPopcorn.grid(row=4,column=3)

lblFajitas= Label(f1, font=('Times', 16, 'bold'),text="iPhone 11 Pro",bd=16,bg="light green",anchor="w")
lblFajitas.grid(row=5, column=2)
txtFajitas=Entry(f1, font=('Times',10,'bold'),textvariable=Fajitas,bd=10,insertwidth=2,bg="cyan",justify='right')
txtFajitas.grid(row=5,column=3)





lblDumplings= Label(f1, font=('Times', 16, 'bold'),text="vivo Z1x",bd=16,bg="light green",anchor="w")
lblDumplings.grid(row=0, column=4)
txtDumplings=Entry(f1, font=('Times',10,'bold'),textvariable=Dumplings,bd=10,insertwidth=2,bg="cyan",justify='right')
txtDumplings.grid(row=0,column=5)

lblPasta= Label(f1, font=('Times', 16, 'bold'),text="Redmi 7A",bd=16,bg="light green",anchor="w")
lblPasta.grid(row=1, column=4)
txtPasta=Entry(f1, font=('Times',10,'bold'),textvariable=Pasta,bd=10,insertwidth=2,bg="cyan",justify='right')
txtPasta.grid(row=1,column=5)

lblHot_Dog= Label(f1, font=('Times', 16, 'bold'),text="Redmi k20",bd=16,bg="light green",anchor="w")
lblHot_Dog.grid(row=2, column=4)
txtHot_Dog=Entry(f1, font=('Times',10,'bold'),textvariable=Hot_Dog,bd=10,insertwidth=2,bg="cyan",justify='right')
txtHot_Dog.grid(row=2,column=5)

lblIce_Cream= Label(f1, font=('Times', 16, 'bold'),text="Honor 9i",bd=16,bg="light green",anchor="w")
lblIce_Cream.grid(row=3, column=4)
txtIce_Cream=Entry(f1, font=('arial',10,'bold'),textvariable=Ice_Cream,bd=10,insertwidth=2,bg="cyan",justify='right')
txtIce_Cream.grid(row=3,column=5)






lblCost= Label(f1, font=('Times', 16, 'bold'),text="COST OF MOBILE",bd=16,bg="light green",anchor="w")
lblCost.grid(row=6, column=0)
txtCost=Entry(f1, font=('Times',16,'bold'),textvariable=Cost,bd=10,insertwidth=2,bg="cyan",justify='right')
txtCost.grid(row=6,column=1)


lblStateTax= Label(f1, font=('Times', 16, 'bold'),text="GST",bd=16,bg="light green",anchor="w")
lblStateTax.grid(row=6, column=2)
txtStateTax=Entry(f1, font=('Times',16,'bold'),textvariable=Tax,bd=10,insertwidth=2,bg="cyan",justify='right')
txtStateTax.grid(row=6,column=3)



lblTotalCost= Label(f1, font=('Times', 16, 'bold'),text="TOTAL COST",bd=16,bg="light green",anchor="w")
lblTotalCost.grid(row=6, column=4)
txtTotalCost=Entry(f1, font=('Times',16,'bold'),textvariable=Total,bd=10,insertwidth=2,bg="cyan",justify='right')
txtTotalCost.grid(row=6,column=5)

btnTotal=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('Times',16,'bold'),width=10,text="TOTAL",bg="goldenrod",command=Ref).grid(row=9,column=0,padx=5,pady=30)
btnTally=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('Times',16,'bold'),width=10,text="ADD TO CART",bg="goldenrod",command=database).grid(row=9,column=1,padx=5,pady=30)
btnReset=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('Times',16,'bold'),width=10,text="RESET",bg="goldenrod",command=Reset).grid(row=9,column=2,padx=5,pady=30)

btnExit=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('Times',16,'bold'),width=13,text="MOVE TO CART",bg="goldenrod",command=wish).grid(row=9,column=3,padx=5,pady=30)
btnExit=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('Times',16,'bold'),width=11,text="EXIT",bg="goldenrod",command=qExit).grid(row=9,column=4,padx=5,pady=30)

root.mainloop()
