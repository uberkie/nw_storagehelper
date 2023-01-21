import tkinter as tk
from tkinter import messagebox
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

# Create the main window
root = tk.Tk()
root.title("Excel Editor")

# Read the xlsx file into a pandas dataframe
df = pd.read_excel("storage.xlsx")

# Create a label and entry widget for the search query
query_label = tk.Label(root, text="Search Query:")
query_label.grid(row=0, column=0)
query_entry = tk.Entry(root)
query_entry.grid(row=0, column=1)

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
            filtered_df = df[(df['Perks'].str.contains(query, case=False)) | (df['Weptype'].str.contains(query, case=False) | (df['Name'].str.contains(query, case=False)))]
            # Clear the text widget
            result_text.delete("1.0", tk.END)


    # Insert the filtered data into the text widget
            for index, row in filtered_df.iterrows():
                result_text.insert(tk.END, f"Storage: {row['Storage']}\n")
                result_text.insert(tk.END, f"Weptype: {row['Weptype']}\n")
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
search_button.grid(row=0, column=2)

# Create a text widget to display the search results
result_text = tk.Text(root)
result_text.grid(row=1, column=0, columnspan=3)
                
                
## new window
def open_window_2():
    window_2 = tk.Toplevel(root)
    window_2.title("Title 2")
    # Create a label to display "Hello world2"

# Create Entry widgets for row, column, and new value
row_label = tk.Label(root, text="Enter Row Index:")
row_label.grid(row=2, column=0)
row_entry = tk.Entry(root)
row_entry.grid(row=2, column=1)

column_label = tk.Label(root, text="Enter Column:")
column_label.grid(row=3, column=0)
column_entry = tk.Entry(root)
column_entry.grid(row=3, column=1)

value_label = tk.Label(root, text="Enter New Value:")
value_label.grid(row=4, column=0)
value_entry = tk.Entry(root)
value_entry.grid(row=4, column=1)
def update_cell():
    # Get the row and column indexes from the user input
    row = int(row_entry.get())
    column = column_entry.get()

    # Get the new value from the user input
    new_value = value_entry.get()

    try:
        # Update the cell in the DataFrame
        df.at[row, column] = new_value

        # Write the changes to the original xlsx file
        df.to_excel('file.xlsx', index=False)
        messagebox.showinfo("Success", "Data has been updated Successfully.")
    except:
        messagebox.showerror("Error", "Data could not be updated.")
# Create update button
update_button = tk.Button(root, text="Update", command=update_cell)
update_button.grid(row=3, column=2)





root.mainloop()