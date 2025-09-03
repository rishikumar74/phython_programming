def convert(days) :
    yrs=days//365
    
    remd=days%365
    mts=remd//30
    rem=remd%30
    return f"{yrs} yrs and {mts} months and {rem} days"



print(convert(400))