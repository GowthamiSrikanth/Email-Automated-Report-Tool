import yagmail
import pandas as pd

# Step 1: Read the CSV
df = pd.read_csv("dummy sales data.csv")

# Step 2: Clean the data
df = df.dropna(subset=["Sales_Amount"])

# Step 3: Get user input
region = input("Enter the region (North/South/East/West): ").title()
min_sales = float(input("Enter the minimum sales amount: "))

# Step 4: Apply filters
filtered_df = df[(df["Region"] == region) & (df["Sales_Amount"] > min_sales)]

# Step 5: Group and summarize
summary = filtered_df.groupby("Product")["Sales_Amount"].sum().reset_index()
summary = summary.sort_values(by="Sales_Amount", ascending=False)

# Step 6: Export to CSV
output_file = f"summary_report_{region}_{int(min_sales)}.csv"
summary.to_csv(output_file, index=False)

print(f"✅ Report generated successfully: {output_file}")


# Step 7: Email setup
receiver = input("Enter recipient email: ")

# Step 8: Login and send
yag = yagmail.SMTP("gowthamihsrikanth@gmail.com", "zyuj tktv nvtu zfda")

yag.send(
    to=receiver,
    subject="Sales Summary Report",
    contents="Hi,\n\nPlease find attached the requested sales summary report.\n\nRegards,\nGowthami - Data Analyst",
    attachments=output_file
)

print(f"📧 Email sent successfully to {receiver}")
