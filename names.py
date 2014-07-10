

def func2(filename):
   
    names = [i.strip() for i in open(filename)]
    re = 0
    c = ''
    for index, value in enumerate(sorted(names)):
        num = sum ( [(ord(c) - ord('A') + 1) for c in list(value)])
        re = re + num * (index + 1)

    return re


def func3(filename):
   
    names = [i.strip() for i in open(filename)]
    c=''
    return sum([sum([(ord(c)-ord('A')+1) for c in list(value)])*(index+1) for index,value in enumerate(sorted(names))])            


def func4(filename):                                                    #map/reduce method
    names = (r.strip() for r in open(filename))
    names = sorted(names)
    f =  lambda x, y: sum([ord(word)-64 for word in x]) * y             #hidden function
    values = [f(name, index+1) for index, name in enumerate(names)]
    print sum(values)

    





            

        
