import socket
from threading import Thread
from tkinter import *



client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port = 8000

client.connect((ip_address, port))
print("Connected with the server...")

class GUI:
    def __init__(self):
        self.window = Tk()
        self.window.withdraw()
        
        self.login = Toplevel()
        self.login.title("Login")
        self.login.resizable(width = False,
							height = False)
        self.login.configure(width = 400,
							height = 300)
        self.pls = Label(self.login,
					text = "Please login to continue",
					justify = CENTER,
					font = "Helvetica 14 bold")
        
        self.pls.place(relheight = 0.15,
					relx = 0.2,
					rely = 0.07)
        self.labelName = Label(self.login,
							text = "Name: ",
							font = "Helvetica 12")
        
        self.labelName.place(relheight = 0.2,
							relx = 0.1,
							rely = 0.2)
        
        self.entryName = Entry(self.login,
							font = "Helvetica 14")
        
        
        self.entryName.place(relwidth = 0.4,
							relheight = 0.12,
							relx = 0.35,
							rely = 0.2)
        
        self.entryName.focus()
        
        self.go = Button(self.login,
						text = "CONTINUE",
						font = "Helvetica 14 bold",
						command = lambda: self.goAhead(self.entryName.get()))
        
        self.go.place(relx = 0.4,
					rely = 0.55)
        
        self.window.mainloop()
        
    def goAhead(self, name):
        self.login.destroy()
        self.layout(name)
        rcv = Thread(target=self.receive)
        rcv.start()
	self.layout(name)

   
  

    def receive(self):
        while True:
            try:
                message = client.recv(2084).decode('utf-8')
                if message == 'NICKNAME':
                    client.send(self.name.encode('utf-8'))
                else:
                    pass

            except:
                print('An error has occured')
                client.close()
                break
    def layout(self,name):
	self.name = name
	self.Window.deiconify()
	self.Window.title('CHAT ROOM')
	self.Window.resizeable(width=False, height = False)
	self.Window.configure(width = 470, height= 550, bg = '#17202A')
	
g = GUI()

