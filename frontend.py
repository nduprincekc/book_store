from tkinter import *
import backend
root = Tk()

root.title('book store')
def get_selected_row(event):
    global selected_tuple
    index =list1.curselection()[0]
    selected_tuple=list1.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])
    e4.delete(0,END)
    e4.insert(END,selected_tuple[4])


def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)


def search_command():
    list1.delete(0,END)
    for row in backend.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        list1.insert(END,row)


def add_command():
    backend.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    list1.delete(0,END)
    list1.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))


def delete_command():
    backend.delete(selected_tuple[0])


def update_command():
    backend.update(selected_tuple[0],title_text.get(),author_text.get(), year_text.get(), isbn_text.get())


def close():
    sys.exit()

l1 = Label(root, text='Title')
l1.grid(row=0, column=0)

l2 = Label(root, text='Author')
l2.grid(row=0, column=2)


l3 = Label(root, text='Year')
l3.grid(row=1, column=0)

l4 = Label(root, text='ISBN')
l4.grid(row=1, column=2)

title_text = StringVar()
e1 = Entry(root,textvariable =title_text)
e1.grid(row=0,column=1)

author_text = StringVar()
e2=Entry(root,textvariable=author_text)
e2.grid(row=0,column =3)

year_text = StringVar()
e3=Entry(root,textvariable=year_text)
e3.grid(row=1,column =1)


isbn_text = StringVar()
e4=Entry(root,textvariable=isbn_text)
e4.grid(row=1,column =3)

# listbox code
list1 = Listbox(root,height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1 = Scrollbar(root)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview())
list1.bind('<<ListboxSelect>>',get_selected_row)
b1 = Button(root,text ='View All',width = 12,command=view_command)
b1.grid(row=2,column=3)

b2 = Button(root,text ='Search Entry',width = 12, command=search_command)
b2.grid(row=3,column=3)

b3 = Button(root,text ='Add Entry',width = 12, command=add_command)
b3.grid(row=4,column=3)

b4 = Button(root,text ='Update Selected',width = 12,command=update_command)
b4.grid(row=5,column=3)

b5 = Button(root,text ='Delete Selected',width = 12,command=delete_command)
b5.grid(row=6,column=3)

b6 = Button(root,text ='Close',width = 12,command=close )
b6.grid(row=7,column=3)



root.mainloop()
