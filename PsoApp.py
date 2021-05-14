from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter.ttk import *
import sqlite3

root = Tk()
root.title("Pro Shop Helper")
root.iconbitmap('bowling.ico')
root.geometry("1600x950")
#root.configure(bg="lightblue")

myCanvas = Canvas(root, width=1600, height=1000, bg="lightblue", borderwidth=0)
myCanvas.pack()





#create or connect to DB
conn = sqlite3.connect('bowlers.db')

#creat cursor
c = conn.cursor()

'''
#create the table
c.execute("""CREATE TABLE bowlers(
        f_name text, 
        l_name text,
        date text,
        address text,
        city text,
        state text,
        zipcode text,
        email text,
        phone text,
        handedness text,
        num_of_hands text,
        ring_reverse text,
        middle_reverse text,
        ring_out text,
        bridge_width text,
        middle_out text,
        ring_forward text,
        middle_forward text,
        ring_span text,
        middle_span text,
        thumb_forward text,
        thumb_left text,
        thumb_right text,
        thumb_reverse text,
        ball_name text,
        ball_weight text,
        serial_number text,
        grip_type text,
        thumb_style text,
        thumb_size text,
        middle_style text,
        middle_size text,
        ring_style text,
        ring_size text
)
""")
'''
def query_database():
    # Create a database or connect to one that exists
    conn = sqlite3.connect('bowlers.db')

    # Create a cursor instance
    c = conn.cursor()

    c.execute("SELECT rowid, * FROM bowlers ORDER BY l_name")
    records = c.fetchall()

    # Add our data to the screen
    global count
    count = 0

    #for record in records:
    #   print(record)

    for record in records:
        if count % 2 == 0:
            my_tree.insert(parent='',index='end',iid=count,text='',values=(record[0], record[2], record[1],record[25]),tags=('evenrow', ))
        else:
            my_tree.insert(parent='',index='end',iid=count,text='',values=(record[0], record[2], record[1],record[25]),tags=('oddrow', ))
        # increment counter
        count += 1

    # Commit changes
    conn.commit()

    # Close our connection
    conn.close()

def clear_form():
    f_name.delete(0, END)
    l_name.delete(0, END)
    date.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)
    email.delete(0, END)
    phone.delete(0, END)
    handedness.delete(0, END)
    num_of_hands.delete(0, END)
    middle_reverse.delete(0, END)
    ring_reverse.delete(0, END)
    middle_outward.delete(0, END)
    bridge.delete(0, END)
    ring_outward.delete(0, END)
    middle_forward.delete(0, END)
    ring_forward.delete(0, END)
    middle_span.delete(0, END)
    ring_span.delete(0, END)
    thumb_forward.delete(0, END)
    thumb_left.delete(0, END)
    thumb_right.delete(0, END)
    thumb_reverse.delete(0, END)
    ball_name.delete(0, END)
    ball_weight.delete(0, END)
    serial.delete(0, END)
    grip.delete(0, END)
    thumb_style.delete(0, END)
    thumb_size.delete(0, END)
    middle_style.delete(0, END)
    middle_size.delete(0, END)
    ring_style.delete(0, END)
    ring_size.delete(0, END)

