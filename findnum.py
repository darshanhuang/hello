
def findnum(low,high,index):

    for n in range(low, high):
        a=str(n)
        result=0
        result = sum(int(i)**index for i in a)
        if result==n:
            print 'Find!', result
            result=0


            
    
