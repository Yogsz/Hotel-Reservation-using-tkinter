from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

def login():
    def insert():
        try:
            conn = mysql.connector.connect(user='root', password='yogesh2005', host='localhost', database="hotel_reservation", port='3306')
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO booking 
                (first_name, second_name, contact, email, room_type, checkIn_date, checkIn_time, checkOut_date) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """,
                (
                    first_name.get(),
                    second_name.get(),
                    contact_entry.get(),
                    email_entry.get(),
                    cb1.get(),
                    arrival_date.get(),
                    arrival_time.get(),
                    leave_date.get()
                )
            )
            conn.commit()
            messagebox.showinfo('CONFIRM', 'You successfully reserved a room!')
        except mysql.connector.Error as err:
            messagebox.showerror('Error',"SORRY! SOMETHING WENT WRONG")
        finally:
            cursor.close()
            conn.close()

    def on_enter2(e):
        e.widget.config(bg="white", fg="black")

    def on_leave2(e):
        e.widget.config(bg="dark orange", fg="white")
    
    global login_image

    login=Toplevel(root)
    login.title("www.palace mario.com")
    login.iconbitmap('icon.ico')
    w=login.winfo_screenwidth()
    h=login.winfo_screenheight()
    login.geometry(f"{w}x{h}")
    login_image = PhotoImage(file=r"D:\Downloads\wallhaven-z8kevw_1920x1080.png")

    canvas = Canvas(login, width=w, height=h)
    canvas.pack(fill="both", expand=True)

    canvas.create_image(0, 0, anchor=NW, image=login_image)

    frame = Frame(login, bg="white", width=1000, height=1000, padx=20, pady=20, relief=GROOVE, bd=2, highlightbackground="orange", highlightthickness=2)
    window_id = canvas.create_window(w//2, h//2, window=frame, anchor="center")

    Label(frame, text="Room Reservation System", font=("Helvetica", 30, "bold"),bg="white",fg="dark orange").place(x=230,y=50)
    Label(frame,text="Experience something new every moment.",font=("Algerian", 15),bg="white").place(x=265,y=100)
    Label(frame,text="Name",font=("Helvetica", 15,"bold"),bg="white").place(x=30,y=150)
    first_name=Entry(frame,width=35,bd=1,relief=SOLID)
    first_name.place(x=30,y=190,height=30)
    second_name=Entry(frame,width=35,bd=1,relief=SOLID)
    second_name.place(x=270,y=190,height=30)

    Label(frame,text="First Name",font=("Helvetica", 10),bg="white").place(x=30,y=220)
    Label(frame,text="Second Name",font=("Helvetica", 10),bg="white").place(x=270,y=220)

    Label(frame,text="Email",font=("Helvetica", 15,"bold"),bg="white").place(x=670,y=150)
    email_entry=Entry(frame,width=35,bd=1,relief=SOLID)
    email_entry.place(x=670,y=190,height=30)

    Label(frame,text="Contact",font=("Helvetica", 15,"bold"),bg="white").place(x=30,y=270)
    contact_entry=Entry(frame,width=35,bd=1,relief=SOLID)
    contact_entry.place(x=30,y=310,height=30)

    Label(frame,text="No.of Guest",font=("Helvetica", 15,"bold"),bg="white").place(x=670,y=270)
    members_ip = Spinbox(frame, width=30,relief=SOLID, from_=1, to=6)
    members_ip.place(x=670, y=310, height=30)
    options = [
    'Standard Room(1 to 2 People)', 'Family Room(1 to 4 People)', 'Private Room(1 to 3 People)',
    'Mix Dorm Room(6 People)', 'Female Dorm Room(6 People)', 'Male Dorm Room(6 People)'
    ]
    Label(frame,text="Room Type",font=("Helvetica", 15,"bold"),bg="white").place(x=30,y=370)
    border_frame = Frame(frame, bd=1, relief=SOLID)  
    border_frame.place(x=30, y=410, height=30, width=300)

    cb1 = ttk.Combobox(border_frame, values=options, width=30)
    cb1.pack(fill=BOTH, expand=True)  
    cb1.set('Please Select')

    arrival_label = Label(frame,bg="white", text='Check IN',font=("Helvetica", 15,"bold"))
    arrival_label.place(x=30, y=470)
    arrival_date = Entry(frame, width=75,relief=SOLID)
    arrival_date.place(x=30, y=510, height=30)
    checkin = Label(frame,bg="white", text="Please enter Check In Date   (yyyy-mm-dd)")
    checkin.place(x=30, y=540)
    arrival_time = Entry(frame, width=20,relief=SOLID)
    arrival_time.place(x=500, y=510, height=30)
    arrival_time.insert(0, "07:30")

    cb_frame=Frame(frame,bd=1,relief=SOLID)
    cb_frame.place(x=650,y=510,height=30,width=100)
    am_pm = ttk.Combobox(cb_frame, width=10, values=['AM', 'PM'])
    am_pm.pack(fill=BOTH, expand=True)
    am_pm.set('AM')

    leave_label = Label(frame,bg="white", text='Check Out',font=("Helvetica", 15,"bold"))
    leave_label.place(x=30, y=590)
    leave_date = Entry(frame, width=75,relief=SOLID)
    leave_date.place(x=30, y=630, height=30)
    checkout = Label(frame,bg="white",text="Please Enter a Check Out Date    (yyyy-mm-dd)")
    checkout.place(x=30, y=660)

    payment = Label(frame, text='Payment Method',bg="white",font=("Helvetica", 15,"bold"))
    payment.place(x=30, y=710)
    r1 = IntVar()
    rad1 = Radiobutton(frame, text='Online Payment', font=("Helvetica",14),bg="white", value=1, variable=r1)
    rad2 = Radiobutton(frame, text='Offline Payment', font=("Helvetica",14),bg="white", value=2, variable=r1)
    rad1.place(x=30, y=750)
    rad2.place(x=280, y=750)


    confirm = Button(frame, text='Confirm', font=("Helvetica", 12, "bold"), bg="dark orange", fg="white", activebackground="orange", activeforeground="white", relief=FLAT, padx=20, pady=8,command=insert)
    confirm.place(x=800, y=820)
    cancel=Button(frame,text="Cancel",font=("Helvetica", 12, "bold"),bg="dark orange",fg="white",activebackground="orange",activeforeground="white",relief=FLAT,padx=20,pady=8,command=login.destroy)
    cancel.place(x=30,y=820)
    confirm.bind("<Enter>", on_enter2)
    confirm.bind("<Leave>", on_leave2)
    cancel.bind("<Enter>", on_enter2)
    cancel.bind("<Leave>", on_leave2)



def login_admin():
    def login():
        def database_table():
            def update_record():
                def save_update():
                    # new_values should skip the first entry (booking_id)
                    # so we use entries[1:] to get the last 8 values
                    new_values = [entry.get() for entry in entries[1:]]

                    try:
                        conn = mysql.connector.connect(user='root', password='yogesh2005',
                                                    host='localhost', database="hotel_reservation", port='3306')
                        cursor = conn.cursor()
                        cursor.execute("""
                            UPDATE booking 
                            SET first_name=%s, second_name=%s, contact=%s, Email=%s, room_type=%s, 
                                checkIn_date=%s, checkIn_time=%s, checkOut_date=%s 
                            WHERE contact=%s
                        """, (*new_values, values[4]))  
                        conn.commit()
                        cursor.close()
                        conn.close()
                        tree.item(selected_item, values=(values[0], *new_values))

                        update_window.destroy()
                        table.withdraw()
                        messagebox.showinfo('Success', 'Record updated successfully')
                    except mysql.connector.Error as err:
                        messagebox.showerror('Database Error', f"Error: {err}")

                
                selected_item = tree.selection()[0]
                values = tree.item(selected_item, 'values')
                update_window = Toplevel(data_window)
                update_window.title("Update Record")
                update_window.iconbitmap('apartment_naj_icon.ico')
                
                labels = ['Booking_id', 'First Name', 'Second Name', 'Contact', 'Email', 'Room Type', 'Check In Date', 'Check In Time', 'Check Out Date']
                entries = []
                for i, label in enumerate(labels):
                    Label(update_window, text=label).grid(row=i, column=0, padx=15, pady=15)
                    entry = Entry(update_window)
                    entry.grid(row=i, column=1, padx=15, pady=15)
                    entry.insert(0, values[i])
                    entries.append(entry)
                Button(update_window, text="Save", command=save_update).grid(row=len(labels), column=1)

            def delete_record(tree):
                selected_item = tree.selection()[0]
                if selected_item:
                    values = tree.item(selected_item, 'values')
                    confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete the record of {values[0]}?")
                    if confirm:
                        conn = mysql.connector.connect(user='root', password='yogesh2005', host='localhost', database="hotel_reservation", port='3306')
                        cursor = conn.cursor()
                        cursor.execute("DELETE FROM booking WHERE contact=%s", (values[3],))
                        conn.commit()
                        cursor.close()
                        conn.close()
                        tree.delete(selected_item)
                        messagebox.showinfo('Success', 'Record deleted successfully')
                    else:
                        messagebox.showwarning("No selection", "Please select a record to delete")

            data_window = Toplevel(table)
            data_window.title("Database")
            conn = mysql.connector.connect(user='root', password='yogesh2005', host='localhost', database="hotel_reservation", port='3306')
            cursor = conn.cursor()
            columns = ('Booking ID', 'First Name', 'Second Name', 'Contact', 'Email', 'Room Type', 'Check In Date', 'Check In Time', 'Check Out Date')
            tree = ttk.Treeview(data_window, columns=columns, show='headings')
            for col in columns:
                tree.heading(col, text=col)
                tree.column(col, width=100)
            cursor.execute("SELECT * FROM booking")
            rows = cursor.fetchall()
            for row in rows:
                tree.insert('', END, values=row)
            yscroll = ttk.Scrollbar(data_window, orient=VERTICAL, command=tree.yview)
            tree.configure(yscrollcommand=yscroll.set)
            yscroll.pack(side=RIGHT, fill=Y)
            xscroll = ttk.Scrollbar(data_window, orient=HORIZONTAL, command=tree.xview)
            tree.configure(xscrollcommand=xscroll.set)
            xscroll.pack(side=BOTTOM, fill=X)
            tree.pack(fill=BOTH, expand=True)
            update_button = Button(data_window, text='UPDATE', command=update_record)
            update_button.pack(side=LEFT, padx=10, pady=10)
            delete_button = Button(data_window, text='DELETE', command=lambda: delete_record(tree))
            delete_button.pack(side=RIGHT, padx=10, pady=10)
            cursor.close()
            conn.close()

        username = username_entry.get()
        password = password_entry.get()
        if username == 'root' and password == 'yogesh2005':
            messagebox.showinfo('Login', 'Login Successful')
            root.destroy()
            table = Tk()
            table.geometry('300x300')
            table.title("Admin Use")
            table.iconbitmap('icon.ico') 
            database_button = Button(table, text="Get in➡", font=('bold', 20), command=database_table)
            database_button.pack(side=RIGHT)
        else:
            messagebox.showerror('Login', 'Sorry! You are not an Admin')

    admin_window = Toplevel(root)
    admin_window.title("www.Room Reservation.com")
    admin_window.iconbitmap('icon.ico')
    admin_window.geometry('500x400')
    frame = Frame(admin_window, bg="white", padx=20, pady=20, relief=GROOVE, bd=2)
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)
    Label(admin_window, text="Room Reservation System", font=("Helvetica", 16, "bold"), fg="#37474f", bg="#eceff1").pack(pady=20)

    frame = Frame(admin_window, bg="white", padx=30, pady=30, relief=FLAT, bd=0)
    frame.pack(pady=10)

    Label(frame, text="Username", font=("Helvetica", 12), bg="white", fg="#37474f").grid(row=0, column=0, pady=10, sticky=W)
    username_entry = Entry(frame, width=25, font=("Helvetica", 12), bd=1, relief=SOLID)
    username_entry.grid(row=0, column=1, pady=10)

    Label(frame, text="Password", font=("Helvetica", 12), bg="white", fg="#37474f").grid(row=1, column=0, pady=10, sticky=W)
    password_entry = Entry(frame, width=25, font=("Helvetica", 12), bd=1, relief=SOLID, show="*")
    password_entry.grid(row=1, column=1, pady=10)

    login_button = Button(frame, text="Login", font=("Helvetica", 12, "bold"), bg="#00796b", fg="white",
                          activebackground="#004d40", activeforeground="white", relief=FLAT, padx=20, pady=8, command=login)
    login_button.grid(row=2, columnspan=2, pady=20)

    Label(admin_window, text="© 2025 Room Reservation System", font=("Helvetica", 10), bg="#eceff1", fg="#78909c").pack(side=BOTTOM, pady=10)

def contact_us():
    contact_us = Toplevel()
    contact_us.title("CONTACT US")
    contact_us.iconbitmap('apartment_naj_icon.ico')
    w = contact_us.winfo_screenwidth()
    h = contact_us.winfo_screenheight()
    contact_us.geometry(f"{w}x{h}")

    contact_us.config(bg="#f5f5f5")

    content_frame = Frame(contact_us, bg="white", padx=20, pady=20, relief="flat", bd=0)
    content_frame.pack(padx=50, pady=20, fill=BOTH, expand=True)


    contact_content = """
