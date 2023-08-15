from tkinter import *
root = Tk()
root.geometry("500x300")

Label(root,text ="Python Registration form", font ="arial 15 bold").grid(row=0,column=3)

#Fiel name
name = Label(root, text="Name")
surname = Label(root, text="Surname")
email = Label(root, text="Email")
institution = Label(root, text="Institution")
placement = Label(root, text="Placement")

#packing fiels
name.grid(row=1,column=2)
surname.grid(row=2,column=2)
email.grid(row=3,column=2)
institution.grid(row=4,column=2)
placement.grid(row=5,column=2)

#variables for storing data
namevalue = StringVar
surnamevalue = StringVar
emailvalue = IntVar
institutionvalue = StringVar
placementvalue = StringVar


#creating entry field
nameentry = Entry(root, textvariable = namevalue)
surnameentry = Entry(root, textvariable = surnamevalue)
emailentry = Entry(root, textvariable = emailvalue)
institutionentry = Entry(root, textvariable = institutionvalue)
placemententry = Entry(root, textvariable = placementvalue)

#packing entry field
nameentry.grid(row=1,column=3)
surnameentry.grid(row=2,column=3)
emailentry.grid(row=3,column=3)
institutionentry.grid(row=4,column=3)
placemententry.grid(row=5,column=3)

#creating checkbox
btn = Button(root, text = 'Click me !', bd = '5', command = root.destroy)

# Set the position of button on the top of window.  
btn.pack(side = 'left')  
 
root.mainloop()