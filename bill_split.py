import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Bill Split Calculator")
root.geometry("350x430")
root.configure(bg="#F0F4F8")
root.resizable(False, False)

tk.Label(root, text="Bill Split Calculator",
         font=("Arial", 18, "bold"),
         bg="#F0F4F8", fg="#2563EB").pack(pady=15)

def field(text):
    tk.Label(root, text=text, bg="#F0F4F8").pack()
    e = tk.Entry(root, font=("Arial", 12))
    e.pack(pady=5)
    return e

bill = field("Total Bill (₹)")
people = field("Number of People")
tip = field("Tip Percentage (%)")

result = tk.Label(root, text="Enter details and calculate",
                  bg="#F0F4F8", font=("Arial", 11),
                  justify="left")
result.pack(pady=15)

def calculate():
    try:
        b = float(bill.get())
        p = int(people.get())
        t = float(tip.get())

        if b <= 0 or p <= 0 or t < 0 or t > 100:
            raise ValueError

        tip_amount = b * t / 100
        total = b + tip_amount
        each = total / p

        result.config(text=f"Tip: ₹{tip_amount:.2f}\n"
                           f"Final Bill: ₹{total:.2f}\n"
                           f"Each Person: ₹{each:.2f}")

    except ValueError:
        messagebox.showerror(
            "Error",
            "Enter valid values!\nBill and people must be positive.\nTip: 0-100%"
        )

def reset():
    bill.delete(0, tk.END)
    people.delete(0, tk.END)
    tip.delete(0, tk.END)
    result.config(text="Enter details and calculate")

tk.Button(root, text="Calculate Bill", command=calculate,
          bg="#2563EB", fg="white", width=18).pack(pady=5)

tk.Button(root, text="Reset", command=reset,
          width=18).pack(pady=5)

root.mainloop()