📍 Address:
Palace Mario, Serenity Street, Dreamland City, Country

📞 Phone:
+123 456 7890 (Reception)
+987 654 3210 (Customer Support)

✉️ Email:
info@palacemario.com
support@palacemario.com

🌐 Website:
www.palacemario.com

🔗 Follow Us on Social Media:
📌 Facebook: facebook.com/PalaceMario
📌 Instagram: instagram.com/PalaceMario
📌 Twitter (X): twitter.com/PalaceMario
📌 YouTube: youtube.com/PalaceMario

🕒 Business Hours:
Monday – Friday: 9 AM – 8 PM
Saturday – Sunday: 10 AM – 6 PM

📍 Find Us on Google Maps:
Click here to view our location
"""

    # Use Text widget for the contact content
    text_widget = Text(
        content_frame,
        font=("Segoe UI Emoji", 14),
        wrap=WORD,
        bg="white",
        fg="#333",
        relief="flat",
        height=30,
    )
    text_widget.insert(INSERT, contact_content)
    text_widget.config(state=DISABLED)  # Make text uneditable
    text_widget.pack(fill=BOTH, expand=True)

    
def show_about_us():
    about_content="""
WELCOME TO PALACE MARIO – Where Every Stay Feels Like Home

        Palace Mario redefines hospitality by offering a perfect blend of luxury, comfort, and tradition. Situated in the heart of serene landscapes, our resort is a destination where dreams come to life, and every moment is crafted to perfection.