def submit():
    #create or connect to DB
    conn = sqlite3.connect('bowlers.db')

    #creat cursor
    c = conn.cursor()

    c.execute(
        """INSERT INTO bowlers VALUES (
        :f_name, 
        :l_name,
        :date,
        :address,
        :city,
        :state,
        :zipcode,
        :email,
        :phone,
        :handedness,
        :num_of_hands,
        :ring_reverse,
        :middle_reverse,
        :ring_out,
        :bridge_width,
        :middle_out,
        :ring_forward,
        :middle_forward,
        :ring_span,
        :middle_span,
        :thumb_forward,
        :thumb_left,
        :thumb_right,
        :thumb_reverse,
        :ball_name,
        :ball_weight,
        :serial_number,
        :grip_type,
        :thumb_style,
        :thumb_size,
        :middle_style,
        :middle_size,
        :ring_style,
        :ring_size)""",
        {
            'f_name' : f_name.get(),
            'l_name' : l_name.get(),
            'date' : date.get(),
            'address' :address.get(),
            'city' :city.get(),
            'state' :state.get(),
            'zipcode' :zipcode.get(),
            'email' :email.get(),
            'phone' :phone.get(),
            'handedness' :handedness.get(),
            'num_of_hands' :num_of_hands.get(),
            'middle_reverse' :middle_reverse.get(),
            'ring_reverse' :ring_reverse.get(),
            'middle_out' :middle_outward.get(),
            'bridge_width' :bridge.get(),
            'ring_out' :ring_outward.get(),
            'middle_forward' :middle_forward.get(),
            'ring_forward' :ring_forward.get(),
            'middle_span' :middle_span.get(),
            'ring_span' :ring_span.get(),
            'thumb_forward' :thumb_forward.get(),
            'thumb_left' :thumb_left.get(),
            'thumb_right' :thumb_right.get(),
            'thumb_reverse' :thumb_reverse.get(),
            'ball_name' :ball_name.get(),
            'ball_weight' :ball_weight.get(),
            'serial_number' :serial.get(),
            'grip_type' :grip.get(),
            'thumb_style' :thumb_style.get(),
            'thumb_size' :thumb_size.get(),
            'middle_style' :middle_style.get(),
            'middle_size' :middle_size.get(),
            'ring_style' :ring_style.get(),
            'ring_size' :ring_size.get()
        })

    id = my_tree.insert('', 'end', text="", values=('', l_name.get(), f_name.get(), ball_name.get()))


    #commit changes
    conn.commit()

    #close connection
    conn.close()
    clear_form()


def edit():
    #create or connect to DB
    conn = sqlite3.connect('bowlers.db')

    #creat cursor
    c = conn.cursor()
    selected=my_tree.focus()
    values=my_tree.item(selected, 'values')
    idnum = values[0]
    c.execute(
        """UPDATE bowlers SET
        'f_name' = :f_name,
        'l_name' = :l_name,
        'date' = :date,
        'address'= :address,
        'city'= :city,
        'state'= :state,
        'zipcode'= :zipcode,
        'email'= :email,
        'phone'= :phone,
        'handedness'= :handedness,
        'num_of_hands'= :num_of_hands,
        'middle_reverse'= :middle_reverse,
        'ring_reverse'= :ring_reverse,
        'middle_out'= :middle_out,
        'bridge_width'= :bridge_width,
        'ring_out'= :ring_out,
        'middle_forward'= :middle_forward,
        'ring_forward'= :ring_forward,
        'middle_span'= :middle_span,
        'ring_span'= :ring_span,
        'thumb_forward'= :thumb_forward,
        'thumb_left'= :thumb_left,
        'thumb_right'= :thumb_right,
        'thumb_reverse'= :thumb_reverse,
        'ball_name'= :ball_name,
        'ball_weight'= :ball_weight,
        'serial_number'= :serial,
        'grip_type'= :grip,
        'thumb_style'= :thumb_style,
        'thumb_size'= :thumb_size,
        'middle_style'= :middle_style,
        'middle_size'= :middle_size,
        'ring_style'= :ring_style,
        'ring_size'= :ring_size

        WHERE oid = :oid""",
        {
            'f_name': f_name.get(),
            'l_name': l_name.get(),
            'date': date.get(),
            'address': address.get(),
            'city': city.get(),
            'state': state.get(),
            'zipcode': zipcode.get(),
            'email': email.get(),
            'phone': phone.get(),
            'handedness': handedness.get(),
            'num_of_hands': num_of_hands.get(),
            'middle_reverse': middle_reverse.get(),
            'ring_reverse': ring_reverse.get(),
            'middle_out': middle_outward.get(),
            'bridge_width': bridge.get(),
            'ring_out': ring_outward.get(),
            'middle_forward': middle_forward.get(),
            'ring_forward': ring_forward.get(),
            'middle_span': middle_span.get(),
            'ring_span': ring_span.get(),
            'thumb_forward': thumb_forward.get(),
            'thumb_left': thumb_left.get(),
            'thumb_right': thumb_right.get(),
            'thumb_reverse': thumb_reverse.get(),
            'ball_name': ball_name.get(),
            'ball_weight': ball_weight.get(),
            'serial': serial.get(),
            'grip': grip.get(),
            'thumb_style': thumb_style.get(),
            'thumb_size': thumb_size.get(),
            'middle_style': middle_style.get(),
            'middle_size': middle_size.get(),
            'ring_style': ring_style.get(),
            'ring_size': ring_size.get(),
            'oid' : idnum
        })

    #commit changes
    conn.commit()

    #close connection
    conn.close()
    my_tree.item(selected, text="", values =(idnum,l_name.get(), f_name.get(), ball_name.get()))
    clear_form()


