def ispalindrome(s,start,end):
    if start>end:
        return 1
    elif s[start]!=s[end]:
        return 0
    else:
        start+=1
        end-=1
        return ispalindrome(s,start,end)
    
s=input()
print(ispalindrome(s,0,len(s)-1))    
