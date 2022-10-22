class Solution:
    def isPalindrome(self, x: int) -> bool:

        print("The int value is ", x)
        temp = x
        rev = 0
        while (x > 0):
            rem = x % 10
            rev = (rev * 10) + rem
            x = x // 10
        print("the rev number is ", rev)

        if x == temp:
            return True
        else:
            return False

if __name__ == "__main__":

    a = Solution()
    a.isPalindrome(121)