
[1, 2, 3]
[3, 0]

def add_strings(num1, num2):
    l=list()
    l1=list()
    l2=list()
    str_=''
    print("test")
    for i in num1:
        l.append(int(i))
    for i in num2:
        l1.append(int(i))
    len_=len(l)
    len1_=len(l1)

    if len_==len1_:
        for i in l2:
            l2[i]=l[i]+l1[i]
    if len_<len1_:
        diff= len1_-len_
        l=([0]*diff + l)
        for i in range(len1_):
            #l2[i]=l[i]+l1[i]
            l2.append(l[i]+l1[i])
    if len1_<len_:
        diff= len_-len1_
        l1=([0]*diff + l1)
        for i in range(len_):
            # l2[i]=l[i]+l1[i]
            l2.append(l[i]+l1[i])
    print(l2)

    for e in l2:
        str_+= str(e)
    print(str_)

    return str_
        