# Conditional Execution

hrs=input("Enter Hours")
h=float(hrs)

rate=input("Enter the rate")
X=float(rate)
if h<=40:
    print(h*X)
elif  h > 40:
        print(40*X+(h-40)*1.5*X)
