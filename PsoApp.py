from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter.ttk import *
import sqlite3

root = Tk()
root.title("Pro Shop Helper")
root.iconbitmap('bowling.ico')
root.geometry("1600x1000")

myCanvas = Canvas(root)
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
'''
class Shape:
    def __init__(self, master=None):
        self.master = master

        # Calls create method of class Shape
        self.create()

    def create(self):

        # Creates a object of class canvas
        # with the help of this we can create different shapes
        self.canvas = Canvas(self.master)

        # Creates a circle of diameter 80
        self.canvas.create_oval(400,
                                400,
                                100,
                                100,
                                outline="black",
                                fill="white",
                                width=2)

        self.canvas.place(x=0, y=0)
'''





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



    #commit changes
    conn.commit()

    #close connection

    conn.close()
def create_circle(x, y, r, canvasName): # center coordinates, radius
    x0 = x-r
    y0 = y-r
    x1 = x+r
    y1 = y+r
    return canvasName.create_oval(x0,y0,x1,y1)

def show():

    #create or connect to DB
    conn = sqlite3.connect('bowlers.db')

    #creat cursor
    c = conn.cursor()

    c.execute("SELECT *, oid FROM bowlers ORDER BY l_name")
    bowlers = c.fetchall()
    #print(bowlers)


    #commit changes
    conn.commit()

    #close connection
    conn.close()


'''
    oid_bowlers = ''
    f_name_bowlers = ''
    l_name_bowlers = ''
    ball_name_bowlers = ''
    for bowler in bowlers:
        oid_bowlers += str(bowler[34]) + '\n'
        f_name_bowlers += str(bowler[0]) + '\n'
        l_name_bowlers += str(bowler[1]) + '\n'
        ball_name_bowlers += str(bowler[24]) + '\n'

    oid_bowlers_label = Label(table_frame, text=oid_bowlers)
    oid_bowlers_label.grid(row=1, column=7)
    f_name_bowlers_label = Label(table_frame, text=f_name_bowlers)
    f_name_bowlers_label.grid(row=1, column=9)
    l_name_bowlers_label = Label(table_frame, text=l_name_bowlers)
    l_name_bowlers_label.grid(row=1, column=8)
    ball_name_bowlers_label = Label(table_frame, text=ball_name_bowlers)
    ball_name_bowlers_label.grid(row=1, column=10)
'''



#create text box labels and entry
f_name_label = Label(myCanvas, text="First", anchor=W)
f_name_label.grid(row=0, column=0, pady=(20, 5))
f_name = Entry(myCanvas, width=38)
f_name.grid(row=0, column=1, pady=(20,5))

l_name_label = Label(myCanvas, text="Last", anchor=W)
l_name_label.grid(row=0, column=2, pady=(20, 5))
l_name = Entry(myCanvas, width=30)
l_name.grid(row=0, column=3, pady=(20, 5))

date_label = Label(myCanvas, text="Date", anchor=W)
date_label.grid(row=0, column=4, pady=(20, 5))
date = Entry(myCanvas, width=30)
date.grid(row=0, column=5, pady=(20, 5))

address_label = Label(myCanvas, text="Address", anchor=W)
address_label.grid(row=1, column=0, pady=5)
address = Entry(myCanvas, width=128)
address.grid(row=1, column=1, columnspan=5, pady=5)

city_label = Label(myCanvas, text="City", anchor=W)
city_label.grid(row=2, column=0, pady=5)
city = Entry(myCanvas, width=38)
city.grid(row=2, column=1, pady=5)

state_label = Label(myCanvas, text="State", anchor=W)
state_label.grid(row=2, column=2, pady=5)
state = Entry(myCanvas, width=30)
state.grid(row=2, column=3, pady=5)

zipcode_label = Label(myCanvas, text="Zipcode", anchor=W)
zipcode_label.grid(row=2, column=4, pady=5)
zipcode = Entry(myCanvas, width=30)
zipcode.grid(row=2, column=5, pady=5)

email_label = Label(myCanvas, text="E-Mail", anchor=W)
email_label.grid(row=3, column=0, pady=5)
email = Entry(myCanvas, width=75)
email.grid(row=3, column=1, columnspan=3, pady=5)

