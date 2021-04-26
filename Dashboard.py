from py2neo import Graph #,Node,Relationship
graph=Graph("http://localhost:11009/db/data/",user="neo4j",password="chauhan123")
#graph.delete_all()
import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image
import os

def main(lid):
    root=tk.Tk()
    root.title("User Dashboard")
    root.geometry("640x640+0+0")
    root.configure(background="lightblue")
    tk.Label(root,text="User ID",font=("Aerial",14,"bold"),fg="steelblue").place(x=900,y=10)

    tk.Label(root,text=lid,font=("Aerial",14,"bold"),fg="steelblue").place(x=1000,y=10)
#33333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
    def issueBook():
            root2=Toplevel(root)
            root2.title("Book Issue")
            root2.geometry("640x640+0+0")
            root2.configure(background="lightblue")

            #img=ImageTk.PhotoImage(Image.open(r"C:\Users\Ritesh\Pictures\book3.jpg"))
            #panel=Label(root2,image=img)
           # panel.pack(side="bottom",fill="both",expand="yes")

            tk.Label(root2,text="select book",font=("Aerial",14,"bold"),fg="blue").place(x=200,y=150)
            books=[]
            q1='''match(u:Book) return u.name'''
            data1 = graph.run(q1)
            print(type(data1))
            for d in data1:
                #print(type(d))
                books.append(d)
            print(books)
            '''for i in range(len(books)):
               # books[i]=Variable()
                l=Checkbutton(root2,text=books[i],variable=books[i])
                l.pack()'''
            var1=tk.StringVar(root2)
            var1.set("Select Books")
            w1=tk.OptionMenu(root2,var1,*books)
            w1.place(x=400,y=150)
            
            #tk.Label(root2,text=lid,font=("Aerial",14,"bold"),fg="steelblue").place(x=500,y=50)
            #libID=[]
            #q2='''match(m:Member) return id(m)'''#.libraryID'''
           #data2 = graph.run(q2)
            #for d in data2:
             #   libID.append(d)
              #  print(libID)
          #  var2=tk.StringVar(root2)
           # var2.set(libID[0])
            #w2=tk.OptionMenu(root2,var2,*libID)
            #w2.place(x=700,y=50)
            
            tk.Label(root2,text="Enter Date ",font=("Aerial",14,"bold"),fg="blue").place(x=200,y=300)
            text3=tk.Text(root2,height=1,width=10,font=("Aerial",22),fg="brown",background="light blue")
            text3.place(x=500,y=300)
            #label4=tk.Label(root2,text="Enter Return Date(dd/mm/yy)",font=("Aerial",14,"bold"),fg="steelblue").place(x=10,y=200)
            #text4=tk.Text(root2,height=1,width=10,font=("Aerial",22),fg="brown",background="light blue")
            #text4.place(x=300,y=200)
        
            def create_relation1():
                #lid = var2.get()
                bname = var1.get()    
                issueDate=text3.get("1.0","end-1c")
                #returnDate=text4.get("1.0","end-1c")
                #bname="World Book Encyclopedia"
                #print(bname)
                #bname[1:];bname[:-1]
                print(bname[2:-3])
                #lid1='26'
                q1='''match(m:Member),(b:Book)
                where ID(m)={i} and b.name={b}
                create (m)-[r:Issued{date:{idate}}]->(b)
                return type(r)'''
                data1 = graph.run(q1,i=int(lid),b=bname[2:-3],idate=issueDate)
                for x in data1:
                    #print(x)
                    pass
                messagebox.showinfo(" Successful",x)
            def create_relation2():
                bname = var1.get()    
                issueDate=text3.get("1.0","end-1c")
                q1='''match(m:Member),(b:Book)
                where ID(m)={i} and b.name={b}
                create (m)-[r:Wrote{issue_date:{idate}}]->(b)
                return type(r)'''
                data1 = graph.run(q1,i=int(lid),b=bname[2:-3],idate=issueDate)
                for x in data1:
                    pass
                messagebox.showinfo(" Successful",x)
            def create_relation3():
                bname = var1.get()    
                issueDate=text3.get("1.0","end-1c")
                q1='''match(m:Member),(b:Book)
                where ID(m)={i} and b.name={b}
                create (m)-[r:Recommended{issue_date:{idate}}]->(b)
                return type(r)'''
                data1 = graph.run(q1,i=int(lid),b=bname[2:-3],idate=issueDate)
                for x in data1:
                    pass
                messagebox.showinfo(" Successful",x)
            def create_relation4():
                bname = var1.get()    
                issueDate=text3.get("1.0","end-1c")
                q1='''match(m:Member),(b:Book)
                where ID(m)={i} and b.name={b}
                create (m)-[r:Translated{issue_date:{idate}}]->(b)
                return type(r)'''
                data1 = graph.run(q1,i=int(lid),b=bname[2:-3],idate=issueDate)
                for x in data1:
                    pass
                messagebox.showinfo(" Successful",x)
            
            
            def cancel():
                root2.destroy()

            tk.Button(root2,text="Issue",command=create_relation1,font=("Aerial",10,"bold"),bg="black",fg="white",height=3,width=10).place(x=400,y=400)
            tk.Button(root2,text="Write",command=create_relation2,font=("Aerial",10,"bold"),bg="black",fg="white",height=3,width=10).place(x=500,y=400)
            tk.Button(root2,text="Recommend",command=create_relation3,font=("Aerial",10,"bold"),bg="black",fg="white",height=3,width=10).place(x=600,y=400)
            tk.Button(root2,text="Translate",command=create_relation4,font=("Aerial",10,"bold"),bg="black",fg="white",height=3,width=10).place(x=700,y=400)

            tk.Button(root2,text="Cancel",command=cancel,font=("Aerial",10,"bold"),bg="black",fg="white",height=3,width=10).place(x=800,y=400)
            root2.mainloop()
