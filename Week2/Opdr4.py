def mybin(n):
    if n < 0:
        return 'nope'
    elif n == 0:
        return '0'
    else:
        print(n//2)
        return mybin(n//2) + str(n%2)

#print(test(5))

#print (127//2)
#print( 127%2)

print(mybin(127))