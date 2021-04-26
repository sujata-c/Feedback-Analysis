

#----------------------Delete------------------------------------
from py2neo import Graph #,Node,Relationship
graph=Graph("http://localhost:11009/db/data/",user="neo4j",password="chauhan123")
#graph.delete_all()
import tkinter as tk
from tkinter import *
#import addMem
from PIL import ImageTk,Image
import os
import Dashboard

root =tk.Tk()
root.title("Library System")
#root.withdraw()
root.configure(background="silver")
root.geometry("640x640+0+0")

img=ImageTk.PhotoImage(Image.open(r"C:\Users\Ritesh\Pictures\lib2.jpg"))
panel=Label(root,image=img)
panel.pack(side="bottom",fill="both",expand="yes")
label1=tk.Label(root,text="Welcome To Library!!",fg="red",background="blue",font=("Helvetica",30)).place(x=450,y=50)

#3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333#
def addMem():
    #from PIL import ImageTk,Image
    #import os       
    
    root1=Toplevel(root)
   # addMem.main()    
    root1.title("Member Entry")
    root1.geometry("640x640+0+0")
    img=ImageTk.PhotoImage(Image.open(r"C:\Users\Ritesh\Pictures\reg1.jpg"))
    panel=Label(root1,image=img)
    panel.pack(side="bottom",fill="both",expand="yes")
    labelx=tk.Label(root1,text="Registeration!!",fg="red",background="yellow",font=("Helvetica",20)).place(x=550,y=50)


    label1=tk.Label(root1,text="Enter  Name",font=("Aerial",14,"bold"),fg="steelblue").place(x=500,y=150)
    text1=tk.Text(root1,height=1,width=10,font=("Aerial",22),fg="brown",background="light blue")
    text1.place(x=650,y=150)
    label2=tk.Label(root1,text="Enter Class/Department",font=("Aerial",14,"bold"),fg="steelblue").place(x=500,y=200)
    text2=tk.Text(root1,height=1,width=10,font=("Aerial",22),fg="brown",background="light blue")
    text2.place(x=750,y=200)
    label3=tk.Label(root1,text="Enter Email ID",font=("Aerial",14,"bold"),fg="steelblue").place(x=500,y=250)
    text3=tk.Text(root1,height=1,width=10,font=("Aerial",22),fg="brown",background="light blue")
    text3.place(x=650,y=250)
    label4=tk.Label(root1,text="Member Role",font=("Aerial",14,"bold"),fg="steelblue").place(x=500,y=300)

    option=["Please select one","Student","Professor"]
    var=tk.StringVar(root1)
    var.set(option[0])
    w=tk.OptionMenu(root1,var,*option)
    w.place(x=650,y=300)
    tk.Label(root1,text="Password",font=("Aerial",14,"bold"),fg="steelblue").place(x=500,y=350)
    text5=tk.Text(root1,height=1,width=10,font=("Aerial",22),fg="brown",background="light blue")
    text5.place(x=650,y=350)


    def create_node():
        nameVal=text1.get("1.0","end-1c")
        classVal=text2.get("1.0","end-1c")
        mailVal=text3.get("1.0","end-1c")
        roleVal = var.get()
        #print(roleVal)
        pwd=text5.get("1.0","end-1c")
        query1='''create (user:Member{name:{name},Class:{Class},email:{email},role:{role},password:{p}})'''#,libraryID:{lid}}) '''#with
        graph.run(query1,name=nameVal,Class=classVal,email=mailVal,role=roleVal,p=pwd)#,lid=lid)
        q='''match(u:Member) return ID(u)'''#.libraryID'''
        data2 = graph.run(q)
        for i in data2:
            #print(d)
            pass
        #print("added",d)
        messagebox.showinfo("Registeration Successful",i)
    def cancel():
        root1.destroy()

    tk.Button(root1,text="Add",command=create_node,font=("Aerial",10,"bold"),bg="black",fg="white",height=3,width=10).place(x=500,y=500)
    tk.Button(root1,text="Cancel",command=cancel,font=("Aerial",10,"bold"),bg="black",fg="white",height=3,width=10).place(x=650,y=500)
    tk.Button(root1,text="Home",command=cancel,font=("Aerial",10,"bold"),bg="black",fg="white",height=3,width=10).place(x=800,y=500)
    root1.mainloop()

            