phone_label = Label(myCanvas, text="Phone", anchor=W)
phone_label.grid(row=3, column=4, pady=5)
phone = Entry(myCanvas, width=30)
phone.grid(row=3, column=5, pady=5)

handedness_label = Label(myCanvas, text="Hand", anchor=W)
handedness_label.grid(row=4, column=0, pady=5)
handedness = Entry(myCanvas, width=75)
handedness.grid(row=4, column=1, columnspan=3, pady=5)

num_of_hands_label = Label(myCanvas, text="# of Hands", anchor=W)
num_of_hands_label.grid(row=4, column=4, pady=5)
num_of_hands = Entry(myCanvas, width=30)
num_of_hands.grid(row=4, column=5, pady=5)

middle_reverse_label = Label(myCanvas, text="Reverse", anchor=W)
middle_reverse_label.grid(row=5, column=0, columnspan=2, pady=5)
middle_reverse = Entry(myCanvas, width=10)
middle_reverse.grid(row=6, column=0, columnspan=2, pady=5)

ring_reverse_label = Label(myCanvas, text="Reverse", anchor=W)
ring_reverse_label.grid(row=5, column=4, columnspan=2, pady=5)
ring_reverse = Entry(myCanvas, width=10)
ring_reverse.grid(row=6, column=4, columnspan=2, pady=5)

middle_outward_label = Label(myCanvas, text="Outward", anchor=W)
middle_outward_label.grid(row=7, column=0, columnspan=2, pady=5)
middle_outward = Entry(myCanvas, width=10)
middle_outward.grid(row=8, column=0, columnspan=2, pady=5)

bridge_label = Label(myCanvas, text="Bridge", anchor=W)
bridge_label.grid(row=7, column=2, columnspan=2, pady=5)
bridge = Entry(myCanvas, width=10)
bridge.grid(row=8, column=2, columnspan=2, pady=5)

ring_outward_label = Label(myCanvas, text="Outward", anchor=W)
ring_outward_label.grid(row=7, column=4, columnspan=2, pady=5)
ring_outward = Entry(myCanvas, width=10)
ring_outward.grid(row=8, column=4, columnspan=2, pady=5)

middle_forward_label = Label(myCanvas, text="Forward", anchor=W)
middle_forward_label.grid(row=9, column=0, columnspan=2, pady=5)
middle_forward = Entry(myCanvas, width=10)
middle_forward.grid(row=10, column=0, columnspan=2, pady=5)

ring_forward_label = Label(myCanvas, text="Forward", anchor=W)
ring_forward_label.grid(row=9, column=4, columnspan=2, pady=5)
ring_forward = Entry(myCanvas, width=10)
ring_forward.grid(row=10, column=4, columnspan=2, pady=5)

middle_span_label = Label(myCanvas, text="Span", anchor=W)
middle_span_label.grid(row=11, column=1, columnspan=3, pady=5)
middle_span = Entry(myCanvas, width=10)
middle_span.grid(row=12, column=1, columnspan=3, pady=(0, 60))

ring_span_label = Label(myCanvas, text="Span", anchor=E)
#middle_span_label.grid(row=11, column=2, columnspan=4, pady=5)
ring_span = Entry(myCanvas, width=10)
#middle_span.grid(row=12, column=2, columnspan=4 , pady=(0, 60))
ring_span.place(x=478, y=378)
ring_span_label.place(x=494, y=354)

thumb_forward_label = Label(myCanvas, text="Forward", anchor=W)
thumb_forward_label.grid(row=13, column=2, columnspan=2, pady=5)
thumb_forward = Entry(myCanvas, width=10)
thumb_forward.grid(row=14, column=2, columnspan=2, pady=(0, 30))

thumb_left_label = Label(myCanvas, text="Left", anchor=W)
thumb_left_label.grid(row=15, column=1, columnspan=3, pady=5)
thumb_left = Entry(myCanvas, width=10)
thumb_left.grid(row=16, column=1, columnspan=3, pady=(0, 40))

thumb_right_label = Label(myCanvas, text="Right", anchor=W)
#thumb_right_label.grid(row=15, column=2, columnspan=4, pady=5)
thumb_right = Entry(myCanvas, width=10)
#thumb_right.grid(row=16, column=2, columnspan=4, pady=(0,40))
thumb_right.place(x=484, y=568)
thumb_right_label.place(x=500, y=544)

