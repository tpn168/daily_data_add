import tkinter as tk
from tkinter import ttk

root = tk.Tk()

def submit_form():
    print("Form submitted!")  # Modify this function to handle form submission.

# Frame 1
frame1 = ttk.LabelFrame(root, text="Voyage Information")
frame1.grid(row=0, column=0, padx=10, pady=10, sticky='w')

labels1 = ['Voyage No.', 'Status of the day', 'Load Port (ท่ารับสินค้า)', 'Discharge Port (ท่าส่งสินค้า)']
for i, label in enumerate(labels1):
    ttk.Label(frame1, text=label).grid(row=i, column=0, sticky='w')
    ttk.Entry(frame1).grid(row=i, column=1)

# Frame 2
frame2 = ttk.LabelFrame(root, text="Noon Report")
frame2.grid(row=1, column=0, padx=10, pady=10, sticky='w')

labels2 = ['M/E RPM']

sub_labels = [
    ("Fresh Water", ['Fresh Water Consumed', 'Fresh Water Received']),
    ("MGO USED ปริมาณใช้น้ำมันMGO", ['A/E#1', 'A/E#2', 'A/E#3', 'Boiler', 'Cargo Pump', 'M/E', 'Diesel Received']),
    ("MFO USED ปริมาณใช้น้ำมันเตา", ['Boiler', 'M/E', 'Total MFO Used', 'MFO Received']),
    ("System Lube Oil", ['Used', 'Received']),
    ("A/E Lube. Oil", ['Used', 'Received']),
    ("Cylinder Oil เฉพาะลำ1,5,7", ['Used', 'Received']),
    ("HYD46 Hydraulic Oil", ['Used', 'Received']),
]

r = 0
for label in labels2:
    ttk.Label(frame2, text=label).grid(row=r, column=0, sticky='w')
    ttk.Entry(frame2).grid(row=r, column=1)
    r += 1

for title, labels in sub_labels:
    ttk.Label(frame2, text=title, foreground="blue", font=('Arial', 10, 'bold')).grid(row=r, column=0, sticky='w')
    r += 1
    for label in labels:
        ttk.Label(frame2, text=label).grid(row=r, column=0, sticky='w')
        ttk.Entry(frame2).grid(row=r, column=1)
        r += 1

# Submit Button
submit_button = ttk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=2, column=0, pady=10)

root.mainloop()
