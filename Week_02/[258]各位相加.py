# 给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。
#
#  示例:
#
#  输入: 38
# 输出: 2
# 解释: 各位相加的过程为：3 + 8 = 11, 1 + 1 = 2。 由于 2 是一位数，所以返回 2。
#
#
#  进阶:
# 你可以不使用循环或者递归，且在 O(1) 时间复杂度内解决这个问题吗？
#  Related Topics 数学


# leetcode submit region begin(Prohibit modification and deletion)
# 数字迭代
class Solution:
    def addDigits1(self, num: int) -> int:
        _sum = 0
        while num > 0 or _sum >= 10:
            _sum += num % 10
            num //= 10
            if _sum >= 10 and num == 0:
                num, _sum = _sum, 0

        return _sum

    # 要求的数叫做数字根，看下 维基百科 的定义。
    #
    # 在数学中，数根(又称位数根或数字根Digital root)是自然数的一种性质，换句话说，每个自然数都有一个数根。
    #
    # 数根是将一正整数的各个位数相加（即横向相加），若加完后的值大于10的话，则继续将各位数进行横向相加直到其值小于十为止[1]，或是，将一数字重复做数字和，直到其值小于十为止，则所得的值为该数的数根。
    #
    # 例如54817的数根为7，因为5+4+8+1+7=25，25大于10则再加一次，2+5=7，7小于十，则7为54817的数根
    #
    # 它的用途:
    #
    # 数根可以计算模运算的同余，对于非常大的数字的情况下可以节省很多时间。
    #
    # 数字根可作为一种检验计算正确性的方法。例如，两数字的和的数根等于两数字分别的数根的和。
    #
    # 另外，数根也可以用来判断数字的整除性，如果数根能被3或9整除，则原来的数也能被3或9整除。
    #
    def addDigits(self, num: int) -> int:
        return 0 if not num else (num - 1) % 9 + 1


# leetcode submit region end(Prohibit modification and deletion)
res = Solution().addDigits(38)
print(res)
