def result(marks[]) :
    if(marks[1]<40 or marks[2]<40 or marks[3]<40) :
        print(f"fail")
        return
    i=1
    while i<=3 :
        if(marks[i]>=40) :
            print(f"{marks[i]} marks pass")
        elif(marks[i]<=50) :
            print("c grade")
        elif(marks[i]>=51 and marks[i]<=70) :
            print("b grade")
        elif(marks[i]>=71 and marks[i]<=80) :
            print("a grade")
        else :
            print("s grade")
        i+=1
result(60,33,55)

            

        