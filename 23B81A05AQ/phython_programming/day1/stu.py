student={
    1:{"roll":"5aq","name":"rishi","s1m":5,"s2m":7,"s3m":10},
    2:{"roll":"5ag","name":"naveen","s1m":5,"s2m":6,"s3m":10},
    3:{"roll":"5af","name":"nandu","s1m":5,"s2m":9,"s3m":10}
}
i=1;
total=[0,0,0,0];
avg=[0,0,0,0];
while i<=3 :
    total[i]=student[i]["s1m"]+student[i]["s2m"]+student[i]["s3m"]
    avg[i]=total[i]/3;
    i+=1
print(total,avg)
    