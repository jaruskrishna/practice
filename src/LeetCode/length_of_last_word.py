class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        print("The sentence is - ", s)
        brk = s.split()
        print(brk)
        l = len(brk)
        print("The last word is - ", brk[l-1])
        last = brk[l-1]
        len_last = len(last)
        print("The last word -", len_last)


if __name__ == "__main__":
    sent = "hello   world    i am     here"
    a = Solution()
    a.lengthOfLastWord(sent)