#33333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333#
def login():
        root2=Toplevel(root)
        root2.title("Login")
        root2.geometry("640x640+0+0")
        img=ImageTk.PhotoImage(Image.open(r"C:\Users\Ritesh\Pictures\reg1.jpg"))
        panel=Label(root2,image=img)
        panel.pack(side="bottom",fill="both",expand="yes")
        tk.Label(root2,text="Login!!",fg="red",background="yellow",font=("Helvetica",20)).place(x=600,y=50)

        tk.Label(root2,text="Login id",font=("Aerial",14,"bold"),fg="steelblue").place(x=550,y=200)
        text1=tk.Text(root2,height=1,width=10,font=("Aerial",22),fg="brown",background="light blue")
        text1.place(x=700,y=200)
        tk.Label(root2,text="Password",font=("Aerial",14,"bold"),fg="steelblue").place(x=550,y=300)
        text2=tk.Text(root2,height=1,width=10,font=("Aerial",22),fg="brown",background="light blue")
        text2.place(x=700,y=300)
        
        def Login():
            
            id1=text1.get("1.0","end-1c")
            pw=text2.get("1.0","end-1c")
            print(pw);info=[]
            q='''match(m:Member) where Id(m)={i} and m.password={pwd} return m'''#.libraryID'''
            data2 = graph.run(q,i=int(id1),pwd=pw)
            for i in data2:
                info.append(i)
            if not info:
                messagebox.showinfo("Warning","Invalid Id or Password")
            else:
                Dashboard.main(id1)
        def cancel():
            root2.destroy()

        tk.Button(root2,text="Login",command=Login,font=("Aerial",10,"bold"),bg="black",fg="white",height=3,width=10).place(x=600,y=400)
        tk.Button(root2,text="Cancel",command=cancel,font=("Aerial",10,"bold"),bg="black",fg="white",height=3,width=10).place(x=750,y=400)
        root2.mainloop()

#33333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333#
def defaulter():
    root3=Toplevel(root)
    root3.title("Defaulters")
    root3.geometry("640x640+0+0")
    img=ImageTk.PhotoImage(Image.open(r"C:\Users\Ritesh\Pictures\book1.jpg"))
    panel=Label(root3,image=img)
    panel.pack(side="bottom",fill="both",expand="yes")
    tk.Label(root3,text="Defaulters!!",fg="red",background="yellow",font=("Helvetica",20)).place(x=600,y=50)
   
    ibooks=[]
    label1=tk.Label(root3,text="Select book for finding its defaulter list",font=("Aerial",14,"bold"),fg="steelblue").place(x=380,y=200)
    q1='''match(b:Book) 
    return b.name'''
    data1 = graph.run(q1)
    for d1 in data1:
        
        ibooks.append(d1)
          
    var1=tk.StringVar(root3)
    var1.set("Select Books ")
    
    w1=tk.OptionMenu(root3,var1,*ibooks)
    w1.place(x=750,y=200)

    def create_list():
        bname=var1.get()
        print(bname)
        q1=''' match(m:Member),(b:Book) 
        where (m)-[:Issued]->(b) and not (m)-[:Returned]->(b) and b.name={bnm}
        return m.name,Id(m)'''
        dat=graph.run(q1,bnm=bname[2:-3])
        #print(dat)
        dname=[]
        for d1 in dat:
            dname.append(d1)
            #print(dname)
        if not dname:
            dname.append("Null")
        
        tk.Label(root3,text=dname,font=("Aerial",14,"bold"),fg="steelblue").place(x=550,y=300)

    def cancel():
            root3.destroy()

    tk.Button(root3,text="Show",command=create_list,font=("Aerial",10,"bold"),bg="black",fg="white",height=3,width=10).place(x=550,y=400)
    tk.Button(root3,text="Cancel",command=cancel,font=("Aerial",10,"bold"),bg="black",fg="white",height=3,width=10).place(x=750,y=400)
    root3.mainloop()

#333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
#def mostRated():
    
