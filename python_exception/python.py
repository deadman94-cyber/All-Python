from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta



 #   now = datetime.now()
  #  print(now)
   # today=date.today()
   # print(today.day,today.month,today.year,today.weekday)


print(timedelta(days=365,hours=5,minutes=1))

#print todays time
today = date.today()
print(today)

#one year from now
print(today  + timedelta(days=365))

#next 2 weeks
print(today + timedelta(days=2,weeks=3))

#previous days/week
print(today - timedelta(weeks=2))

#fools day
birthday = date(today.year, 1, 17)

if birthday < today:
    print("Bithday day has alread went by %d days ago" % (today - birthday).days)
    birthday = birthday.replace(year=today.year + 1)

else:
    date_to_afd = (birthday - today).days
    print("it is just ", date_to_afd, "days to you birthday")


#calender--------------------------------------------------------------------------------------
import calendar
c = calendar.TextCalendar(calendar.SUNDAY)
st=c.formatmonth(2020,1,0,0)
print(st)

#HTML Formatted Calender
chtml = calendar.HTMLCalendar(calendar.SUNDAY)
sthtml=chtml.formatmonth(2020,1)
print(sthtml)

for i in c.itermonthdates(2020,9):
    print(i,i.weekday())

for name in calendar.month_name:
    print(name)
for day in calendar.day_name:
    print(day)

#meeting example on every friday for every month  for years

print("Team meeting will be on:")
for m in range (1,13):
    cal = calendar.monthcalendar(2020,m)
    weekone=cal[0]
    weektwo=cal[1]

    if weekone[calendar.FRIDAY]!=0:
        meetday=weekone[calendar.FRIDAY]
    else:
        meetday=weektwo[calendar.FRIDAY]

    print("%10s %2d" % (calendar.month_name[m],meetday))



#calender for an event for a tuesday for every month for a year

print("Event on every tesday,every month  for a year ")
#for n in range(1,13):
 #   vin = calendar.monthcalendar(2020,m)
  #  print(calendar.month_name[m])


for v in range (1,13):
    vin = calendar.weekday(2020,v,1)
    print() 
    print("%10s %2d" % (calendar.month_name[v],vin))