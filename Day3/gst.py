def apply_disc(dv,price) :
    dis=price-(dv/100)*price
    return dis

def add_gst(price,percent=18) :
    tot=price+(percent/100)*price
    return tot

def gen_invoice(dict,dv=0,gst=18) :
    for i in dict['rishi'] :
        discount=apply_disc(20,dict['rishi'][i])
        print("actuall price",discount)

    for i in dict['rishi']:
        discount = add_gst(dict['rishi'][i],20)
        print("actuall price", discount)

