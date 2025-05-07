import tkinter as tk
from tkinter import messagebox

def clear_textboxes():
    kelvin_entry.delete(0, tk.END)
    celsius_entry.delete(0, tk.END)
    fahrenheit_entry.delete(0, tk.END)

def calculate_temperatures():
    kelvin_str = kelvin_entry.get()

    if not kelvin_str:
        messagebox.showerror("Error", "Kelvin cannot be blank.")
        return

    try:
        kelvin = float(kelvin_str)
        if kelvin < 0:
            messagebox.showerror("Error", "Kelvin cannot be negative.")
            return
    except ValueError:
        messagebox.showerror("Error", "Kelvin must be a number.")
        return

    celsius = kelvin - 273.15
    fahrenheit = 9/5 * (kelvin - 273.15) + 32

    celsius_entry.delete(0, tk.END)
    fahrenheit_entry.delete(0, tk.END)

    celsius_entry.insert(0, f"{celsius:.2f}")
    fahrenheit_entry.insert(0, f"{fahrenheit:.2f}")

# Main Window Setup
window = tk.Tk()
window.title("Temperature Conversion")

# Labels
kelvin_label = tk.Label(window, text="Kelvin:")
kelvin_label.grid(row=0, column=0, sticky=tk.E, padx=5, pady=5)
celsius_label = tk.Label(window, text="Celsius:")
celsius_label.grid(row=1, column=0, sticky=tk.E, padx=5, pady=5)
fahrenheit_label = tk.Label(window, text="Fahrenheit:")
fahrenheit_label.grid(row=2, column=0, sticky=tk.E, padx=5, pady=5)

# Textboxes
kelvin_entry = tk.Entry(window)
kelvin_entry.grid(row=0, column=1, padx=5, pady=5)
celsius_entry = tk.Entry(window)
celsius_entry.grid(row=1, column=1, padx=5, pady=5)
fahrenheit_entry = tk.Entry(window)
fahrenheit_entry.grid(row=2, column=1, padx=5, pady=5)

# Buttons
calc_button = tk.Button(window, text="CALC", command=calculate_temperatures)
calc_button.grid(row=3, column=0, padx=5, pady=5)
clear_button = tk.Button(window, text="CLEAR", command=clear_textboxes)
clear_button.grid(row=3, column=1, padx=5, pady=5)

window.mainloop()