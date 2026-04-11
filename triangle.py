def valid(sides):
    a,b,c = sorted(sides)
    return a>0 and a +b >= c 


def equilateral(sides):
    
    return valid(sides) and len(set(sides)) == 1
    


def isosceles(sides):
    return valid(sides) and len(set(sides)) <=2

def scalene(sides):
    return valid(sides) and len(set(sides)) ==3 

   
