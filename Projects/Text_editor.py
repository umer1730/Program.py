import tkinter as tk
from tkinter import filedialog, messagebox

def new_file(): # 1.0 ka matlab pehli line ka pehla word and tk.end  mean end tk
    text.delete(1.0, tk.END)  # when user want to make new file delete text box

def open_file(): # if user want to work in existing file then user enter file path
    file_path = filedialog.askopenfile(defaultextension= ".txt", filetypes = [("Text Files","*.txt" )])  # txt isliye ta ke koi aur na khul jae like png
    if file_path:
        with open(file_path, "r") as file: # phir hm check kre ga ke file path empty ha ke nahi agr empty nahi ha to hm with open statement se file ko read mode me open kre ga aur uska context text box me insert krde ga
             text.delete(1.0, tk.END)   
             text.insert(tk.END, file.read())    # agr file me hm add krna chahe agr empty na ho

def save_file():  # if user want to save file
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files","*.txt")])  
    if file_path:
        with open(file_path, "w") as file: # ab hm check kre ga ke text file empty ha ya nahi agr empty nahi ha to hm with open statement se text ko write mode me convert krde ga aur isme text box ka content include krde ga
            file.write(text.get(1.0, tk.END))
            messagebox.showinfo("Info", "File saves succssfully!")  # tell file save 
root = tk.Tk()
root.title("Simple Text Editor")  # make window
root.geometry("800x600") # give size

menu = tk.Menu(root)  # menu me hm file menu btae ge that new open and save ho ga
root.config(menu=menu)
file_menu= tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

text = tk.Text(root,wrap=tk.WORD, font = ("Helvetica",12), fg="blue")
text.pack(expand=tk.YES, fill=tk.BOTH)
root.mainloop() # user input ko chlae ga aur input ko screen pr show kre ga