# Remove Many records
def delete():
    #create or connect to DB
    conn = sqlite3.connect('bowlers.db')

    #creat cursor
    c = conn.cursor()
    selected=my_tree.focus()
    values=my_tree.item(selected, 'values')
    idnum = values[0]
    c.execute("""DELETE FROM bowlers WHERE oid == :idnum""",{'idnum': idnum})
    my_tree.delete(selected)

    #commit changes
    conn.commit()

    #close connection
    conn.close()
    clear_form()

def create_circle(x, y, r, canvasName): #center coordinates, radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvasName.create_oval(x0, y0, x1, y1,width = 5)

def select(e):
    clear_form()

    selected=my_tree.focus()
    values=my_tree.item(selected, 'values')
    idnum = values[0]
    # Create a database or connect to one that exists
    conn = sqlite3.connect('bowlers.db')

    # Create a cursor instance
    c = conn.cursor()

    c.execute("""SELECT * FROM bowlers WHERE oid == :idnum""",{'idnum': idnum})
    records = c.fetchall()
    for record in records:
        f_name.insert(0, record[0])
        l_name.insert(0, record[1])
        date.insert(0, record[2])
        address.insert(0, record[3])
        city.insert(0, record[4])
        state.insert(0, record[5])
        zipcode.insert(0, record[6])
        email.insert(0, record[7])
        phone.insert(0, record[8])
        handedness.insert(0, record[9])
        num_of_hands.insert(0, record[10])
        middle_reverse.insert(0, record[11])
        ring_reverse.insert(0, record[12])
        middle_outward.insert(0, record[13])
        bridge.insert(0, record[14])
        ring_outward.insert(0, record[15])
        middle_forward.insert(0, record[16])
        ring_forward.insert(0, record[17])
        middle_span.insert(0, record[18])
        ring_span.insert(0, record[19])
        thumb_forward.insert(0, record[20])
        thumb_left.insert(0, record[21])
        thumb_right.insert(0, record[22])
        thumb_reverse.insert(0, record[23])
        ball_name.insert(0, record[24])
        ball_weight.insert(0, record[25])
        serial.insert(0, record[26])
        grip.insert(0, record[27])
        thumb_style.insert(0, record[28])
        thumb_size.insert(0, record[29])
        middle_style.insert(0, record[30])
        middle_size.insert(0, record[31])
        ring_style.insert(0, record[32])
        ring_size.insert(0, record[33])

#create text box labels and entry
f_name_label = Label(myCanvas, text="First")
f_name_label.grid(row=0, column=0, pady=(20, 5))
f_name = Entry(myCanvas, width=38)
f_name.grid(row=0, column=1, pady=(20,5), sticky="NSEW")

l_name_label = Label(myCanvas, text="Last")
l_name_label.grid(row=0, column=2, pady=(20, 5))
l_name = Entry(myCanvas, width=30)
l_name.grid(row=0, column=3, pady=(20, 5), sticky="NSEW")

