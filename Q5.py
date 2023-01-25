# Check given date is in range or not

from datetime import datetime
 
print('Note : Date Format should be like these --> 2023-01-25') 

s_date = input('Enter the Starting date: ')
e_date = input('Enter the End date: ')
g_date = input('Enter the date that you have to check in range or not: ')

g_date = datetime.strptime(g_date, '%Y-%m-%d')         # this function will convert the input date string into proper time_data format 
s_date = datetime.strptime(s_date, '%Y-%m-%d')
e_date = datetime.strptime(e_date, '%Y-%m-%d')

if( g_date >= s_date and g_date <= e_date):
       print('Yes, given date is in range')
else:
    print('No, given date is not in range')


