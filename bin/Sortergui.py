import tkinter as tk


# function called when the button is pressed
def callsort():
    enterdpath = ent_path.get()

    #adds the sorting path
    lbl_result["text"] = "Sorting in: "+enterdpath

    #writes the path to the pathbase file
    fo=open("pathbase.txt",'w')
    fo.write(enterdpath)
    fo.close()

    #runs sorter
    import sorter

    lbl_result["text"] = "Sorted"


window = tk.Tk()
window.title("Sorter")

# widget definations
frm_entry = tk.Frame(master=window)
ent_path = tk.Entry(master=frm_entry, width=50)
lbl_pathenter = tk.Label(master=frm_entry, text="Path:")
lbl_result = tk.Label(master=window, text="")
lbl_credit = tk.Label(master=window, text="- Subh Chaturvedi")


# button defination
btn_sort = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=callsort
)


# placing widgets
ent_path.grid(row=0, column=1, sticky="e")
lbl_pathenter.grid(row=0, column=0, sticky="w")
frm_entry.grid(row=0, column=0, padx=10)
btn_sort.grid(row=0, column=1, pady=10, padx=10)
lbl_result.grid(row=1, column=0, padx=10)
lbl_credit.grid(row=2, column=1, padx=8)
   
window.mainloop()