date_label = Label(myCanvas, text="Date")
date_label.grid(row=0, column=4, pady=(20, 5))
date = Entry(myCanvas, width=30)
date.grid(row=0, column=5, pady=(20, 5), sticky="NSEW")

address_label = Label(myCanvas, text="Address")
address_label.grid(row=1, column=0, pady=5)
address = Entry(myCanvas, width=128)
address.grid(row=1, column=1, columnspan=5, pady=5, sticky="NSEW")

city_label = Label(myCanvas, text="City")
city_label.grid(row=2, column=0, pady=5)
city = Entry(myCanvas, width=38)
city.grid(row=2, column=1, pady=5, sticky="NSEW")

state_label = Label(myCanvas, text="State")
state_label.grid(row=2, column=2, pady=5)
state = Entry(myCanvas, width=30)
state.grid(row=2, column=3, pady=5, sticky="NSEW")

zipcode_label = Label(myCanvas, text="Zipcode")
zipcode_label.grid(row=2, column=4, pady=5)
zipcode = Entry(myCanvas, width=30)
zipcode.grid(row=2, column=5, pady=5, sticky="NSEW")

email_label = Label(myCanvas, text="E-Mail")
email_label.grid(row=3, column=0, pady=5)
email = Entry(myCanvas, width=75)
email.grid(row=3, column=1, columnspan=3, pady=5, sticky="NSEW")

phone_label = Label(myCanvas, text="Phone")
phone_label.grid(row=3, column=4, pady=5)
phone = Entry(myCanvas, width=30)
phone.grid(row=3, column=5, pady=5, sticky="NSEW")

handedness_label = Label(myCanvas, text="Hand")
handedness_label.grid(row=4, column=0, pady=5)
handedness = Entry(myCanvas, width=75)
handedness.grid(row=4, column=1, columnspan=3, pady=5, sticky="NSEW")

num_of_hands_label = Label(myCanvas, text="# of Hands")
num_of_hands_label.grid(row=4, column=4, pady=5)
num_of_hands = Entry(myCanvas, width=30)
num_of_hands.grid(row=4, column=5, pady=5, sticky="NSEW")

middle_reverse_label = Label(myCanvas, text="Reverse")
middle_reverse_label.grid(row=5, column=0, columnspan=2, pady=5)
middle_reverse = Entry(myCanvas, width=10)
middle_reverse.grid(row=6, column=0, columnspan=2, pady=5)

ring_reverse_label = Label(myCanvas, text="Reverse")
ring_reverse_label.grid(row=5, column=4, columnspan=2, pady=5)
ring_reverse = Entry(myCanvas, width=10)
ring_reverse.grid(row=6, column=4, columnspan=2, pady=5)

middle_outward_label = Label(myCanvas, text="Outward")
middle_outward_label.grid(row=7, column=0, columnspan=2, pady=5)
middle_outward = Entry(myCanvas, width=10)
middle_outward.grid(row=8, column=0, columnspan=2, pady=5)

bridge_label = Label(myCanvas, text="Bridge")
bridge_label.grid(row=7, column=2, columnspan=2, pady=5)
bridge = Entry(myCanvas, width=10)
bridge.grid(row=8, column=2, columnspan=2, pady=5)

create_circle(280, 270, 50, myCanvas)
create_circle(520, 270, 50, myCanvas)
create_circle(405, 570, 50, myCanvas)

ring_outward_label = Label(myCanvas, text="Outward")
ring_outward_label.grid(row=7, column=4, columnspan=2, pady=5)
ring_outward = Entry(myCanvas, width=10)
ring_outward.grid(row=8, column=4, columnspan=2, pady=5)

middle_forward_label = Label(myCanvas, text="Forward")
middle_forward_label.grid(row=9, column=0, columnspan=2, pady=5)
middle_forward = Entry(myCanvas, width=10)
middle_forward.grid(row=10, column=0, columnspan=2, pady=5)

