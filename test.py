import tkinter as tk

root = tk.Tk()
root.geometry('800x500')
root.title("TEST PLATFORM")
label_list = ['Cliente:', 'Responsavel por Teste:', 'Nome do Sistema:', 'Ref:', 'Data Base:', 'Data Teste:']
entry_list = []

# Row and Column configure to manage weights
root.columnconfigure(0, weight=1)
root.columnconfigure(2, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(2, weight=1)

# Add a frame to hold the rest of the widgets and place that frame in the row/column without a weight.
# This will allow us to center everything that we place in the frame.
frame = tk.Frame(root)
frame.grid(row=1, column=1)

# use a loop to create our widgets.
for ndex, label in enumerate(label_list):
    tk.Label(frame, text=label, font='10').grid(row=ndex, column=0, sticky='w')
    # Store the entry widgets in a list for later use
    entry_list.append(tk.Entry(frame, borderwidth=2, width=30))
    entry_list[-1].grid(row=ndex, column=1)

# Get and print each entry value.
def print_entries():
    for entry in entry_list:
        print(entry.get())


tk.Button(frame, text='Selecionar Arquivo', command=print_entries).grid(row=len(label_list)+1, column=0, columnspan=2)
root.mainloop()