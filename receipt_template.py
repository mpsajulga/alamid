import datetime

date = datetime.datetime.now()

total_sales = float(input("Total Sales: "))
less_witholding_tax = float(input("Less Witholding Tax: "))


total = total_sales/1.12
less_vat = total*0.12
total_due = total_sales
amount_due = total_sales-less_witholding_tax

print()
print("Date: ", end='')
print(date.strftime("%m""-""%d""-""%Y"))
print(f"Total sales: {total_sales}")
print(f"Less VAT: {less_vat}")
print(f"Total: {total}")
print("SC/PWD Discount: ******")
print(f"Total Due: {total_due}")
print(f"Less Witholding Tax: {less_witholding_tax}")
print(f"Amount Due: {amount_due}")
print(f"VATable Sales: {total}")
print("VAT-Exempt Sales: ******")
print("Zero Rated Sales: ******")
print(f"VAT Amount: {less_vat}")
print(f"Total Sales: {total_sales}")
