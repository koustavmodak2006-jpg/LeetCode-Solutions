class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return "1"

        say = self.countAndSay(n-1)
        result = ""
        count = 1
        
        for i in range(len(say)):
            if i+1 < len(say) and say[i] == say[i+1]:
                count+=1
            else:
                result+= str(count) + say[i]
                count=1
        return result