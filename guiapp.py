import tkinter as tk
import tkinter.ttk as ttk
import sqlite3
import tkinter.simpledialog as simpledialog

root = tk.Tk()

# Connect to the database
conn = sqlite3.connect("newworld.db")
cursor = conn.cursor()

# Fetch the data
cursor.execute("SELECT * FROM storage")
data = cursor.fetchall()

# Set up the treeview widget
tree = ttk.Treeview(root,
                    columns=["id", "Storage", "Type", "Tier", "Class", "Name", "Gearscore", "CON", "STR", "DEX", "INT",
                             "FOC", "Perks", "BoE", "BoP"], show="headings")

tree.heading("id", text="id", anchor="center")
tree.heading("Storage", text="Storage", anchor="center")
tree.heading("Type", text="Type")
tree.heading("Tier", text="Tier")
tree.heading("Class", text="Class")
tree.heading("Name", text="Name")
tree.heading("Gearscore", text="Gearscore")
tree.heading("CON", text="CON")
tree.heading("STR", text="STR")
tree.heading("DEX", text="DEX")
tree.heading("INT", text="INT")
tree.heading("FOC", text="FOC")
tree.heading("Perks", text="Perks")
tree.heading("BoE", text="BoE")
tree.heading("BoP", text="BoP")
tree.column("id", width=100, stretch=False)
tree.column("Storage", width=100, stretch=False)
tree.column("Type", width=100, stretch=False, anchor="center")
tree.column("Tier", width=100, stretch=False, anchor="center")
tree.column("Class", width=100, stretch=False, anchor="center")
tree.column("Name", width=100, stretch=False, anchor="center")
tree.column("Gearscore", width=100, stretch=False, anchor="center")
tree.column("CON", width=100, stretch=False, anchor="center")
tree.column("STR", width=100, stretch=False, anchor="center")
tree.column("DEX", width=100, stretch=False, anchor="center")
tree.column("INT", width=100, stretch=False, anchor="center")
tree.column("FOC", width=100, stretch=False)
tree.column("Perks", width=100, stretch=False, anchor="center")
tree.column("BoE", width=100, stretch=False, anchor="center")
tree.column("BoP", width=100, stretch=False, anchor="center")

# Insert the data into the treeview
for index, row in enumerate(data):
    tree.insert("", index, text=str(index), values=row)

# Add a search entry widget
label_entry = tk.Label(root, text="Search for something")
label_entry.pack()
search_var = tk.StringVar()
entry = tk.Entry(root, textvariable=search_var)
entry.pack()


def search():
    # Get the search term and split it by the delimiter of "+"
    search_terms = search_var.get().lower().split("+")

    # Clear the treeview
    for item in tree.get_children():
        tree.delete(item)

    # Search for items that match all of the search terms
    for index, row in enumerate(data):
        if all([any([search_term in str(x).lower() for x in row]) for search_term in search_terms]):
            tree.insert("", index, text=str(index), values=row)


label2_entry = tk.Label(root, text="Search for 2 things")
label2_entry.pack()


# Create a sorting function
def sort_tree(tree, col, reverse):
    l = [(tree.set(k, col), k) for k in tree.get_children('')]
    l.sort(reverse=reverse)

    for index, (val, k) in enumerate(l):
        tree.move(k, '', index)

    tree.heading(col, command=lambda: sort_tree(tree, col, not reverse))


# Sort the Treeview in ascending order
sort_tree(tree, "Storage", False)
sort_tree(tree, "Type", False)
sort_tree(tree, "Tier", False)
sort_tree(tree, "Class", False)
sort_tree(tree, "Name", False)
sort_tree(tree, "Gearscore", False)
sort_tree(tree, "CON", False)
sort_tree(tree, "STR", False)
sort_tree(tree, "DEX", False)
sort_tree(tree, "INT", False)
sort_tree(tree, "FOC", False)
sort_tree(tree, "Perks", False)
sort_tree(tree, "BoE", False)
sort_tree(tree, "BoP", False)

# Call the search function when the user types in the search bar
entry.bind("<Key>", lambda event: search())


def update_database(item, column, new_value):
    # Update the database
    cursor.execute("UPDATE storage SET {}=? WHERE ID=?".format(column), (new_value, item))
    conn.commit()
    cursor.execute("SELECT * FROM storage")


def delete_data():
    # Get the selected row
    selected_item = tree.selection()[0]
    uid = tree.item(selected_item)['values'][0]

    # Delete the selected row from the database
    del_query = "DELETE FROM  storage WHERE id=?"
    sel_data = (uid,)
    conn.execute(del_query, sel_data)
    conn.commit()

    # Delete the selected row from the treeview
    tree.delete(selected_item)


# Add a button to delete the selected row
delete_button = tk.Button(root, text="Delete", command=delete_data)
delete_button.pack()

tree.pack()

root.mainloop()