thumb_reverse_label = Label(myCanvas, text="Reverse", anchor=W)
thumb_reverse_label.grid(row=17, column=2, columnspan=2, pady=5)
thumb_reverse = Entry(myCanvas, width=10)
thumb_reverse.grid(row=18, column=2, columnspan=2, pady=(0, 30))

create_circle(500,600,10,myCanvas)

ball_name_label = Label(myCanvas, text="Ball Name", anchor=W)
ball_name_label.grid(row=19, column=0, pady=5)
ball_name = Entry(myCanvas, width=38)
ball_name.grid(row=19, column=1, pady=5)

ball_weight_label = Label(myCanvas, text="Weight", anchor=W)
ball_weight_label.grid(row=19, column=2, pady=5)
ball_weight = Entry(myCanvas, width=20)
ball_weight.grid(row=19, column=3, pady=5)

serial_label = Label(myCanvas, text="Serial", anchor=W)
serial_label.grid(row=19, column=4, pady=5)
serial = Entry(myCanvas, width=30)
serial.grid(row=19, column=5, pady=5)

insert_label = Label(myCanvas, text="Insert", anchor=W)
insert_label.grid(row=20, column=2, pady=5)
style_label = Label(myCanvas, text="Style", anchor=W)
style_label.grid(row=20, column=3, pady=5)
size_label = Label(myCanvas, text="Size", anchor=W)
size_label.grid(row=20, column=4, pady=5)

grip_label = Label(myCanvas, text="Grip", anchor=W)
grip_label.grid(row=21, column=0, pady=5)
grip = Entry(myCanvas, width=38)
grip.grid(row=21, column=1, pady=5)

thumb_label = Label(myCanvas, text="Thumb", anchor=W)
thumb_label.grid(row=21, column=2, pady=5)
thumb_style = Entry(myCanvas, width=20)
thumb_style.grid(row=21, column=3, pady=5)
thumb_size = Entry(myCanvas, width=20)
thumb_size.grid(row=21, column=4, pady=5)

middle_label = Label(myCanvas, text="Middle", anchor=W)
middle_label.grid(row=22, column=2, pady=5)
middle_style = Entry(myCanvas, width=20)
middle_style.grid(row=22, column=3, pady=5)
middle_size = Entry(myCanvas, width=20)
middle_size.grid(row=22, column=4, pady=5)

ring_label = Label(myCanvas, text="Ring", anchor=W)
ring_label.grid(row=23, column=2, pady=5)
ring_style = Entry(myCanvas, width=20)
ring_style.grid(row=23, column=3, pady=5)
ring_size = Entry(myCanvas, width=20)
ring_size.grid(row=23, column=4, pady=5)

submit_btn = Button(myCanvas, text="Add Drill Sheet", command=submit)
submit_btn.grid(row=24, column=0, columnspan=6, ipadx=200)

edit_btn = Button(myCanvas, text="List Drill Sheets", command=show)
edit_btn.grid(row=25, column=0, columnspan=6, ipadx=200)





#s = Style()
#s.configure('TFrame', borderwidth=5)

table_frame = Frame(myCanvas, height=900, width=750, relief=GROOVE, borderwidth=10)
table_frame.grid_propagate(0)
table_frame.grid(row=0,column=7,columnspan=5, rowspan=30,pady=(20, 0),padx=(10, 0),sticky=N)


my_tree = Treeview(table_frame)
my_tree['columns'] = ("ID", "Last Name", "First Name", "Ball Name")

my_tree.column("#0", width=0)
my_tree.column("ID", anchor=W)
my_tree.column("First Name")
my_tree.column("Last Name")
my_tree.column("Ball Name")


'''
table_id = Label(table_frame, text="Table ID")
table_id.grid(row=0, column=7, pady=(20, 5), padx=50)

table_f_name = Label(table_frame, text="First Name")
table_f_name.grid(row=0, column=9, pady=(20, 5), padx=50)

table_l_name = Label(table_frame, text="Last Name")
table_l_name.grid(row=0, column=8, pady=(20, 5), padx=50)

table_ball_name = Label(table_frame, text="Ball Name")
table_ball_name.grid(row=0, column=10, pady=(20, 5), padx=50)
'''



#shape = Shape(root)



#commit changes
conn.commit()

#close connection
conn.close()

root.mainloop()
