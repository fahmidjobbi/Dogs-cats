from re import T
import tkinter as tk
from PIL import Image,ImageTk
from email.message import Message
from timeit import repeat
import tkinter
import tkinter.messagebox
import customtkinter
from tkinter import Tk, Frame, Menu, ttk,Toplevel
from PIL import Image,ImageTk
import os
import tkinter.filedialog as filedialog
import numpy as np
import joblib as joblib
import pandas as pd 
from keras.models import load_model
#kkkkkk

#create the main window

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

print('hello')
class App(customtkinter.CTk):

    WIDTH = 780
    HEIGHT = 520

    def __init__(self):
        super().__init__()
        self.filename = None

        self.title("Cats&dogs")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed
        vo= str(os.path.abspath(os.getcwd()))+r'\cat.ico'
        self.iconbitmap(vo)
       
        

        # ============ create two frames ============

        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # ============ frame_left ============

        # configure grid layout (1x11)
        self.frame_left.grid_rowconfigure(0, minsize=10)   # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(5, weight=1)  # empty row as spacing
        self.frame_left.grid_rowconfigure(8, minsize=20)    # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing
    
        # ============ frame_right ============
        
        self.button_1 = customtkinter.CTkButton(master=self.frame_left,
                                                text ='Choose a picture', 
                                                command=self.open_img)
                                               
        self.button_1.grid(row=1, column=0, pady=10, padx=20)
        self.button_2 = customtkinter.CTkButton(master=self.frame_left,
                                                text ='Dog or Cat?', 
                                                command=self.result)
                                               
        self.button_2.grid(row=5, column=0, pady=10, padx=20)
        
      
        
     
        
        
    def on_closing(self,event=0):
    #delete tmp files if exist  
    #delete tmp files if exist
       
   
        # directory
        dir = str(os.path.abspath(os.getcwd()))+r'\tmp'
   
        # path
        try:
            for file in os.scandir(dir):
                os.remove(file.path)
       
        except:
            pass
       
        if tkinter.messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.destroy()
            
    
 
    def open_img(self):
        try:
          
            self.filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
            self.img = Image.open(self.filename)
            self.img = self.img.resize((300, 300), Image.ANTIALIAS)
            self.img = ImageTk.PhotoImage(self.img)
            self.panel = tk.Label(self.frame_left, image = self.img)
            self.panel.grid(row=2, column=0, pady=10, padx=20)
            
            
        except:
            pass
            
          
            
     
    
    def result(self):
        classifer = self.classify(self.filename)

        
        self.label = customtkinter.CTkLabel(master=self.frame_right, text=classifer, foreground='green',width=350, 
                                            height=380,bg_color='white',corner_radius=10,text_color='green',
                                            anchor='center',text_font=('Arial', 30, 'bold'))
                                            
     
                                           
      
        self.label.grid(row=4, column=1, pady=10, padx=20)
        
        
    def prob(self,pred):
        if pred>0.5 :
            pred=1
        else:
            pred=0
        return pred
  
    def classify(self,filename):
        model = load_model('model1_catsVSdogs_10epoch.h5')
        #dictionary to label all traffic signs class.
        classes = { 
        1:'its a cat',
        0:'its a dog',
 
        }
        global label_packed
        image = Image.open(filename)
        image = image.resize((64,64))
        image = np.expand_dims(image, axis=0)
        image = np.array(image)
        image = image/255
        pred = model.predict([image])[0]
        classes_x=self.prob(pred[0])
        sign = classes[classes_x]
        print(sign)
        
 
       
        return sign


# ============ main ============
            

class Example(Frame):
    
        def __init__(self):
            super().__init__()

            self.initUI()


        def initUI(self):

            self.master.title("Cats&dogs")

            menubar = Menu(self.master)
            self.master.config(menu=menubar)

            fileMenu = Menu(menubar)
            fileMenu.add_command(label="Exit", command=self.onExit)
            menubar.add_cascade(label="File", menu=fileMenu)
            
            editMenu = Menu(menubar)
            editMenu.add_command(label="Undo")
            editMenu.add_separator()
            editMenu.add_command(label="Cut")
            editMenu.add_command(label="Copy")
            editMenu.add_command(label="Paste")
            editMenu.add_separator()
            editMenu.add_command(label="Select All")
            menubar.add_cascade(label="Edit", menu=editMenu)
          
            
            helpMenu = Menu(menubar)
            helpMenu.add_command(label="About", command=self.onAbout)
            menubar.add_cascade(label="Help", menu=helpMenu)
            
            
          
            
            
            #set HTML content
            
            #print(frame.html.cget("zoom"))           

            #frame.load_website("https://app.powerbi.com/reportEmbed?reportId=e7a66a17-9821-4656-966b-b6e21a4b8ed6&autoAuth=true&ctid=889cdbee-d881-42dc-bd06-ad3237c34a53&config=eyJjbHVzdGVyVXJsIjoiaHR0cHM6Ly93YWJpLXNvdXRoLWFmcmljYS1ub3J0aC1hLXByaW1hcnktcmVkaXJlY3QuYW5hbHlzaXMud2luZG93cy5uZXQvIn0%3D") #load a website
        
            #frame.pack(fill="both", expand=True) #attach the HtmlFrame widget to the parent window
            
            

            
           
        
            


        def onExit(self):

            self.quit()   
            
        

        
        ## FUNCTION TO SHOW ABOUT DIALOG     
        def onAbout(self):
            new_window=Toplevel(self.master)
            new_window.geometry("800x400+50+50")
            new_window.attributes('-alpha', 1)
            new_window.title("About")
            new_window.resizable(False,False)
            lbl=customtkinter.CTkLabel(master=new_window,
                                                   text=
                                                   '''Auteur : FAHMI DJOBBI \n \n \t'''+
                                                    '''Version : 1.0 \n \n \t''',


                                                   
                                                   height=150,
                                                   fg_color=("yellow"),  #<- custom tuple-color
                                                   justify="left",
                                                   )

            lbl.grid(row=0, column=0, columnspan=2, pady=10, padx=20, sticky="we")
            lbl.configure(font=("Arial", 9, "bold"))

             
 
 
 
 
 
 
 ######################### END  APP ###################################               

if __name__ == "__main__":
    app = App()
    app1=Example()
    app.mainloop()