def basetodec(num_str,base):
    num_str = num_str[::-1]
    num = 0
    for k in range(len(num_str)):
        dig = num_str[k]
        if dig.isdigit():
            dig = int(dig)
        else:    
            dig = ord(dig.upper())-ord('A')+10
        num += dig*(base**k)
    return num
print(basetodec("315",7))
