from tkinter import *
from tkinter import messagebox
import base64


def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)

def savefiles():
    ttl=entr1.get()
    written=txt1.get("1.0",END)
    secr=entr2.get()

    if len(ttl)==0 or len(written)==0 or len(secr)==0:
        messagebox.showinfo(title="ERROR",message="Fill all the blanks")

    else:
        message=encode(secr,written)
        try:
            with open("secret.txt","a") as newfile:
                newfile.write(f"\n{ttl}\n{message}")

        finally:
            entr1.delete(0,END)
            txt1.delete("1.0",END)
            entr2.delete(0,END)


def decryp():
    message=txt1.get("1.0",END)
    secr=entr2.get()

    if len(message)==0 or len(secr)==0:
        messagebox.showinfo(title="error",message="missing information")
    else:
        try:
            decryp=decode(secr,message)
            txt1.delete("1.0",END)
            txt1.insert("1.0",decryp)

        except:
            messagebox.showinfo(title="error",message="try again")


#uı

wndw=Tk()
wndw.title("secret notes")
wndw.config(padx=30,pady=30)

#görsel
photo=PhotoImage(file="img.png")
photolbl=Label(image=photo)
photolbl.pack()
#label
lbl1=Label(text="Enter title:",font=("Ariel",20,"normal"))
lbl1.pack()
#entry
entr1=Entry(width=20)
entr1.pack()
#label
lbl2=Label(text="Enter your secret note:",font=("Ariel",20,"normal"))
lbl2.pack()
#text
txt1=Text(width=30,height=10)
txt1.pack()

#label

lbl3=Label(text="Enter the key:",font=("Ariel",20,"normal"))
lbl3.pack()

#entry
entr2=Entry(width=30)
entr2.pack()

#button
bttn1=Button(text="SAVE",command=savefiles)
bttn1.pack()
#button
bttn2=Button(text="Solve",command=decryp)
bttn2.pack()




wndw.mainloop()