# 你正在和你的朋友玩 猜数字（Bulls and Cows）游戏：你写下一个数字让你的朋友猜。每次他猜测后，你给他一个提示，告诉他有多少位数字和确切位置都猜对
# 了（称为“Bulls”, 公牛），有多少位数字猜对了但是位置不对（称为“Cows”, 奶牛）。你的朋友将会根据提示继续猜，直到猜出秘密数字。 
# 
#  请写出一个根据秘密数字和朋友的猜测数返回提示的函数，用 A 表示公牛，用 B 表示奶牛。 
# 
#  请注意秘密数字和朋友的猜测数都可能含有重复数字。 
# 
#  示例 1: 
# 
#  输入: secret = "1807", guess = "7810"
# 
# 输出: "1A3B"
# 
# 解释: 1 公牛和 3 奶牛。公牛是 8，奶牛是 0, 1 和 7。 
# 
#  示例 2: 
# 
#  输入: secret = "1123", guess = "0111"
# 
# 输出: "1A1B"
# 
# 解释: 朋友猜测数中的第一个 1 是公牛，第二个或第三个 1 可被视为奶牛。 
# 
#  说明: 你可以假设秘密数字和朋友的猜测数都只包含数字，并且它们的长度永远相等。 
#  Related Topics 哈希表


# leetcode submit region begin(Prohibit modification and deletion)
# 第一遍找到公牛
# 第二遍找到母牛
# 关键在与理解题目的含义：找完公牛之后，如果secret中有重复的数字且guess中也有重复的数字，是要计算多次母牛的
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        l = len(secret)
        guess = [c for c in guess]
        bull = 0
        tmp = {str(i): 0 for i in range(10)}
        for i in range(l):
            if secret[i] == guess[i]:
                bull += 1
                guess[i] = '#'
            else:
                tmp[secret[i]] += 1
        cow = 0
        for c in guess:
            if c in tmp and tmp[c] > 0:
                cow += 1
                tmp[c] -= 1

        return f'{bull}A{cow}B'


# leetcode submit region end(Prohibit modification and deletion)

res = Solution().getHint('1123', '0111')
print(res)
