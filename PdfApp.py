import PIL as pil
import tkinter as tk
from tkinter import filedialog
from tkinter import StringVar
from PyPDF2 import PdfFileMerger
import os
from os import path

#TODO: Fix/Make an ordering system
#TODO: Display the selected files properly
#TODO: Clean up the UI
#TODO: Make it so we can merge multiple time without restarting/fix the bug where the merge duplicates the files


root = tk.Tk()

merger = PdfFileMerger()
cwd = os.getcwd()
list_of_filenames_text = StringVar()


def open_file_browser(pdf_list_text):
    filepaths = filedialog.askopenfilenames(initialdir="/home/wzhang/Documents", title="Select PDF files to merge", filetypes=[("PDF files", "*.pdf")])
    list_of_filenames_string = ""
    i = 1
    for filepath in filepaths:
        merger.append(filepath)
        list_of_filenames_string += f"{i}: {filepath.split('/')[-1]}\n"
        i += 1
    filepaths = tuple()
    pdf_list_text.set(list_of_filenames_string)


def merge_files():
    if not path.exists(f"{cwd}/output"):
        os.mkdir("./output")
    merger.write(f"./output/{filename_entry.get()}.pdf")



w = 20
h = 10

prompt = tk.Button(root, text="Select PDF files to merge", command=lambda: open_file_browser(list_of_filenames_text))
list_of_selected_file_label = tk.Label(root, text="List of selected files:")
list_of_files = tk.Label(root, textvariable=list_of_filenames_text, fg="white", bg="grey", width=w)
output_filename_label = tk.Label(root, text="Output file name:")
filename_entry = tk.Entry(root)
merge_btn = tk.Button(root, text="Merge Selected Files", command=merge_files)

for i in range(6):
    root.rowconfigure(i, weight=1, minsize=50)
    root.columnconfigure(i, weight=1)

prompt.grid(row=0)
list_of_selected_file_label.grid(row=1)
list_of_files.grid(row=2)
output_filename_label.grid(row=3)
filename_entry.grid(row=4)
merge_btn.grid(row=5)

root.mainloop()
