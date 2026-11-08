class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = 0
        b = a = l = o = n = 0
        for i in range(len(text)):
            if text[i] == "b":
                b+=1
            elif text[i] == "a":
                a+=1
            elif text[i] == "l":
                l+=1
            elif text[i] == "o":
                o+=1
            elif text[i] == "n":
                n+=1

            if b >= 1 and a >= 1 and l >= 2 and o >= 2 and n >=1:
                b -=1
                a-=1
                l-=2
                o-=2
                n-=1

                count +=1
        return count