def bill(units) :
    sum=0
    tot=units-50
    if tot<0 :
        print(f"{units*3.80} units")
        sum+=units*3.80
    
    elif tot>0 :
        print(f"{50*3.80} units")
        rem=units-50
    if(rem<=100) :
        print(f"{rem*4.20}")
    else :
        tr=rem-100
        print(f"{tr*4.20}")
    
        
    
    
    
    
unit=float(input("Enter no of units"))
