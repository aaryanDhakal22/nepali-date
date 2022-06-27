# IMPORTS
from nepali_date import NepaliDate
from win10toast import ToastNotifier
from datetime import datetime
# VARIABLE
weekDays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
months = ['Baisakh','Jestha','Ashar','Shrawan','Bhadau','Ashoj','Kartik','Mangsir','Poush','Magh','Falgun','Chaitra']

# TODAYS DATE
date = NepaliDate.today()
date_str = str(date)

# MONTH
index = date_str[9:10] if date_str[8:9] == '0' else date_str[8:10]
month = months[int(index)-1]

# YEAR
year = date.year_translated

# YEAR
day = date.day_translated
day_in_eng = weekDays[datetime.today().weekday()]

# IF SHE READS OR NOT
read = 'No' if day_in_eng in ['Wednesday','Saturday'] else 'Yes'

final_format = f'{day}th of {month} , {day_in_eng} - {read} Reading'

# NOTIFIER
toaster = ToastNotifier()
toaster.show_toast(final_format,msg='  ',duration=5)