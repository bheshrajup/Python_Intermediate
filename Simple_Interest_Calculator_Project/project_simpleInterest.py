#-----------Simple interest calculator-----------

def interestCalculator(p,r,t):
    interest =(p*r*t)/100
    return interest

def simpleInterest():
    principal = float(input("Enter the principal amount=>"))
    rate = float(input("Enter the rate of interest =>"))
    time = float(input("Enter the time interval(in yeays)=>"))
    
    interestResult = interestCalculator(principal,time,rate)
    print(f"The simple interest is=>{interestResult}")


simpleInterest()