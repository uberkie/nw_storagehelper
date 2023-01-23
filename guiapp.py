import tkinter as tk
from tkinter import messagebox
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from tkinter import *

# Create the main window
root = tk.Tk()
root.title("NW Storage")
#sets the position of the main window 

root.attributes("-alpha", 0.7)
root.focus_set()
root.geometry('500x350+1100+50')
root.update_idletasks()



# Read the xlsx file into a pandas dataframe
df = pd.read_excel("storage.xlsx")

# Create a label and entry widget for the search query
query_label = tk.Label(root, text="Search Query:")
query_label.grid(row=0, column=0)
query_label.place(height=40, width=100)
query_entry = tk.Entry(root)
query_entry.grid(row=0, column=1)
query_entry.place(height=30, width=100,x=100,y=2)

def search():
    # Get the search query
    query = query_entry.get()
    if query == [int]:
        columns_to_search = ["Name", "CON", "STR", "DEX", "INT", "FOC", "Perks", "BoE", "BoP"]
        filtered_df = df.copy()
        for col in columns_to_search:
            filtered_df = filtered_df[filtered_df[col] == int(query)]
    else:
        # Filter the dataframe based on the query
        colm = ["Name", "CON", "STR", "DEX", "INT", "FOC", "BoE", "BoP"]
        for colms in colm:
            filtered_df = df[(df['Perks'].str.contains(query, case=False)) | (df['Type'].str.contains(query, case=False) | (df['Name'].str.contains(query, case=False)))]
            # Clear the text widget
            result_text.delete("1.0", tk.END)


    # Insert the filtered data into the text widget
            for index, row in filtered_df.iterrows():
                result_text.insert(tk.END, f"Storage: {row['Storage']}\n")
                result_text.insert(tk.END, f"Type: {row['Type']}\n")
                result_text.insert(tk.END, f"Tier: {row['Tier']}\n")
                result_text.insert(tk.END, f"Class: {row['Class']}\n")
                result_text.insert(tk.END, f"Name: {row['Name']}\n")
                result_text.insert(tk.END, f"Gearscore: {row['Gearscore']}\n")
                result_text.insert(tk.END, f"CON: {row['CON']}\n")
                result_text.insert(tk.END, f"STR: {row['STR']}\n")
                result_text.insert(tk.END, f"DEX: {row['DEX']}\n")
                result_text.insert(tk.END, f"INT: {row['INT']}\n")
                result_text.insert(tk.END, f"FOC: {row['FOC']}\n")
                result_text.insert(tk.END, f"Perks: {row['Perks']}\n")
                result_text.insert(tk.END, f"BoE: {row['BoE']}\n")
                result_text.insert(tk.END, f"BoP: {row['BoP']}\n")
                result_text.insert(tk.END, "\n")
                
# Create a text widget to display the data

                
search_button = tk.Button(root, text="Search", command=search)
search_button.grid(row=0, column=1)
root.columnconfigure(2, weight=1)
search_button.place(height=30, width=100,x=210,y=2)

# Create a text widget to display the search results
result_text = tk.Text(root)
result_text.grid(row=1, column=0, columnspan=1)
result_text.place(width=350, height=200,x=10,y=100)

root.mainloop()
