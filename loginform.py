import ast
import customtkinter 
from tkinter import messagebox
from tkinter import *

customtkinter.set_appearance_mode("dark")
# customtkinter.set_default_color_theme("blue")
def signin(): #main sign in function..
    root=customtkinter.CTk()
    root.wm_iconbitmap("D:/custom tkinter/login-project/signin.ico")
    root.title("Sign-in")
    root.geometry("900x600")

    # ---------------------------------------signup------------------------------
    def signup():
        root=customtkinter.CTk()
        root.iconbitmap("D:/custom tkinter/login-project/signin.ico") #icon

        # -----------------------------------------------------logic---------------------------------
        def againsign(): #if sign-in button is pressed in sign-up page 
            root.destroy()
        def sign_up_verify(): #logic for sign-up button..
            username=name_entry.get()
            password=password_entry.get()
            pass_confirm=password_confirm_entry.get()
           
            if password !="" and password == pass_confirm and username !="" :
              
                try:
                   file=open("data.txt","r+")
                   d=file.read()
                   r=ast.literal_eval(d)
                   dict2={username:password}
                   if username in r.keys(): #if user is present then it will show error.
                       messagebox.showinfo("Error","This user is present,Chose another one.Thanks!!")
                   else: #Otherwise it will add it to database.
                        r.update(dict2)
                        print(r)
                        file.truncate(0)
                        file.close()
                        messagebox.showinfo("Welcome","you have succesfully Signed Up.")
                        root.destroy() 

                   flie_write=open("data.txt","w")
                   w=flie_write.write(str(r))
                   flie_write.close()
                   print(r.keys())
                   print(r.values())
                except: #if file donot exist
                   file=open("data.txt","w")
                   data=str({username:password})
                   file.write(data)
                   file.close()
            else:
                messagebox.showerror("Error","Both passwords should same...")
        # --------------------------------------------design---------------------------------------------------
      

        
        root.title("Sign-up")
        root.geometry("900x600")
        frame=customtkinter.CTkFrame(master=root,
                height=450,
                width=400,
                corner_radius=10,
                )
        frame.place(x=250,y=60)

        label=customtkinter.CTkLabel(master=frame,
                                    text="Sign Up",
                                    font=("Calibri",50,"bold"),
                                    text_color="yellow")
        label.place(x=130,y=10)

        name_entry=customtkinter.CTkEntry(master=frame,
                                        height=30,
                                        width=200,
                                        corner_radius=10,
                                        placeholder_text="Name",
                                        placeholder_text_color="grey")
        name_entry.place(x=100,y=100)

        password_entry=customtkinter.CTkEntry(master=frame,
                                        height=30,
                                        width=200,
                                        corner_radius=10,
                                        placeholder_text="Password",
                                        placeholder_text_color="grey")
        password_entry.place(x=100,y=150)

        password_confirm_entry=customtkinter.CTkEntry(master=frame,
                                        height=30,
                                        width=200,
                                        corner_radius=10,
                                        placeholder_text="Confirm Password",
                                        placeholder_text_color="grey")
        password_confirm_entry.place(x=100,y=200)

        butoon3=customtkinter.CTkButton(master=frame,
                                    text="Sign up",
                                    width=200,fg_color="#2b2b2b",
                                    hover_color="green",
                                    border_width=1,command=sign_up_verify)
        butoon3.place(x=100,y=250)


        label=customtkinter.CTkLabel(master=frame,
                                    text=" I have an account?",
                                    font=("halvatica",15))
        label.place(x=100,y=290)

        butoon4=customtkinter.CTkButton(master=frame,
                                    text="Sign-in",text_color="#15d8e6",
                                    
                                    width=30,
                                    font=("Noto Serif",15,"underline"),
                                    hover_color="#2a2b3b",
                                    fg_color="#2b2b2b",command=againsign)
        butoon4.place(x=230,y=290)
        root.mainloop()
# ------------------------------signin-------------------------------------
    def verify():
        username=name_entry.get()
        password=password_entry.get()
            
            #Opening file for sign-in
        try:
            file=open("data.txt")
            f=file.read()
            r=ast.literal_eval(f)
            file.close()

            if username in r.keys() and password==r[username]:
                messagebox.showinfo("Welcome","Singed in succesfully!")
                # --------new window for just fun..................
                main=Toplevel()
                main.geometry("900x600")
                Label(main,text="Welcome back!",font="halvatica 30 bold").pack(anchor=CENTER)
                main.mainloop()
                # --------------------------------------------------
            else:
                messagebox.showerror("Error","Provided Information is not present in our records")
        except:
            messagebox.showinfo("Invalid Information","Your credentials are not present in our records.I hope you have to Sign-Up ")
    frame=customtkinter.CTkFrame(master=root,
                height=450,
                width=400,
                corner_radius=10,
                )
    frame.place(x=250,y=60)

    label=customtkinter.CTkLabel(master=frame,
                                text="Sign In",
                                font=("Calibri",50,"bold"),
                                text_color="yellow")
    label.place(x=130,y=10)

    name_entry=customtkinter.CTkEntry(master=frame,
                                    height=30,
                                    width=200,
                                    corner_radius=10,
                                    placeholder_text="Name",
                                    placeholder_text_color="grey")
    name_entry.place(x=100,y=100)

    password_entry=customtkinter.CTkEntry(master=frame,
                                    height=30,
                                    width=200,
                                    corner_radius=10,
                                    placeholder_text="Password",
                                    placeholder_text_color="grey")
    password_entry.place(x=100,y=170)

    butoon=customtkinter.CTkButton(master=frame,command=verify,
                                text="Sign-in",
                                width=200,fg_color="#2b2b2b",
                                hover_color="green",
                                border_width=1)
    butoon.place(x=100,y=230)


    label=customtkinter.CTkLabel(master=frame,
                                text="Don't have an account?",
                                font=("halvatica",15))
    label.place(x=100,y=270)

    butoon2=customtkinter.CTkButton(master=frame,
                                text="Sign-up",text_color="#15d8e6",
                                
                                width=30,
                                font=("Noto Serif",15,"underline"),
                                hover_color="#2a2b3b",
                                fg_color="#2b2b2b",command=signup)
    butoon2.place(x=255,y=270)
    root.mainloop()
signin()