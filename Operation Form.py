import tkinter as tk
from tkinter import ttk

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

    # ... the rest of the code is the same ...


    frame2 = ttk.LabelFrame(page, text="Noon Report")
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

    submit_button = ttk.Button(page, text="Submit", command=lambda: print("Form submitted!"))  # Modify this function to handle form submission.
    submit_button.grid(row=2, column=0, pady=10)


def main():
    root = tk.Tk()

    notebook = ttk.Notebook(root)
    notebook.grid(row=0, column=0, padx=10, pady=10)

    for page_name in ['RM1', 'RM2', 'RM5', 'RM7', 'SM3']:
        create_page(notebook, page_name)

    root.mainloop()

if __name__ == "__main__":
    main()
