# https://leetcode.com/problems/length-of-last-word/?envType=study-plan-v2&envId=top-interview-150

str = "   fly me   to   the moond  "
def lengthOfLastWord(s: str) -> int:
    return len(s.split()[-1])


print(lengthOfLastWord(str))