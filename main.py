from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Generate Password")
window.config(padx=50,pady=50)

img = PhotoImage(file='logo.png')
canvas = Canvas(width=200,height=200)
canvas.create_image(100,100,image=img)
canvas.grid(row=0,column=1)

website_label = Label(window,text='Website name: ')
website_label.grid(row=1,column=0)

website_input = Entry(width=60,borderwidth=8,relief=FLAT)
website_input.grid(row=1,column=1,columnspan=2,pady=10,padx=15)



email_user_label = Label(window,text='Email / Username : ')
email_user_label.grid(row=2,column=0)

email_user_input = Entry(width=60,borderwidth=8,relief=FLAT)
email_user_input.grid(row=2,column=1,columnspan=2,pady=10,padx=15)





password = Label(window,text='Password : ')
password.grid(row=3,column=0)
password_out = Entry(window,width=40,borderwidth=8,relief=FLAT)
password_out.grid(row=3,column=1,pady=10)

generate_btn = Button(text='Generate',pady=5,padx=5,width=10)
generate_btn.grid(row=3,column=2)






add_btn = Button(text="Add",width=50,pady=10,padx=10)
add_btn.grid(row=4,column=1,columnspan=2,pady=10)



window.mainloop()


