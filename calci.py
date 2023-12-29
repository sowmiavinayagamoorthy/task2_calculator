import tkinter as tk
from tkinter import messagebox

def button_click(symbol):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + str(symbol))

def clear_entry():
    entry.delete(0, tk.END)

def delete_single():
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text[:-1])

def calculate():
    expression = entry.get()
    try:
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
        history_text.insert(tk.END, f"{expression} = {result}\n")
    except Exception as e:
        messagebox.showerror("Error", "Invalid expression. Please enter a valid mathematical expression.")

def clear_history():
    history_text.delete(1.0, tk.END)

# Create the main window
window = tk.Tk()
window.title("Advanced Calculator")

# Create entry widget for expression and result
entry = tk.Entry(window, width=20, justify="right", font=("Arial", 14))
entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# Define colors
number_button_color = "#FFFFFF"                                          #aaffaa  # Light green for numbers
symbol_button_color = "#CCCCCC"           #ffaaaa  # Light red for symbols
symbol_button_equals = "#ADD8E6"
symbol_button_clear = "#ADD8E6"
symbol_button_del = "#ADD8E6"
# Create number buttons (0-9)
for i in range(1, 10):
    tk.Button(window, text=str(i), command=lambda i=i: button_click(i), width=5, height=2, bg=number_button_color, fg="#000000").grid(row=(i-1) // 3 + 1, column=(i-1) % 3, padx=5, pady=5)

# Create zero button
tk.Button(window, text="0", command=lambda: button_click(0), width=5, height=2, bg=number_button_color).grid(row=4, column=1, padx=5, pady=5)

# Create operation buttons (+, -, *, /)
operations = ['+', '-', '*', '/']
row_index = 1
col_index = 3
for operation in operations:
    symbol_color = symbol_button_color if operation in ['+', '*'] else "#aaaaff"  # Light blue for -, /
    tk.Button(window, text=operation, command=lambda operation=operation: button_click(operation), width=5, height=2, bg=symbol_color).grid(row=row_index, column=col_index, padx=5, pady=5)
    row_index += 1

# Create other buttons (clear, del, point, equals)
tk.Button(window, text="C", command=clear_entry, width=5, height=2, bg=symbol_button_clear).grid(row=4, column=0, padx=5, pady=5)
tk.Button(window, text="Del", command=delete_single, width=5, height=2, bg=symbol_button_del).grid(row=5, column=1, padx=5, pady=5)
tk.Button(window, text=".", command=lambda: button_click("."), width=5, height=2, bg=number_button_color).grid(row=4, column=2, padx=5, pady=5)
tk.Button(window, text="=", command=calculate, width=5, height=2, bg=symbol_button_equals).grid(row=5, column=0, padx=5, pady=5)

# Create history text widget
history_text = tk.Text(window, height=5, width=30)
history_text.grid(row=6, column=0, columnspan=4, padx=5, pady=5)

# Create clear history button
tk.Button(window, text="Clear History", command=clear_history, width=15, bg="#cccccc").grid(row=7, column=0, columnspan=4, padx=5, pady=5)

# Run the Tkinter event loop
window.mainloop()







