import math
import copy
def B(n,k):
    return((math.factorial(n)//math.factorial(k))//math.factorial(n-k))


print(B(6,3))

def BDP(n,k):
    gvddomN = n+1
    gvddomK = k+1

    twoDwarray = [None]*gvddomN
    for needtodothiscusfillinga2darrayinonelinegivesbyreferencedotdotdot in range(0,gvddomN):
        twoDwarray[needtodothiscusfillinga2darrayinonelinegivesbyreferencedotdotdot] = [None]*gvddomK

    for en in range(0, gvddomN):
        for ka in range(0,gvddomK):
            if (en-ka) >= 0:
                twoDwarray[en][ka] = B(en,ka)
                # print(str(en) + " " + str(ka))
    return twoDwarray

print(BDP(6,3))