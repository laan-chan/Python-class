def factorial(N):
    f0=1
    i=1
    while i<=N:
        f0=f0*i
        i=i+1
    return
print("N value")
N=int(input())
print("r value")
R=int(input())
bincoef=fact(N)/(fact(R)*fact(N-R))
print('bincoef=',bincoef)
