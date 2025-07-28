from datetime import datetime, timedelta
current_date=datetime.today()
newdate=current_date - timedelta(days=5)

print("current date:", current_date.strftime("%d-%m-%Y"))
print("Date after subtracting 5 days:", newdate.strftime("%d-%m-%Y"))
