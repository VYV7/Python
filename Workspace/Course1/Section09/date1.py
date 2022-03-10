print("========================================================================")

print("1--------------------------------")
# TIME
import datetime

# set time
t = datetime.time(1,15,5)
print(t)

# get today's date
d = datetime.date.today()
print(d)

# get OS date and time
dt = datetime.datetime.now()
print(dt)


print("2--------------------------------")
# TIME MEASUREMENT
t0 = datetime.datetime.now()
result = [x**2 for x in range(1000)]
t1 = datetime.datetime.now()

timeDiff = t1 - t0
print(timeDiff)


print("========================================================================")