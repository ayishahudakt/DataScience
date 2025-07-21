from datetime import datetime

date1_str = input("Enter the first date (dd-mm-yyyy): ")
date2_str = input("Enter the second date (dd-mm-yyyy): ")

date1 = datetime.strptime(date1_str, "%d-%m-%Y")
date2 = datetime.strptime(date2_str, "%d-%m-%Y")

if date1 < date2:
    print("The earlier date is:", date1_str)
elif date2 < date1:
    print("The earlier date is:", date2_str)
else:
    print("Both dates are the same.")
