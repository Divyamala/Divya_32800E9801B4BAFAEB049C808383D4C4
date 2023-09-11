#1.1 Implement a recursive function to: calculate the Tectorial of a given amber
def fact_rec(n):
if n@ or n=1:
return 1
else:
return n*fact_rec(n-1)
number = 2
res = fact_rec(number)
pyproject.toml
Tools
print("The factorial of {} is {}".format(number, res))
