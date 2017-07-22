def isSpecialPalindrome(n):
    b=bin(n)
    b=b.replace("0b","")
    
    nb = b[::-1]
    b=b.replace("b0","")
    
    if(b != nb):
        return False
    
    if(b.count('0') != 1):
        print(2)
        return False
    
    if(b.count('1') == 0 ):
        print(3)
        return False
    
    return True
    
    
        
    
    
