def match(a, b):
    #print('check', a, b)
    if a == b:
        return True
    if a == 'z' and b == 'a':
        return True
    return ord(a) + 1 == ord(b)
    
class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        p1 = 0
        for letter in str2:
            #print('check', letter)
            while p1 < len(str1) and not match(str1[p1], letter):
                p1 += 1
            if p1 >= len(str1):
                return False
            p1 += 1
            #print('match', str1[p1], letter)
        return True
