'''def add_binary(a,b):
    return '{0:b}'.format(int(a,2)+int(b,2))'''

def add_binary(a,b):
    max_len = max(len(a),len(b))
    a, b = a.zfill(max_len), b.zfill(max_len)
    carry = 0
    res = []
    for i in range(max_len-1,-1,-1):
        if a[i] == '1':
            carry +=1
        if b[i] == '1':
            carry+=1

        if carry%2 == 1:
            res.append('1')
        else:
            res.append('0')
        
        carry //=2
    if carry == 1:
        res.append('1')
    res.reverse()
    return ''.join(res)



print(add_binary("11","1"))
