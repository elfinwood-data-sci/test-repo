# Using Python version 3.5.0, raw_input no longer valid in this version
hrs = input('Enter Hours:\n')
rate = input('Enter pay rate (dollars/hour):')
r = float(rate)
h = float(hrs)
if 0<h<=40:
    pay_ltet40=h*r
    print(pay_ltet40)
else:
    pay_gt40=(40*r)+((h-40)*(r*1.5))
    print(pay_gt40)
    print ("Howdy Partner")
    
