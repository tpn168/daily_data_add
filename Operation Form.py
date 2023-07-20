import tkinter as tk
from tkinter import ttk

def submit_form():
    print("Form submitted!")  # Modify this function to handle form submission.

def create_page(notebook, page_name):
    page = ttk.Frame(notebook)
    notebook.add(page, text=page_name)
    
    frame1 = ttk.LabelFrame(page, text="Voyage Information")
    frame1.grid(row=0, column=0, padx=10, pady=10, sticky='w')

    labels1 = ['Voyage No.', 'Load Port (ท่ารับสินค้า)', 'Discharge Port (ท่าส่งสินค้า)', 'ETA']
    for i, label in enumerate(labels1):
        ttk.Label(frame1, text=label).grid(row=i, column=0, sticky='w')
        ttk.Entry(frame1).grid(row=i, column=1)
        
    status_label = 'Status of the day'
    ttk.Label(frame1, text=status_label).grid(row=len(labels1), column=0, sticky='w')
    status_options = [
        'AT SEA SAILING LOAD (อยู่ระหว่างทางไปส่งสินค้า)',
        'AT SEA SAILING BALLAST (อยู่ระหว่างทางไปรับสินค้า)',
        'AT BERTH LOADING  (กำลังรับสินค้า)',
        'AT BERTH DISCHARGING (กำลังส่งสินค้า)',
        'AT ANCHORAGE (เรือทิ้งสมอ)',
        'OTHER [Maintenance, Drydock, etc.] (อื่นๆ)',
        'OFF HIRED (ว่างงาน)'
    ]
    status_dropdown = ttk.Combobox(frame1, values=status_options, width=60)
    status_dropdown.grid(row=len(labels1), column=1)

    frame2 = ttk.LabelFrame(page, text="Noon Report")
    frame2.grid(row=1, column=0, padx=10, pady=10, sticky='w')

    labels2 = ['M/E RPM']
    sub_labels = [
        ("Fresh Water", ['Fresh Water Consumed', 'Fresh Water Received']),
        ("MGO USED ปริมาณใช้น้ำมันMGO", ['A/E#1', 'A/E#2', 'A/E#3', 'Boiler', 
                                           'Cargo Pump' if page_name not in ['RM2', 'RM5', 'RM7'] else None, 
                                           'M/E', 'Diesel Received']),
        ("MFO USED ปริมาณใช้น้ำมันเตา", ['Boiler', 'M/E', 'MFO Received' if page_name != 'RM1' else None]),
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
            if label is not None:
                ttk.Label(frame2, text=label).grid(row=r, column=0, sticky='w')
                if (title == "MFO USED ปริมาณใช้น้ำมันเตา" and page_name in ['RM1', 'RM2', 'SM3']) or \
                   (title == "Cylinder Oil เฉพาะลำ1,5,7" and page_name in ['RM2', 'SM3']) or \
                   (label == "A/E#3" and page_name in ['SM3', 'RM5']):
                    ttk.Entry(frame2, state='disabled').grid(row=r, column=1)
                else:
                    ttk.Entry(frame2).grid(row=r, column=1)
                r += 1

    submit_button = ttk.Button(page, text="Submit", command=submit_form)
    submit_button.grid(row=2, column=0, pady=10)

root = tk.Tk()
notebook = ttk.Notebook(root)
page_names = ["RM1", "RM2", "RM5", "RM7", "SM3"]

for name in page_names:
    create_page(notebook, name)

notebook.pack(expand=1, fill="both")
root.mainloop()
