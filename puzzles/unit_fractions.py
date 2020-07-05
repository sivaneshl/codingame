# [(i,n*(n+i)/i) for i in range(1,100000000) if n*(n+i)%i==0]

import time

n=17
x=n
i=0
start=time.time()
while x<2*n:
    i=i+1
    x=n+i
    p=n*x
    q, r=divmod(p, i)
    if r==0:
        print("1/{} = 1/{} + 1/{}".format(n, n*x//i, x))

end = time.time()
print(time.strftime("%H:%M:%S",time.gmtime(end-start)))