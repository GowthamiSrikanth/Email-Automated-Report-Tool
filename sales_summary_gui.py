import tkinter as tk
from tkinter import messagebox
import pandas as pd
import yagmail


def generate_report():
    # Get user inputs from the GUI
    region = region_entry.get().title()
    min_sales = float(min_sales_entry.get())

    # Step 1: Read the CSV
    df = pd.read_csv("dummy sales data.csv")

    # Step 2: Clean the data
    df = df.dropna(subset=["Sales_Amount"])

    # Step 3: Apply filters
    filtered_df = df[(df["Region"] == region) &
                     (df["Sales_Amount"] > min_sales)]

    # Step 4: Group and summarize
    summary = filtered_df.groupby(
        "Product")["Sales_Amount"].sum().reset_index()
    summary = summary.sort_values(by="Sales_Amount", ascending=False)

    # Step 5: Export to CSV
    output_file = f"summary_report_{region}_{int(min_sales)}.csv"
    summary.to_csv(output_file, index=False)

    # Step 6: Send email
    receiver = email_entry.get()
    yag = yagmail.SMTP("gowthamihsrikanth@gmail.com", "ztzw mthx neyf yfbs")

    yag.send(
        to=receiver,
        subject="Sales Summary Report",
        contents="Hi,\n\nPlease find attached the requested sales summary report.\n\nRegards,\nGowthami - Data Analyst",
        attachments=output_file
    )

    # Success message
    messagebox.showinfo("Success", f"Report generated and sent to {receiver}!")


# Create the main window
root = tk.Tk()
root.title("Sales Report Automation")

# Region input
tk.Label(root, text="Enter the region (North/South/East/West):").pack()
region_entry = tk.Entry(root)
region_entry.pack()

# Minimum sales input
tk.Label(root, text="Enter the minimum sales amount:").pack()
min_sales_entry = tk.Entry(root)
min_sales_entry.pack()

# Email input
tk.Label(root, text="Enter recipient email:").pack()
email_entry = tk.Entry(root)
email_entry.pack()

# Generate report button
generate_button = tk.Button(
    root, text="Generate Report", command=generate_report)
generate_button.pack()

# Run the application
root.mainloop()
