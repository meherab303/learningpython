def lengthOfLastWord( s):
       s=s.rstrip()
       s=s.split(" ")
       return len(s[len(s)-1])

print(lengthOfLastWord("   fly me   to   the moon  "))  