Our Legacy:
        Established with a vision to create a sanctuary of tranquility, Palace Mario has become synonymous with elegance and exceptional service. Over the years, we have welcomed travelers from across the globe, creating timeless memories for every guest who walks through our doors.

Facilities Designed for Perfection:
- **Luxurious Accommodations**: Experience the ultimate comfort in our meticulously designed rooms and suites, featuring world-class interiors and breathtaking views.
- **Gourmet Dining**: Indulge in an extraordinary culinary journey with our award-winning chefs offering cuisines from around the world.
- **Recreational Activities**: From water sports to yoga sessions, we offer a range of activities to rejuvenate your body and mind.
- **Event Spaces**: Host your dream wedding, corporate retreat, or special celebration in our state-of-the-art banquet halls.

Sustainability and Responsibility:
        At Palace Mario, we take our responsibility toward the environment seriously. Our sustainability initiatives include:
- Using renewable energy sources to power our operations.
- Minimizing waste by implementing eco-friendly practices.
- Supporting local communities by sourcing materials and services locally.

Our Philosophy:
        At the core of Palace Mario is our commitment to creating experiences that go beyond expectations. Every member of our staff is trained to provide personalized service, ensuring that no detail is overlooked. Your satisfaction is our highest priority.

Memorable Guest Experiences:
        Our guests are the soul of Palace Mario. Here are some of their unforgettable experiences:
