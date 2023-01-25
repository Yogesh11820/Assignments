import datetime


today_date = datetime.date.today() 
date_obj = datetime.date(2022, 5, 21) 

print(date_obj - today_date) 
print((date_obj - today_date).days) 

curr_time = datetime.datetime.now().time()
print(curr_time)
dt_obj = datetime.time(8,10,20)
diff = datetime.timedelta(hours=(dt_obj.hour - curr_time.hour), minutes=(dt_obj.minute - curr_time.minute), seconds=(dt_obj.second - curr_time.second))
print(diff)