#33333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333#
    def returnBook():
            root1=Toplevel(root)
            root1.title("Book Return")
            root1.geometry("640x640+0+0")
            label1=tk.Label(root1,text="Issued books which are not yet Returned by the member",font=("Aerial",14,"bold"),fg="steelblue").place(x=200,y=150)
            rbooks=[]
            q1='''match(m:Member),(b:Book) 
            where (m)-[:Issued]->(b) and not (m)-[:Returned]->(b) and ID(m)={i}
            return b.name'''
            data1 = graph.run(q1,i=int(lid))
            print(type(data1))
            for d in data1:
                rbooks.append(d)
            
            var1=tk.StringVar(root1)
            var1.set("Select Books To Return")
            w1=tk.OptionMenu(root1,var1,*rbooks)
            w1.place(x=450,y=200)
            def cancel():
                root1.destroy()
            def create_relation1():
                bname = var1.get()    
                q1='''match(m:Member),(b:Book)
                where ID(m)={i} and b.name={b}
                create (m)-[r:Returned]->(b)
                return type(r)'''
                data1 = graph.run(q1,i=int(lid),b=bname[2:-3])
                for x in data1:
                    pass
                messagebox.showinfo(" Successful",x)
            tk.Label(root1,text="User Id",font=("Aerial",14,"bold"),fg="steelblue").place(x=900,y=20)
            tk.Label(root1,text=lid,font=("Aerial",14,"bold"),fg="steelblue").place(x=1000,y=20)
            tk.Button(root1,text="Return",command=create_relation1,font=("Aerial",10,"bold"),bg="black",fg="white",height=3,width=10).place(x=550,y=400)
            tk.Button(root1,text="Cancel",command=cancel,font=("Aerial",10,"bold"),bg="black",fg="white",height=3,width=10).place(x=650,y=400)
            
