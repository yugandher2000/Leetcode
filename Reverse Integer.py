class Solution:
    def reverse(self, x: int) -> int:
        a=abs(x)
        num=0
        while(a!=0):
            num=num*10+a%10
            a=a//10
        if x>0:
            num=num
        else:
            num=-num
        if num<-2**31 or num> 2**31-1:
            return 0 
        return num
