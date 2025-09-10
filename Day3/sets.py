day1={"rishi@gmail.com","naveen@gmail.com","nandu@gmail.com","vansh@gmail.com","NAVEEN@gmail.com"}
day2={"rakesh@gmail.com","manoj@gmail.com","rishi@gmail.com","nandu@gmail.com"}
day3={"rishi@gmail.com","kiran@gmail.com","nandu@gmail.com","vansh@gmail.com","naveen@gmail.com"}


#1 case 1 conertcase and remove dup


d1=set()
d2=set()
d3=set()
for i in day1:
    d1.add(i.lower())
for i in day2:
    d2.add(i.lower())
for i in day3:
    d3.add(i.lower())

    #2 uniqe attendence
print("day 1 unique attd",d1)
print("day 2 unique attd",d2)
print("day 3 unique attd",d3)

#3all three days attendence psent
ss=d1.intersection(d2)

print("present all three days",ss.intersection(d3))


#4exactly one day

eod=d1.symmetric_difference(d2)
eod.symmetric_difference(d3)

print("present one day",eod)

#5for



