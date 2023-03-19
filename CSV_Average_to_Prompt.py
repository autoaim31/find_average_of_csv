import tkinter as tk
from tkinter import filedialog as fd
import pandas as pd

root= tk.Tk()
root.title('Average')
root.geometry('300x300')

file_name = fd.askopenfilename(title="Select file", filetypes=(("CSV Files","*.csv"),))
                   
if file_name:
    csv = pd.read_csv(file_name)
    means = csv.mean(axis=0)
    final_string = "What should I do?"
    measure_mean_dict = means.to_dict()
    for measure, mean in measure_mean_dict.items():
        final_string = "My average " + str(measure) + " is " + str(mean) + ". " + final_string
    text = tk.Text(root, wrap=tk.WORD)
    text.insert(tk.INSERT, final_string)
    text.pack()

else:
    text = tk.Text(root, wrap=tk.WORD)
    text.insert(tk.INSERT, "No File Read")
    text.pack()

root.mainloop()
