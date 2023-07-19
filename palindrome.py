def ispalindrome(s,start,end):
    if start>end:
        return True
    elif s[start]!=s[end]:
        return False
    else:
        start+=1
        end-=1
        return ispalindrome(s,start,end)
    
s=input()
print(ispalindrome(s,0,len(s)-1))    