ring_forward_label = Label(myCanvas, text="Forward")
ring_forward_label.grid(row=9, column=4, columnspan=2, pady=5)
ring_forward = Entry(myCanvas, width=10)
ring_forward.grid(row=10, column=4, columnspan=2, pady=5)

middle_span_label = Label(myCanvas, text="Span")
middle_span_label.grid(row=11, column=1, columnspan=3, pady=5)
middle_span = Entry(myCanvas, width=10)
middle_span.grid(row=12, column=1, columnspan=3, pady=(0, 60))

ring_span_label = Label(myCanvas, text="Span", anchor=E)
ring_span_label.grid(row=11, column=3, pady=5, columnspan=2, padx=(65, 0))
ring_span = Entry(myCanvas, width=10)
ring_span.grid(row=12,
               column=3,
               pady=(0, 60),
               columnspan=2,
               padx=(65, 0))
#ring_span.place(x=478, y=378)
#ring_span_label.place(x=494, y=354)

thumb_forward_label = Label(myCanvas, text="Forward")
thumb_forward_label.grid(row=13, column=2, columnspan=2, pady=5)
thumb_forward = Entry(myCanvas, width=10)
thumb_forward.grid(row=14, column=2, columnspan=2, pady=(0, 30))

thumb_left_label = Label(myCanvas, text="Left")
thumb_left_label.grid(row=15, column=1, columnspan=3, pady=5)
thumb_left = Entry(myCanvas, width=10)
thumb_left.grid(row=16, column=1, columnspan=3, pady=(0, 40))

thumb_right_label = Label(myCanvas, text="Right")
thumb_right_label.grid(row=15, column=3, pady=5, columnspan=2, padx=(65, 0))
thumb_right = Entry(myCanvas, width=10)
thumb_right.grid(row=16,
                 column=3,
                 pady=(0, 40),
                 columnspan=2,
                 padx=(65, 0))
#thumb_right.place(x=484, y=568)
#thumb_right_label.place(x=500, y=544)

thumb_reverse_label = Label(myCanvas, text="Reverse")
thumb_reverse_label.grid(row=17, column=2, columnspan=2, pady=5)
thumb_reverse = Entry(myCanvas, width=10)
thumb_reverse.grid(row=18, column=2, columnspan=2, pady=(0, 30))

ball_name_label = Label(myCanvas, text="Ball Name")
ball_name_label.grid(row=19, column=0, pady=5)
ball_name = Entry(myCanvas, width=38)
ball_name.grid(row=19, column=1, pady=5, sticky="NSEW")

ball_weight_label = Label(myCanvas, text="Weight")
ball_weight_label.grid(row=19, column=2, pady=5)
ball_weight = Entry(myCanvas, width=20)
ball_weight.grid(row=19, column=3, pady=5, sticky="NSEW")

serial_label = Label(myCanvas, text="Serial")
serial_label.grid(row=19, column=4, pady=5)
serial = Entry(myCanvas, width=30)
serial.grid(row=19, column=5, pady=5, sticky="NSEW")

insert_label = Label(myCanvas, text="Insert")
insert_label.grid(row=20, column=2, pady=5)
style_label = Label(myCanvas, text="Style")
style_label.grid(row=20, column=3, pady=5)
size_label = Label(myCanvas, text="Size")
size_label.grid(row=20, column=4, pady=5)

grip_label = Label(myCanvas, text="Grip")
grip_label.grid(row=21, column=0, pady=5)
grip = Entry(myCanvas, width=38)
grip.grid(row=21, column=1, pady=5, sticky="NSEW")

thumb_label = Label(myCanvas, text="Thumb")
thumb_label.grid(row=21, column=2, pady=5)
thumb_style = Entry(myCanvas, width=20)
thumb_style.grid(row=21, column=3, pady=5, sticky="NSEW")
thumb_size = Entry(myCanvas, width=20)
thumb_size.grid(row=21, column=4, pady=5, sticky="NSEW")

