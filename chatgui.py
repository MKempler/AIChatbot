import tkinter as tk
from tkinter import ttk
from chatbot import chatbot_response


class ChatApplication(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Hello")
        self.geometry("400x500")

        self.resizable(width=False, height=False)

        # Create widgets
        self.ChatLog = tk.Text(self, bd=0, bg="white", height="8", width="50", font="Arial")
        self.ChatLog.config(state=tk.DISABLED)

        self.scrollbar = tk.Scrollbar(self, command=self.ChatLog.yview, cursor="heart")
        self.ChatLog['yscrollcommand'] = self.scrollbar.set

        self.SendButton = ttk.Button(self, text="Send", command=self.send)

        self.EntryBox = tk.Text(self, bd=0, bg="lightgray",width="29", height="5", font="Arial")
        self.EntryBox.bind("<Return>", self.send)
        self.EntryBox.insert(tk.END, "Type your message here...")
        self.EntryBox.config(fg="gray")
        self.EntryBox.bind("<FocusIn>", self.remove_placeholder_text)
        self.EntryBox.bind("<FocusOut>", self.insert_placeholder_text)

        # Place widgets
        self.scrollbar.place(x=376,y=6, height=386)
        self.ChatLog.place(x=6,y=6, height=386, width=370)
        self.EntryBox.place(x=128, y=401, height=90, width=265)
        self.SendButton.place(x=6, y=401, height=90)

        self.chatbot_response("Hello! How can I assist you today?")

    def send(self, event=None):
        msg = self.EntryBox.get("1.0",'end-1c').strip()
        self.EntryBox.delete("0.0",tk.END)

        if msg != '':
            self.ChatLog.config(state=tk.NORMAL)
            self.ChatLog.insert(tk.END, "You: " + msg + '\n\n')
            self.ChatLog.config(foreground="#442265", font=("Verdana", 12 ))
        
            res = chatbot_response(msg)
            self.chatbot_response(res)
        
            self.ChatLog.config(state=tk.DISABLED)
            self.ChatLog.yview(tk.END)

    def chatbot_response(self, res):
        self.ChatLog.config(state=tk.NORMAL)
        self.ChatLog.insert(tk.END, "Bot: " + res + '\n\n')
        self.ChatLog.config(state=tk.DISABLED)
        self.ChatLog.yview(tk.END)

    def remove_placeholder_text(self, event):
        if self.EntryBox.get("1.0", "end-1c") == "Type your message here...":
            self.EntryBox.delete("1.0", tk.END)
            self.EntryBox.config(fg="black")

    def insert_placeholder_text(self, event):
        if not self.EntryBox.get("1.0", "end-1c"):
            self.EntryBox.insert(tk.END, "Type your message here...")
            self.EntryBox.config(fg="gray")

app = ChatApplication()
app.mainloop()
