def maximumProfit(prices)->int:
        res=0
        
        for i in range (1,len(prices)):
            if(prices[i]>prices[i-1]):
                res=res+prices[i]-prices[i-1]
                
        return print("Miximum profit :",res)

if __name__=="__main__":
     prices=[100,180,260,310,40,535,695]
     maximumProfit(prices)