#33333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
    def rateBook():
        root3=Toplevel(root)
        root3.title("Book Rating")
        root3.geometry("640x640+0+0")
        ibooks=[]
        r1books=[]
        tk.Label(root3,text="Books that you have read  ",font=("Aerial",14,"bold"),fg="steelblue").place(x=50,y=50)
        tk.Label(root3,text="Books that you have rated  ",font=("Aerial",14,"bold"),fg="steelblue").place(x=400,y=50)

        q1='''match(m:Member),(b:Book) 
            where (m)-[:Issued]->(b)  and
            not (m)-[:Rated]->(b) and ID(m)={i}
            return b.name'''
        data1 = graph.run(q1,i=int(lid))
        for d1 in data1:
                ibooks.append(d1)
          
        var1=tk.StringVar(root3)
        var1.set("Select Books To Rate")
        w1=tk.OptionMenu(root3,var1,*ibooks)
        w1.place(x=50,y=100)
        q2='''match(m:Member),(b:Book) 
        where (m)-[:Rated]->(b)  and ID(m)={i}
            return b.name'''
        data2= graph.run(q2,i=int(lid))
        for d2 in data2:
                r1books.append(d2)
        #print("hhhhhhhhhhhhhhhhhh",r1books)
  
        var2=tk.StringVar(root3)
        var2.set("Select Books To Rate")
        if not r1books:
            r1books.append("Null")
        w2=tk.OptionMenu(root3,var2,*r1books)
        w2.place(x=200,y=100)
       
        
        tk.Label(root3,text="Ratings: ",font=("Aerial",14,"bold"),fg="steelblue").place(x=10,y=200)
        option=["Ratings","0","1","2","3","4","5"]
        var=tk.StringVar(root3)
        var.set(option[0])
        w=tk.OptionMenu(root3,var,*option)
        w.place(x=100,y=200)
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        def cancel():
                root3.destroy()
        def create_relation1():
            bname=var1.get()
            rate = var.get()    
            q1='''match(m:Member),(b:Book)
            where ID(m)={i} and b.name={b}
            create (m)-[r:Rated{rates:{r1}}]->(b)
            return type(r)'''
            data1 = graph.run(q1,i=int(lid),r1=rate,b=bname[2:-3])
            for x in data1:
                pass
            messagebox.showinfo(" Successful",x)
        def create_relation2():
            bnm=var2.get()
            rate=var.get()
            q1='''match(m:Member),(b:Book) 
                match (m)-[r:Rated]-(b)  where ID(m)={i} and b.name={b}
                set r.rates={rt}'''
            data1 = graph.run(q1,i=int(lid),rt=rate,b=bnm[2:-3])
            for x in data1:
                pass
            messagebox.showinfo(" Successful","Rating Updated")
         #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
         

        #tk.Label(root3,text=lid,font=("Aerial",14,"bold"),fg="steelblue").place(x=600,y=50)
        tk.Button(root3,text="Rate",command=create_relation1,font=("Aerial",10,"bold"),bg="black",fg="white",height=3,width=10).place(x=500,y=400)
        tk.Button(root3,text=" Update Rate",command=create_relation2,font=("Aerial",10,"bold"),bg="black",fg="white",height=3,width=10).place(x=600,y=400)
        tk.Button(root3,text="Cancel",command=cancel,font=("Aerial",10,"bold"),bg="black",fg="white",height=3,width=10).place(x=700,y=400)
        
