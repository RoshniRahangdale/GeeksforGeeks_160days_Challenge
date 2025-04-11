def myAtoi( s):
        # Code here
        # remove whitespaces
        i=0
        sign=1
        result=0
        while i<len(s) and s[i]==' ':
            i+=1
            
        # string is empty after removing whitespaces
        if i<len(s) and (s[i]=='-' or s[i]=='+'):
            if s[i]=='-':
                sign=-1
            i+=1    
       
            
        
        while i<len(s) and '0'<=s[i]<='9':
            result=10*result +(ord(s[i])-ord('0'))
            
            if result >(2**31-1):
               return sign*(2**31-1)  if sign==1 else -2**31
            
            i+=1    
       
            
        return sign*result
    
if __name__== "__main__":
        s="  -0012gfg4"
        print(myAtoi(s))
    
    