middle_label = Label(myCanvas, text="Middle")
middle_label.grid(row=22, column=2, pady=5)
middle_style = Entry(myCanvas, width=20)
middle_style.grid(row=22, column=3, pady=5, sticky="NSEW")
middle_size = Entry(myCanvas, width=20)
middle_size.grid(row=22, column=4, pady=5, sticky="NSEW")

ring_label = Label(myCanvas, text="Ring")
ring_label.grid(row=23, column=2, pady=5)
ring_style = Entry(myCanvas, width=20)
ring_style.grid(row=23, column=3, pady=5, sticky="NSEW")
ring_size = Entry(myCanvas, width=20)
ring_size.grid(row=23, column=4, pady=5, sticky="NSEW")

submit_btn = Button(myCanvas, text="Add New", command=submit)
submit_btn.grid(row=24, column=0, columnspan=2, ipadx=50)
delete_btn = Button(myCanvas, text="Delete", command=delete)
delete_btn.grid(row=24, column=3, ipadx=50)

clear_btn = Button(myCanvas, text="Clear", command=clear_form)
clear_btn.grid(row=25, column=3, ipadx=50)
edit_btn = Button(myCanvas, text="Update", command=edit)
edit_btn.grid(row=25, column=0, columnspan=2, ipadx=50)





#s = Style()
#s.configure('TFrame', borderwidth=5)

table_frame = Frame(myCanvas, height=900, width=750, relief=GROOVE, borderwidth=10)
table_frame.grid_propagate(0)
table_frame.grid(row=0,column=7,columnspan=5, rowspan=30,pady=(20, 0),padx=(10, 0),sticky=N)

style=Style()
style.theme_use('default')
style.configure("Treeview",
    background="#D3D3D3",
    foreground="black",
    rowheight=25,
    fieldbackground="#D3D3D3")

style.map('Treeview',
    background=[('selected', "#347083")])


tree_scroll = Scrollbar(table_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

my_tree = Treeview(table_frame, yscrollcommand=tree_scroll.set, selectmode="extended", height=35)
my_tree['columns'] = ("ID", "Last Name", "First Name", "Ball Name")

my_tree.pack()

tree_scroll.config(command=my_tree.yview)

my_tree.column("#0", width=0, stretch=NO)
my_tree.column("ID", anchor=N, width=100, minwidth=30)
my_tree.column("Last Name", anchor=CENTER, width=200, minwidth=30)
my_tree.column("First Name", anchor=CENTER, width=200, minwidth=30)
my_tree.column("Ball Name", anchor=CENTER, width=200, minwidth=30)

my_tree.heading("#0", text='')
my_tree.heading("ID", text="ID", anchor=CENTER)
my_tree.heading("Last Name", text="Last Name", anchor=CENTER)
my_tree.heading("First Name", text="First Name", anchor=CENTER)
my_tree.heading("Ball Name", text="Ball Name", anchor=CENTER)

my_tree.tag_configure('oddrow', background="white")
my_tree.tag_configure('evenrow', background="lightblue")

entry_list = [f_name, l_name, date, address, city, state, zipcode, email, phone,handedness, num_of_hands, middle_reverse, ring_reverse, middle_outward, bridge, ring_outward, middle_forward, ring_forward, middle_size, ring_span, thumb_forward, thumb_left, thumb_right, thumb_reverse, ball_name, ball_weight, serial, grip, thumb_style, thumb_size, middle_size, middle_style, ring_size, ring_style]

row_number = 0
for entry in entry_list:
    Grid.rowconfigure(myCanvas, row_number, weight=1)
    Grid.columnconfigure(myCanvas, row_number, weight=1)
    row_number+=1


my_tree.bind("<ButtonRelease-1>", select)

query_database()


root.mainloop()
