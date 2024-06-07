import tkinter as tk
from tkinter import messagebox
from Logic import convert, convert_digits_symbols, calculate

# Function to handle conversion
def on_convert():
    try:
        nb = number_entry.get()
        b1 = float(original_base_entry.get())
        b2 = float(wanted_base_entry.get())
        result, c = convert(nb, b1, b2)
        if c:
            result_label.config(text=f"The number {nb} in base {b2} is equal to:")
            result_entry.config(state='normal')
            result_entry.delete(0, tk.END)
            result_entry.insert(0, result)
            result_entry.config(state='readonly')
        else:
            result_label.config(text="")
            messagebox.showerror("Error", "Conversion failed.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to get symbols
def on_get_symbols():
    try:
        b = float(base_entry.get())
        print(f"for base {b}, you are allowed to use the following symbols  \n", convert_digits_symbols(0, b, 1, 1))
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to get symbols (for convert interface)
def on_get_convert_symbols():
    try:
        b = float(original_base_entry.get())
        print(f"for base {b}, you are allowed to use the following symbols  \n", convert_digits_symbols(0, b, 1, 1))
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to evaluate expressions
def on_evaluate():
    try:
        expression = expression_entry.get()
        b = float(base_entry.get())
        result, c = calculate(expression, b)
        if c:
            eval_result_label.config(text="Result is:")
            eval_result_entry.config(state='normal')
            eval_result_entry.delete(0, tk.END)
            eval_result_entry.insert(0, result)
            eval_result_entry.config(state='readonly')
        else:
            eval_result_label.config(text="")
            messagebox.showerror("Error", "Evaluation failed.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Initialize the main window
root = tk.Tk()
root.title("Base Converter and Calculator")

# Function to create the convert interface
def show_convert_interface():
    clear_interface()
    tk.Label(root, text="The number").grid(row=0, column=0, pady=10)
    tk.Label(root, text="The original base").grid(row=1, column=0, pady=10)
    tk.Label(root, text="The wanted base").grid(row=1, column=2, pady=10)

    global number_entry, original_base_entry, wanted_base_entry, result_label, result_entry
    number_entry = tk.Entry(root)
    original_base_entry = tk.Entry(root)
    wanted_base_entry = tk.Entry(root)

    number_entry.grid(row=0, column=1, pady=10)
    original_base_entry.grid(row=1, column=1, pady=10)
    wanted_base_entry.grid(row=1, column=3, pady=10)

    tk.Button(root, text="Convert", command=on_convert).grid(row=2, column=1, pady=10)
    tk.Button(root, text="Get the symbols", command=on_get_convert_symbols).grid(row=2, column=3, pady=10)

    result_label = tk.Label(root, text="")
    result_label.grid(row=3, column=0, columnspan=4, pady=10)

    result_entry = tk.Entry(root, state='readonly')
    result_entry.grid(row=4, column=0, columnspan=4, pady=10)

# Function to create the calculate interface
def show_calculate_interface():
    clear_interface()
    tk.Label(root, text="The base").grid(row=0, column=0, pady=10)

    global base_entry, expression_entry, eval_result_label, eval_result_entry
    base_entry = tk.Entry(root)
    base_entry.grid(row=0, column=1, pady=10)

    tk.Button(root, text="Get the symbols", command=on_get_symbols).grid(row=1, column=1, pady=10)

    tk.Label(root, text="Expression").grid(row=3, column=0, pady=10)
    expression_entry = tk.Entry(root, width=50)
    expression_entry.grid(row=4, column=1, pady=10)

    tk.Button(root, text="Evaluate", command=on_evaluate).grid(row=5, column=1, pady=10)
    eval_result_label = tk.Label(root, text="")
    eval_result_label.grid(row=6, column=0, columnspan=4, pady=10)

    eval_result_entry = tk.Entry(root, state='readonly')
    eval_result_entry.grid(row=7, column=0, columnspan=4, pady=5)

    operations_note = tk.Label(root, text="Possible operations: +, -, *, /, ^, %", fg="blue")
    operations_note.grid(row=8, column=0, columnspan=4, pady=5)

# Function to clear the interface
def clear_interface():
    for widget in root.winfo_children():
        widget.destroy()

# Create main buttons
tk.Button(root, text="Convert", command=show_convert_interface).grid(row=0, column=0, padx=20, pady=20)
tk.Button(root, text="Calculate", command=show_calculate_interface).grid(row=0, column=1, padx=20, pady=20)

root.mainloop()
