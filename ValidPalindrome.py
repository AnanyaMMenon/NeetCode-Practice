class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_list = []

        for i in range (len(s)):
            if(ord('a')<=ord(s[i])<=ord('z'))or(ord('A')<=ord(s[i])<=ord('Z'))or (ord('0')<=ord(s[i])<=ord('9')):
                new_list.append(s[i].lower())
        left=0
        right=len(new_list)-1

        while left<right:
            if new_list[left]!= new_list[right]:
                return False
            left+=1
            right-=1
        
        return True
