from palindrome import is_palindrome

def longest_substring(s):
        n=len(s)
        longest=""
        for i in range(n):
                for j in range(i+1,n+1):
                        substring=s[i:j]
                        if is_palindrome(substring) and len(substring)>len(longest):
                                longest=substring
        return longest

if __name__=="__main__":
        string=input("Enter the string: ")
        result=longest_substring(string)
        print("Longest palindromic substring:",result)

