import datetime

today = datetime.datetime.now()
date_time = today.strftime("%H:%M")
print("date and time:",date_time)

ad=None
print(type(ad)==type(None))