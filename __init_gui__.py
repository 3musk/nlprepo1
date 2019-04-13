import tkinter.filedialog
from tkinter import *
from tkinter.messagebox import *


from tokenise_escape_words import TokeniseAndStopWords
from speechtotext import speechtotext

class App:
    def __init__(self, root):
        print("Welcome to NLP to SQL. Generate your SQL query from natural language\n")
        root.title('SQL Query Generator')
        #root.bind('<Return>', self.parse)

        self.sentence_frame = LabelFrame(root, text="Input Question", padx=5, pady=5)
        self.sentence_frame.pack(fill="both", expand="yes", padx=10, pady=200)

        self.input_sentence_string = StringVar()
        self.input_sentence_string.set("Enter a question in natural language...")
        self.input_sentence_entry = Entry(self.sentence_frame, textvariable=self.input_sentence_string, width=50)
        self.input_sentence_entry.pack()
        self.input_sentence_entry.bind('<Button-1>', self.clearEntry)

        self.go_button = Button(root, text="Generate Query!", command=self.lanch_parsing)
        self.go_button.pack(side="right", fill="both", expand="yes", padx=10, pady=20)

        self.reset_button = Button(root, text="Reset", fg="red", command=self.reset_window)
        self.reset_button.pack(side="right", fill="both", expand="yes", padx=10, pady=20)

    def clearEntry(self, event):
        self.input_sentence_string.set("")
    
    def reset_window(self):
        self.input_sentence_string.set("Enter a question in natural language...")
        return

    def lanch_parsing(self):
        try:

            if (str(self.input_sentence_string.get()) != "Enter a question in natural language..."):
                string=self.input_sentence_string.get()
                string.lower()
                tk_sw=TokeniseAndStopWords(string)
                tk_sw.token_and_stop_words()
                showinfo('Result', 'Parsing done!')
            else:
                showwarning('Warning', 'You must enter your question, please.')
        except Exception as e:
            showwarning('Error', e)
        return


root = Tk()
App(root)
root.resizable(width=FALSE, height=FALSE)
root.mainloop()