- “I came here to relax, but I left with memories I will cherish forever.”
- “The staff went above and beyond to make my stay special. I can’t wait to return.”
- “Every corner of Palace Mario feels like it was designed with love and care.”

Explore Beyond:
        While we pride ourselves on the experience within the resort, we encourage our guests to explore the wonders nearby:
- **Heritage Tours**: Discover the rich history and culture of our surroundings.
- **Adventure Excursions**: From hiking trails to river safaris, there's always something exciting to do.
- **Shopping and Local Crafts**: Bring home a piece of tradition with locally made artifacts and souvenirs.

Our Team:
        Behind every magical experience at Palace Mario is a team of dedicated professionals who take immense pride in their work. Our staff undergo rigorous training to ensure every guest feels valued, respected, and cared for.

Future Endeavors:
        As we continue to grow, our vision remains the same: to set new standards in hospitality while staying true to our roots. We are constantly innovating, improving, and looking for ways to make your experience even better.

Your Journey Awaits:
        Whether you're here for a romantic getaway, a family holiday, or a business trip, Palace Mario is here to cater to your every need. Let us be your sanctuary, your escape, and your home away from home.

We look forward to welcoming you and creating memories that will last a lifetime.

Thank you for choosing PALACE MARIO."""
    about_us=Toplevel()
    about_us.title("ABOUT US")
    about_us.iconbitmap('apartment_naj_icon.ico')
    w = about_us.winfo_screenwidth()
    h = about_us.winfo_screenheight()
    about_us.geometry(f"{w}x{h}")
    frame=Frame(about_us)
    frame.pack(expand=True,fill=BOTH)

    scrollbar=Scrollbar(frame)
    scrollbar.pack(side=RIGHT,fill=Y)

    text_widget = Text(
        frame,
        wrap=WORD,
        yscrollcommand=scrollbar.set,
        font=("Segoe UI Emoji", 17),
        padx=10,
        pady=10,
        spacing1=5,
        spacing3=8,
    )
    text_widget.pack(fill=BOTH, expand=True)
    scrollbar.config(command=text_widget.yview)

    text_widget.insert(END, about_content)
    text_widget.config(state=DISABLED)


def on_enter(e):
    e.widget.config(bg="dark blue", fg="white")

def on_leave(e):
    e.widget.config(bg="white", fg="black")

root = Tk()
root.title("ROOM RESERVATION")
root.iconbitmap('apartment_naj_icon.ico')

w = root.winfo_screenwidth()
h = root.winfo_screenheight()
root.geometry(f"{w}x{h}")

bg_image = PhotoImage(file=r"D:\Downloads\wallhaven-0pkmgj_1550x850.png")
canvas = Canvas(root, width=w, height=h)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, anchor=NW, image=bg_image)
canvas.create_text(500, 560, text="WELCOME TO", font=("Georgia", 30), fill="grey")
canvas.create_text(500, 615, text="PALACE MARIO", font=("Georgia", 50,"italic"), fill="black")
canvas.create_text(502, 562, text="WELCOME TO", font=("Georgia", 30), fill="white")
canvas.create_text(502, 617, text="PALACE MARIO", font=("Georgia", 50,"italic"), fill="white")

button_frame = Frame(root, bg="white")
button_frame.place(relx=0, rely=0, relwidth=1, height=30)

buttons = [
    ("Menu", lambda: None),
    ("ADMIN",login_admin),
    ("CONTACT US", contact_us),
    ("ABOUT US", show_about_us),
    ("RESERVING", login),
]

for text, command in buttons:
    btn = Button(
        button_frame,
        text=text,
        compound=LEFT,  
        command=command,
        font=("Arial", 10, "bold"),
        bg="white",
        fg="black",
        relief="flat",
        activebackground="lightgrey",
        cursor="hand2",
    )
    btn.pack(side=RIGHT, padx=10, pady=5)
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

root.mainloop()
