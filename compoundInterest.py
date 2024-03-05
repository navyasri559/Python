principal=int(input("Enter the PrincipalAccount"))
rate=float(input("rate of interest"))
time=int(input("time period"))
ci=(principal*rate*time)/100
print("compound interest=",ci)