#    tk.Label(root,text="",font=("Aerial",14,"bold"),fg="steelblue").place(x=50,y=150)
#33333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
def addBook():
    
    root4=Toplevel(root)
   # addMem.main()    
    root4.title("Book Entry")
    root4.geometry("640x640+0+0")
    img=ImageTk.PhotoImage(Image.open(r"C:\Users\Ritesh\Pictures\book1.jpg"))
    panel=Label(root4,image=img)
    panel.pack(side="bottom",fill="both",expand="yes")
    tk.Label(root4,text="Book Entry!!",fg="red",background="yellow",font=("Helvetica",20)).place(x=550,y=50)
    tk.Label(root4,text="Enter  Name",font=("Aerial",14,"bold"),fg="steelblue").place(x=450,y=200)
    text1=tk.Text(root4,height=1,width=10,font=("Aerial",22),fg="brown",background="light blue")
    text1.place(x=650,y=200)
    tk.Label(root4,text="Enter Subject",font=("Aerial",14,"bold"),fg="steelblue").place(x=450,y=250)
    text2=tk.Text(root4,height=1,width=10,font=("Aerial",22),fg="brown",background="light blue")
    text2.place(x=650,y=250)
    tk.Label(root4,text="Enter Genre",font=("Aerial",14,"bold"),fg="steelblue").place(x=450,y=300)
    text3=tk.Text(root4,height=1,width=10,font=("Aerial",22),fg="brown",background="light blue")
    text3.place(x=650,y=300)
    tk.Label(root4,text="Publisher",font=("Aerial",14,"bold"),fg="steelblue").place(x=450,y=350)
    text4=tk.Text(root4,height=1,width=10,font=("Aerial",22),fg="brown",background="light blue")
    text4.place(x=650,y=350)
    tk.Label(root4,text="Published Year",font=("Aerial",14,"bold"),fg="steelblue").place(x=450,y=400)
    text5=tk.Text(root4,height=1,width=10,font=("Aerial",22),fg="brown",background="light blue")
    text5.place(x=650,y=400)


    def create_node():
        nameVal=text1.get("1.0","end-1c")
        subVal=text2.get("1.0","end-1c")
        genreVal=text3.get("1.0","end-1c")
        pubVal=text4.get("1.0","end-1c") 
        pubYear=text5.get("1.0","end-1c")
        query1='''create (user:Book{name:{name},Subject:{sub},Genre:{gn},Publisher:{pub},Published_year:{py}})'''#,libraryID:{lid}}) '''#with
        graph.run(query1,name=nameVal,sub=subVal,gn=genreVal,pub=pubVal,py=pubYear)#,lid=lid)
        q='''match(u:Member) return ID(u)'''#.libraryID'''
        data2 = graph.run(q)
        for i in data2:
            #print(d)
            pass
        #print("added",d)
        messagebox.showinfo(" Book Added Successfully",i)
    def cancel():
        root4.destroy()

    tk.Button(root4,text="Add",command=create_node,font=("Aerial",10,"bold"),bg="black",fg="white",height=3,width=10).place(x=500,y=500)
    b2=tk.Button(root4,text="Cancel",command=cancel,font=("Aerial",10,"bold"),bg="black",fg="white",height=3,width=10).place(x=650,y=500)
    #b3=tk.Button(root4,text="Home",command=cancel,font=("Aerial",10,"bold"),bg="black",fg="white",height=3,width=10).place(x=750,y=500)
    root4.mainloop()
   
    
    
#33333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
tk.Button(root,text="Add Member",command=addMem,font=("Aerial",10,"bold"),bg="white",fg="black",height=3,width=10).place(x=50,y=150)
tk.Button(root,text="login",command=login,font=("Aerial",10,"bold"),bg="white",fg="black",height=3,width=10).place(x=150,y=250)
tk.Button(root,text="Defaulter List",command=defaulter,font=("Aerial",10,"bold"),bg="white",fg="black",height=3,width=10).place(x=250,y=350)
#tk.Button(root,text="Most Rated Book",command=mostRated,font=("Aerial",10,"bold"),bg="black",fg="white",height=3).place(x=450,y=150)
tk.Button(root,text="Add Book",command=addBook,font=("Aerial",10,"bold"),bg="white",fg="black",height=3,width=10).place(x=350,y=450)
def close():
    root.destroy()
b2=tk.Button(root,text="Close",command=close,font=("Aerial",10,"bold"),bg="white",fg="black",height=3,width=10).place(x=550,y=500)

root.mainloop()
