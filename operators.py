''' my very first modül '''
def toplama(*args):
    res=0
    for i in args:
        res+=i
    return res
def cikarma(a,b):
    return a-b
def carpma(*args):
    res=1
    for i in args:
        res*=i
    return res
def bolme(a,b):
    if b == 0:
        return "error"
    else:
        return a/b