#3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
    def findFriends():
        root4=Toplevel(root)
        root4.title("Find Friends")
        root4.geometry("640x640+0+0")
        rFriends=[]
        sFriends=[]
        tk.Label(root4,text="Find Random Friends  ",font=("Aerial",14,"bold"),fg="steelblue").place(x=10,y=50)
        tk.Label(root4,text="Find Friends with same taste of books ",font=("Aerial",14,"bold"),fg="steelblue").place(x=300,y=50)

        q1='''match(m:Member) where id(m) <>{i}
            return m.name'''
        data1 = graph.run(q1,i=int(lid))
        for d1 in data1:
                rFriends.append(d1)
          
        var1=tk.StringVar(root4)
        var1.set("Select Friend")
        w1=tk.OptionMenu(root4,var1,*rFriends)
        w1.place(x=20,y=100)
        q2='''match(m:Member),(b:Book)where (m)-[:Issued]->(b) and  Id(m)={i} 
        with b  match(m1:Member)-[:Issued]->(b) where Id(m1)<>{i1}
        return  m1.name '''
        data2=graph.run(q2,i=int(lid),i1=int(lid))
        for d2 in data2:
            sFriends.append(d2)
        var2=tk.StringVar(root4)
        var2.set("Select Friend")
        if not sFriends:
            sFriends.append('Null')
        w2=tk.OptionMenu(root4,var2,*sFriends)
        w2.place(x=360,y=100)
        
        def cancel():
                root4.destroy()
        def create_relation1():
            rfrnd=var1.get()
            
            q1='''match(m1:Member),(m2:Member)
            where ID(m1)={i} and m2.name={nm}
            create (m1)-[r:Following]->(m2) 
            return type(r)'''
            data1 = graph.run(q1,i=int(lid),nm=rfrnd[2:-3])
            for x in data1:
                pass
            messagebox.showinfo(" Successful",x)
        def create_relation2():
            sfrnd=var2.get()
            
            q2='''match(m1:Member),(m2:Member)
            where ID(m1)={i} and m2.name={nm}
            create (m1)-[r:Following]->(m2) 
            return type(r)'''
            data2 = graph.run(q2,i=int(lid),nm=rfrnd[2:-3])
            for x in data2:
                pass
            messagebox.showinfo(" Successful",x)
            
        
         #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
         

        tk.Label(root4,text=lid,font=("Aerial",14,"bold"),fg="steelblue").place(x=600,y=50)
        tk.Button(root4,text="Follow",command=create_relation1,font=("Aerial",10,"bold"),bg="black",fg="white",height=3,width=10).place(x=200,y=400)
        tk.Button(root4,text=" Follow ",command=create_relation2,font=("Aerial",10,"bold"),bg="black",fg="white",height=3,width=10).place(x=400,y=400)

        tk.Button(root4,text="Cancel",command=cancel,font=("Aerial",10,"bold"),bg="black",fg="white",height=3,width=10).place(x=800,y=400)
