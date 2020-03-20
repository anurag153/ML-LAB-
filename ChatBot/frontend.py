import bot
master = tk.Tk()
def ask():
    query=textF.get()
    chat=bot.Chat(bot.pairs, bot.reflections)
    answer=chat.respond(query)
    msg.insert(tk.END, "You : " +query)
    msg.insert(tk.END, "Neel : " + answer)
    textF.delete(0,tk.END)
    
def userText(event):
    textF.delete(0,tk.END)
    
    
master.title("ChatBot")
master.geometry("500x900")

img=ImageTk.PhotoImage(Image.open(r"D:\images.jpg"))
photo=tk.Label(master, image=img,width=700,height=180)
photo.grid(column=1,row=1)
photo.pack(pady=10)
master.configure(bg='white')
frame=tk.Frame(master)
sc=tk.Scrollbar(frame)
msg=tk.Listbox(frame, width=65, height=25,fg='black')
msg.configure(bg='white')
sc.pack(side=tk.RIGHT, fill=tk.Y)
msg.pack(side=tk.LEFT, fill=tk.BOTH, pady=5)
frame.pack()
textF=tk.Entry(master, font=("Volkhov", 12),fg='dimgrey',bg="#FFFFFF",width=60)
textF.insert(1,"")
textF.bind("<Button>",userText)
textF.pack(pady=20)
button =tk.Button(master,
                   text="Enter",
                   fg="black",
                   command=ask)
button.pack()
master.mainloop()