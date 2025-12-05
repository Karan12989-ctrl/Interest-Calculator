def s_interest(p,r,t):
    return (p*r*t)/100

def c_interest(p,r,t):
    amount=p*(1+r/100)**t
    return amount-p

print("-----INTEREST CALCULATOR-----")
print("1. Simple Interest")
print("2. Compound Interest")

choice=int(input("Enter your choice for Interest (1 or 2): "))

principal=float(input("Enter your Principal Amount: "))
rate=float(input("Enter your Rate of Interest(%): "))
time=float(input("Enter your Rate of Year: "))

if choice==1:
    si=s_interest(principal,rate,time)
    print(f"Simple Interest = {si:.2f}")
    print(f"Total Amount = {principal + si:.2f}")
elif choice==2:
    ci=c_interest(principal,rate,time)
    print(f"Compund Interest = {ci:.2f}")
    print(f"Total Amount = {principal + ci:.2f}")
else:
    print("Your Choice is Invalid, Try Again")