#33333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
    def viewAccount():
        root5=Toplevel(root)
        root5.title("Your Account")
        root5.geometry("640x640+0+0")
        #rFriends=[]
        #sFriends=[]
        tk.Label(root5,text="Issued books ",font=("Aerial",14,"bold"),fg="steelblue").place(x=10,y=50)
        tk.Label(root5,text="Recommended books ",font=("Aerial",14,"bold"),fg="steelblue").place(x=10,y=100)
        tk.Label(root5,text="Rated books ",font=("Aerial",14,"bold"),fg="steelblue").place(x=10,y=150)
        tk.Label(root5,text="Following ",font=("Aerial",14,"bold"),fg="steelblue").place(x=10,y=200)
        tk.Label(root5,text="Followers ",font=("Aerial",14,"bold"),fg="steelblue").place(x=10,y=250)
        tk.Label(root5,text="Books Recommended by Following ",font=("Aerial",14,"bold"),fg="steelblue").place(x=10,y=300)
        q1='''match(m:Member),(b:Book) 
        where Id(m)={i} and (m)-[:Issued]->(b)
        return b.name'''
        q2='''match(m:Member),(b:Book) 
        where Id(m)={i} and (m)-[:Recommended]->(b)
        return b.name'''
        q3='''match(m:Member),(b:Book) 
        where Id(m)={i} and (m)-[:Rated]->(b)
        return b.name'''
        q4='''match(m1:Member),(m2:Member)
        where Id(m1)={i} and (m1)-[:Following]->(m2)
        return m2.name'''
        q5='''match(m1:Member),(m2:Member)
        where Id(m1)={i} and (m1)<-[:Following]-(m2)
        return m2.name'''
        q6='''match(m1:Member),(m2:Member),(b:Book)
        where Id(m1)={i} and (m1)-[:Following]->(m2) and (m2)-[:Recommended]->(b)
        return b.name'''
        iname=[];rbook=[];rname=[];following=[];follower=[];fbook=[]
        data1=graph.run(q1,i=int(lid))
        data2=graph.run(q2,i=int(lid))
        data3=graph.run(q3,i=int(lid))
        data4=graph.run(q4,i=int(lid))
        data5=graph.run(q5,i=int(lid))
        data6=graph.run(q6,i=int(lid))
        #print(data1)
        #print("eeeeeeeeeeeeeeeeeeeeeeeeehhhhhhhhhhhh")
        #def show():
        for d1 in data1:
            iname.append(d1)
        print(iname)
        if not iname:
            iname.append("Null")
        tk.Label(root5,text=iname,font=("Aerial",14,"bold"),fg="steelblue").place(x=200,y=50)
        
        for d2 in data2:
            rbook.append(d2)
        print(rbook)
        if not rbook:
            rbook.append("Null")
        tk.Label(root5,text=rbook,font=("Aerial",14,"bold"),fg="steelblue").place(x=300,y=100)
        
        for d3 in data3:
            rname.append(d3)
        print(rname)
        if not rname:
            rname.append("Null")
        tk.Label(root5,text=rname,font=("Aerial",14,"bold"),fg="steelblue").place(x=200,y=150)
        
        for d4 in data4:
            following.append(d4)
        print(following)
        if not following:
            following.append("Null")
        tk.Label(root5,text=following,font=("Aerial",14,"bold"),fg="steelblue").place(x=200,y=200)
        
        for d5 in data5:
            follower.append(d5)
        print(follower)
        if not follower:
            follower.append("Null")
        tk.Label(root5,text=follower,font=("Aerial",14,"bold"),fg="steelblue").place(x=200,y=250)
        
        for d6 in data6:
            fbook.append(d6)
        print(fbook)
        if not fbook:
            fbook.append("Null")
        tk.Label(root5,text=fbook,font=("Aerial",14,"bold"),fg="steelblue").place(x=300,y=300)
        #tk.Button(root5,text=" Follow ",command=show,font=("Aerial",10,"bold"),bg="black",fg="white",height=3,width=10).place(x=400,y=400)

    
#333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333   
    def logout():
        root.destroy()
        returnBook.root1.destroy()
        issueBook.root2.destroy()
        rateBook.root3.destroy()
        findFriends.root4.destroy()
        viewAccount.root5.destroy()
        
    tk.Button(root,text="Issue Books",command=issueBook,font=("Aerial",10,"bold"),bg="black",fg="white",height=3,width=10).place(x=250,y=150)
    tk.Button(root,text="Return Books",command=returnBook,font=("Aerial",10,"bold"),bg="black",fg="white",height=3,width=10).place(x=550,y=150)
    tk.Button(root,text="Rate a book",command=rateBook,font=("Aerial",10,"bold"),bg="black",fg="white",height=3,width=10).place(x=850,y=150)
    tk.Button(root,text="Find Friends",command=findFriends,font=("Aerial",10,"bold"),bg="black",fg="white",height=3,width=10).place(x=400,y=350)
    tk.Button(root,text="View Account",command=viewAccount,font=("Aerial",10,"bold"),bg="black",fg="white",height=3,width=12).place(x=700,y=350)
   # tk.Button(root,text="Suggest books to library",command=viewAccount,font=("Aerial",10,"bold"),bg="black",fg="white").place(x=300,y=300)

    tk.Button(root,text="Log out",command=logout,font=("Aerial",10,"bold"),bg="black",fg="white",height=3,width=10).place(x=550,y=550)
    