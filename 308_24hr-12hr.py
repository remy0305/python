hour=int(input("what time is it.(24hr)"))
hour-=12 if hour >=12 else hour
print("it is", hour)