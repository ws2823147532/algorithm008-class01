学习笔记

[TOC]

#### 动态规划

> 其本质是动态递推

1. 避免人肉递归。可以尝试画出递归树
2. 找到**最近最简**方法，将其拆解成可重复解决的问题
3. 如何找到**最近最简方法**：数学归纳法思维
4. 如何区分DP问题：`DP一般会被用来求解最值问题`

> DP与递归和分治的联系

1. DP与 递归或者分治没有根本上的却别
2. 共性：找到重复子问题
3. 差异性：DP有最优子结构，中途可以淘汰次优解



#### 实战例题

###### [509. 斐波那契数](https://leetcode-cn.com/problems/fibonacci-number/)

![image-20200528065512796](https://tva1.sinaimg.cn/large/007S8ZIlly1gf7saakd9nj30nm0hn3zw.jpg)

傻递归 - 自顶向下

画出递归树

时间复杂度：每计算一个节点，需要计算其余的两个节点，以此类推下去，这是一个二叉树的结构，所以它的时间复杂度是O(2^n)的

优化：

- 加入备忘录

  在傻递归的基础上，加入一个缓存，以达到避免重复子问题的重复计算的问题

- 使用DP的思维解决 - 自底向上

DP三步曲

1. 找到重复子问题

   根据数学归纳法：要计算第n个斐波那契数，那么我们只需要计算第n-1和n-2个斐波那契数就可以了

2. 状态定义 - 且找到base case

   假设使用a[i]表示第i个斐波那契数，那么f[i] = f[i-1]+f[i-2] 且f[0]=0,f[1]=1

3. DP方程
   $$
   f(n)=\left\{
   \begin{aligned}
   0 &,& n=0 \\
   1 &,& n=1 \\
   f(n-1)+f(n-2) &,& n>1
   \end{aligned}
   \right.
   $$



###### [70. 爬楼梯](https://leetcode-cn.com/problems/climbing-stairs/)

![image-20200530102415327](https://tva1.sinaimg.cn/large/007S8ZIlly1gfa9koughqj30ij0ebjsi.jpg)

考虑下变体：

- 不止可以上1阶或2阶：可以上1、2、3阶等
- 可以上1 2 3阶，且相邻的两个步伐不能相同，该如何设计

本体：
$$
f(n)=\left\{
\begin{aligned}
1 &,& n=1 \\
2 &,& n=2 \\
f(n-1)+f(n-2) &,& n>2
\end{aligned}
\right.
$$


变体1：
$$
f(n)=\left\{
\begin{aligned}
1 &,& n=1 \\
2 &,& n=2 \\
4 &,& n=3 \\
f(n-1)+f(n-2)+f(n-3) &,& n>3
\end{aligned}
\right.
$$
变体2：

定义dp\[0...2][i]，

​	dp\[0][i]表示到达i最后一次走了1步；

​	dp\[1][i]表示到达i最后一次走了2步；

​	dp\[2][i]表示到达i最后一次走了3步

那么

​	dp\[0][i]=dp\[1][i-1]+dp\[2][i-1]；到当前台阶走了1步，那么前面只能再选最后一次走了2步和3步的

​	dp\[1][i]=dp\[0][i-2]+dp\[2][i-2]；到当前台阶走了2步，那么前面只能再选最后一次走了1步和3步

​	dp\[2][i]=dp\[0][i-3]+dp\[1][i-3]    到当前台阶走了3步，那么前面只能再选最后一次走了1步和2步的

结果为：dp\[0][-1]+dp\[1][-1]+dp\[2][-1]，即到达n的所有步伐的总和

```python
    def changeClimbStairs(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 1
        if n == 3: return 3

        # dp[0][i] 最后一次走了1步到达 i
        # dp[1][i] 最后一次走了2步到达 i
        # dp[2][i] 最后一次走了3步到达 i
        dp = [
            [1, 0, 1] + [0] * (n - 3),  # 最后一次走1步
            [0, 1, 1] + [0] * (n - 3),  # 最后一次走2步
            [0, 0, 1] + [0] * (n - 3)   # 最后一次走3步
        ]

        for i in range(3, n):
            # 到当前台阶走了1步，那么前面只能再选最后一次走了2步和3步的
            dp[0][i] = dp[1][i - 1] + dp[2][i - 1]  
            # 到当前台阶走了2步，那么前面只能再选最后一次走了1步和3步的
            dp[1][i] = dp[0][i - 2] + dp[2][i - 2]  
            # 到当前台阶走了3步，那么前面只能再选最后一次走了1步和2步的
            dp[2][i] = dp[0][i - 3] + dp[1][i - 3]  

        return dp[0][-1] + dp[1][-1] + dp[2][-1]
```





###### [322. 零钱兑换](https://leetcode-cn.com/problems/coin-change/)

![image-20200529150931667](https://tva1.sinaimg.cn/large/007S8ZIlly1gf9c76vxnoj31b00ps77e.jpg)

略过递归方案，直接上DP

DP问题三步曲

1. 找到重复子问题

   根据数学归纳法：已知某金额所需的最少硬币数，可得其他金额的所需最少硬币数

2. 状态定义

   假设dp[i]表示，金额为i时需要的最少硬币数，那么因为有coins个硬币可选，所以dp[i]=min(dp[i-k] for k in coins) + 1，加1表示要选择一个面值为k的硬币

   dp初始值为mount+1，因为金额为amout，所需硬币最多为amout个1元硬币，长度为amout+1

   dp[0]=0，表示当金额为0时，需要的硬币数也为0

   最终结果：dp[amout]

3. DP方程

$$
f(n) = \left\{
\begin{aligned}
0 &,& n=0 \\
1 &,& n=1 \\
min(f(n-k))+1 &,& k \in coins \\
\end{aligned}
\right.
$$

```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] < amount + 1 else -1
```

###### [62. 不同路径](https://leetcode-cn.com/problems/unique-paths/)

![image-20200529153859627](https://tva1.sinaimg.cn/large/007S8ZIlly1gf9d1sl4wtj30xu0u0n2h.jpg)

直接DP三步曲

1. 找到重复子问题

   要求从位置(i,j)到END的不同路径数，由于从某个位置出发只能向右或向下走，如果我知道了从(i+1, j)和从(i,j+1)到END的路径数，那么我就能得到$$path_{i,j}$$，$$path_{i,j}$$=$$path_{i+1,j}$$+$$path_{i,j+1}$$

2. 状态定义

   定义dp\[m][n]数组，表示棋盘，每个元素表示从该位置出发，到END的不同路径数

   dp\[][n]=1，右边界全为1，因为右边界的位置到END，路径数都是1

   dp\[m][]=1，下边界全为1，因为下边界的位置到END，路径数都是1

   遍历方向：从END位置开始向上遍历

   最终结果：dp\[0][0]

3. DP方程

$$
f(x,y) = \left\{
\begin{aligned}
1 &,& x=m\\
1 &,& y=n\\
f(x+1, y)+f(x, y+1) &,& 0 \leq x < m \& 0 \leq y < n
\end{aligned}
\right.
$$

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if n == 1: return 1
        # 初始化dp数组，左边界和右边界都初始化为1
        dp = [[1 if j == m - 1 or i == n - 1 else 0 for j in range(m)] for i in range(n)]

        for i in range(n - 2, -1, -1):
            for j in range(m - 2, -1, -1):
                dp[i][j] = dp[i + 1][j] + dp[i][j + 1]
        return dp[0][0]
    
    # 空间压缩：我们只需要一维的数组就可以存下路径的变化
    def uniquePaths(self, m: int, n: int) -> int:
        if n == 1: return 1
        # 初始化dp数组为 1
        dp = [1] * m

        for i in range(n - 2, -1, -1):
            for j in range(m - 2, -1, -1):
                dp[j] = dp[j] + dp[j + 1]
        return dp[0]
```



###### [63. 不同路径 II](https://leetcode-cn.com/problems/unique-paths-ii/)

![image-20200529175152160](https://tva1.sinaimg.cn/large/007S8ZIlly1gf9gw1sj0kj30xj0u0jx7.jpg)

直接DP三步曲

1. 找到重复子问题

   要求从位置(i,j)到END的不同路径数，由于从某个位置出发只能向右或向下走，如果我知道了从(i+1, j)和从(i,j+1)到END的路径数，那么我就能得到$$path_{i,j}$$，$$path_{i,j}$$=$$path_{i+1,j}$$+$$

2. 状态定义

   定义dp\[m][n]数组，表示棋盘，每个元素表示从该位置出发，到END的不同路径数

   dp\[][n]=1，右边界最后一个障碍物之后全为1，最后一个障碍物及之前的位置全为0，因为右边界一旦出现了障碍物，那么在这之前的位置的路径就都被截断了

   dp\[m][]=1，下边界最后一个障碍物之后全为1，最后一个障碍物及之前的位置全为0，因为下边界一旦出现了障碍物，那么在这之前的位置的路径就都被截断了

   需要注意的是：棋盘上为1的位置不能走，那个位置的路径数为0

   遍历方向：从END位置开始遍历

   最终结果：dp\[0][0]

3. DP方程

$$
f(x,y) = \left\{
\begin{aligned}
0 &,& x=m\&x\leq lastcol(lastrow表示下边界最后一个障碍物的位置)\\
0 &,& y=n\&y\leq lastrow(lastrow表示右边界最后一个障碍物的位置)\\
1 &,& x=m\&x>lastcol(lastrow表示下边界最后一个障碍物的位置)\\
1 &,& y=n\&y>lastrow(lastrow表示右边界最后一个障碍物的位置)\\
0 &,& obstacleGrid(x, y)=1\\
f(x-1, y)+f(x, y-1) &,& 0 \leq x < m \& 0 \leq y < n
\end{aligned}
\right.
$$



```python
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid[0]), len(obstacleGrid)
        # if obstacleGrid[-1][-1] == 1 or obstacleGrid[0][0] == 1: return 0  # 起点和终点为1，直接返回0
        # if n == 1:  # 只有一行
        #     if sum(obstacleGrid[0]) >= 1:  # 行出现了1
        #         return 0
        #     else:
        #         return 1
        # if m == 1:  # 只有一列
        #     if sum(list(chain(*obstacleGrid))) >= 1:  # 列出现了1
        #         return 0
        #     else:
        #         return 1
        # 如果 最后一行或最后一列出现了1，那么1出现的位置及之前的位置和1没有区别
        last_row, last_col = -1, -1  # 标记最后一行(列)出现障碍的位置
        for i in range(n - 1, -1, -1):
            if obstacleGrid[i][-1] == 1:
                last_row = i
                break
        for i in range(m - 1, -1, -1):
            if obstacleGrid[-1][i] == 1:
                last_col = i
                break

        # 根据棋盘的最后一行和最后一列初始化 dp数组
        # 包含了 起点和终点为1 的情况
        # 包含了 只有一行和只有一列的情况
        dp = [[1 if i > last_col and j == n - 1 or j > last_row and i == m - 1 else 0 for i in range(m)] for j in
              range(n)]

        for i in range(n - 2, -1, -1):
            for j in range(m - 2, -1, -1):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i + 1][j] + dp[i][j + 1]

        return dp[0][0]
    
    # dp空间压缩：实际上我们在进行递推的时候，只需要一维数组就可以
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid[0]), len(obstacleGrid)
        dp = [0] * m
        dp[m - 1] = 1
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if obstacleGrid[i][j] == 1:  # 当前位置为障碍物
                    dp[j] = 0
                elif j < m - 1:  # 因为要使用下一个坐标，这里要检测坐标的合法性，防止指针越界
                    dp[j] += dp[j + 1]

        return dp[0]
```



###### [1143. 最长公共子序列](https://leetcode-cn.com/problems/longest-common-subsequence/)

![image-20200530080158059](https://tva1.sinaimg.cn/large/007S8ZIlly1gfa5gmnx4bj30xx0u044x.jpg)

思维：DP最终会归结到一个状态数组中，所以拿到一个这样的题目后，就往一维状态数组上靠拢，一维搞不定，就尝试用二维数组，再不行就三维...然后依靠数学归纳法进行推导，看是否能根据已知内容的位置 推导出当前位置的值

直接上DP三步曲

1. 找到重复子问题

   abcde和abc的问题可以由下列的二维表格描述，如果要求某个位置的值，只需要知道它之前的某些位置即可

   |      | a           | b            | c             | d              | e                |
   | ---- | ----------- | ------------ | ------------- | -------------- | ---------------- |
   | a    | LCS(a,a)=1  | LCS(a,ab)=1  | LCS(a,abc)=1  | LCS(a,aabcd)=1 | LCS(a,abcde)=1   |
   | c    | LCS(ac,a)=1 | LCS(ac,ab)=1 | LCS(ac,abc)=2 | 2              | 2                |
   | e    | 1           | 1            | 2             | 2              | LCS(ace,abcde)=3 |

2. 定义状态

   dp\[i][j]，i表示第一个字符串的位置编号，j表示第二个字符串的位置编号，整体表示两个子串的最长公共子序列的长度

   dp长度初始化为text1.length+1*text2.length+1，因为至少要包含没有字符的情况

   初始值：dp\[0][0]=0

   遍历方向：从前往后。因为base case在前部

   最终结果：dp\[text1.length][text2.length]

3. DP方程

$$
f(x, y) = \left\{
\begin{aligned}
0 &,& x=0\&y=0 \\
max(f(x-1, y), f(x, y-1)) &,& text1(x)!=text2(y) \\
f(x-1, y-1)+1 &,& text1(x)=text2(y) \\
\end{aligned}
\right.
$$



```python
class Solution:
    def longestCommonSubsequence1(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text1[j - 1] == text2[i - 1]:  # 当前位置的两个字符一样，取对角的值再加1(加上自身)
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:  # 当前位置的两个字符不一样，取两个字符对应的最大值
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[n][m]

    # dp空间压缩：发现求当前位置的值，只需要left和last_line的值
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        # 当前位置，当前位置的左一位置
        curr, left = 0, 0
        # 上一行的值
        last_line = [0] * (m + 1)

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text1[j - 1] == text2[i - 1]:  # 当前位置的两个字符一样，取对角的值再加1(加上自身)
                    curr = last_line[j - 1] + 1
                else:  # 当前位置的两个字符不一样，取两个字符对应的最大值
                    curr = max(last_line[j], left)
                # 根据当前计算的结果 更新上一行，遍历到下一行的时候，正好可以用
                if j == m:  # 换行：可以更新当前位置的up位置元素，且把left重置为0
                    last_line[j - 1], last_line[j], left = left, curr, 0
                else:  # 不换行：不能更新up位置，因为在同一行中遍历的时候，要使用原始的值
                    last_line[j - 1], left = left, curr

        return curr
```



###### [120. 三角形最小路径和](https://leetcode-cn.com/problems/triangle/)

![image-20200530092638716](https://tva1.sinaimg.cn/large/007S8ZIlly1gfa7wqal6mj30ku0degmu.jpg)

直接DP三步曲

1. 找到重复子问题

   要想求得到达当前位置的最小路径和，那么我只需要知道到达当前位置的up和up_left最小路径和即可

2. 状态定义

   dp\[i][j]，i和j分别表示矩阵的坐标，整体表示到达该坐标的最小路径和

   dp\[0][0]为矩阵的第一个元素值

   最终结果：min(dp[-1])

3. DP方程

$$
f(x, y) = \left\{
\begin{aligned}
matrix(0, 0) &, & x=0\&y=0 \\
min(f(x-1, y), f(x-1. y-1)) + matrix(x,y) &,& 0\leq x \& 0\leq y
\end{aligned}
\right.
$$

```python
class Solution:
    def minimumTotal1(self, triangle: List[List[int]]) -> int:
        m, n = len(triangle[-1]), len(triangle)

        dp = [[0 for _ in row] for row in triangle]
        dp[0][0] = triangle[0][0]

        for i in range(1, n):
            for j, val in enumerate(triangle[i]):
                if j == 0: dp[i][j] = dp[i - 1][j] + val
                elif j == len(triangle[i]) - 1: dp[i][j] = dp[i - 1][j - 1] + val
                else: dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1]) + val

        return min(dp[-1])

    # dp空间压缩
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m, n = len(triangle[-1]), len(triangle)

        dp = triangle
        for i in range(1, n):
            for j, val in enumerate(triangle[i]):
                if j == 0: dp[i][j] = dp[i - 1][j] + val
                elif j == len(triangle[i]) - 1: dp[i][j] = dp[i - 1][j - 1] + val
                else: dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1]) + val

        return min(dp[-1])
```



###### [221. 最大正方形](https://leetcode-cn.com/problems/maximal-square/)

![image-20200530121844939](https://tva1.sinaimg.cn/large/007S8ZIlly1gfacvt7tj7j30m609iq3f.jpg)

DP三步曲

1. 找到重复子问题

   以某个位置(i,j)为右下角的正方形的边长，可以根据当前位置的up、left、left_up三个位置确定出来

   状态定义

   dp\[i][j]表示以(i,j)为右下角的正方形的边长，那么如果(i,j)为0，dp\[i][j]=0；否则dp\[i][j]=min(up,left,up_left)+1

   加1的目的是，至少包含它本身

2. DP方程

![image-20200601094644553](https://tva1.sinaimg.cn/large/007S8ZIlly1gfcjq9qu41j30j801mq2y.jpg)

```python
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]: return 0
        m, n = len(matrix[0]), len(matrix)
        dp = [[0 for _ in range(m)] for _ in range(n)]
        max_edge = dp[0][0] = int(matrix[0][0])
        for i in range(0, n):
            for j in range(0, m):
                if i == 0 or j == 0:
                    dp[i][j] = 0 if matrix[i][j] == '0' else 1
                else:
                    dp[i][j] = 0 if matrix[i][j] == '0' else min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                max_edge = max(dp[i][j], max_edge)

        return max_edge * max_edge
```



###### [312. 戳气球](https://leetcode-cn.com/problems/burst-balloons/)

![image-20200530092718495](https://tva1.sinaimg.cn/large/007S8ZIlly1gfa7xf1ixuj30mq0bkmyr.jpg)

DP三步曲

1. 找到重复子问题

   当只有一个气球时，只需要戳一次即可

   当有两个气球时，也只需要戳一次

   当有三个气球时，那么肯定要先戳中间那一个

   当有四个气球时，那么就要

2. 状态定义

   气球的个数为n

   假设dp\[i][j]表示序号在(i,j)之间的获得的硬币最大值，那么我们需要通过遍历(i,j)之间的所有序号，求出dp\[i][k]和dp\[k][j]，因为dp\[i][j]=dp\[i][k]+dp\[k][j]+k，

   最终结果：dp\[0][n+1]

3. DP方程

$$

$$







###### [198. 打家劫舍](https://leetcode-cn.com/problems/house-robber/)

![image-20200528063944746](https://tva1.sinaimg.cn/large/007S8ZIlly1gf7ru9d1mfj31bg0p8n24.jpg)

略过递归方案，直接上DP

DP问题三步曲

1. 找到重复子问题

   根据数学归纳法：如果已知小偷在第i-1个房间对应的最高金额，那么小偷在第i个房间的对应的最高金额有以下两种情况

   - 小偷偷了第i-1房间：那么小偷势必不能偷第i个房间，那么这个时候小偷偷的金额应该继承上一个值
   - 小偷没有偷第i-1房间：那么小偷一定要偷第i个房间(因为是求的最大值)，这个时候小偷偷的金额应该是上一个值加上第i个房间的金额

2. 状态定义

   那么我们怎么表示某一个房间偷与不偷呢？此时我们可以考虑在一维的基础之上加一维附加这个状态，用dp\[i][0]表示没有偷第i个房间，dp\[i][1]表示偷了第i个房间，nums[i]表示第i间房的金额，那么

   - 计算没有偷i房的时候在i的最大金额：dp\[i][0]=max(dp\[i-1][0], dp\[i-1][1])

   - 计算偷i房的时候在i的最大金额：dp\[i][1]=dp\[i-1][0]+nums[i]

   dp的初始值为全为0，长度为n+1，

   第0个元素表示房间数为0时，能偷到的金额为0，

   第n个元素表示到达最后一个房间，能偷到的金额为多少

   遍历从1开始

   最终的结果：max(dp\[n][0], dp\[n][1])

3. DP方程定义

$$
f(n,0) =\left\{
\begin{aligned}
0 &,& n=0 \\
max(f(n-1, 0), f(n-1, 1)) &,& n>1
\end{aligned}
\right.
$$

$$
f(n,1) =\left\{
\begin{aligned}
0 &,& n=0 \\
f(n-1, 0)+nums(n) &,& n>1
\end{aligned}
\right.
$$

$$
res = max(f(n, 0), f(n, 1))
$$

```python
class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)  # 房间个数
        dp = [[0 for _ in range(2)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])  # 不偷第i间房
            dp[i][1] = dp[i - 1][0] + nums[i - 1]  # 偷第i间房

        return max(dp[n][0], dp[n][1])  # 返回第i间房 偷与不偷的最大金额
```



DP问题三步曲-version2

> 第一个版本中，我们考虑的时候，并不知道小偷有没有偷某个房间，所以加了一个维度表示某个房间偷与不偷的 对应的最大金额
>
> 这个版本中，我们换个思路，可以肯定的是，小偷一定会偷其中一间房，也就是说，如果我们假定某间房必偷的话，那么我们最终的结果应该是所有结果的最大值

1. 找到重复子问题

   根据数学归纳法：由于小偷不能偷连续的两间房，那么我们如果要计算第i间房最大金额，该怎么计算呢？这个时候，前一间房要么偷了，要么没偷，如果前一间房没偷，那么看前两间房偷没偷，前两间房如果没偷，那就继续往前推

2. 状态定义-DP数组含义及base case

   dp[i]表示当偷到第i间房时的最大金额，不管第i间房偷与不偷，

   dp[i]=max(dp[i-1], dp[i-2]+nums[i])  表示：偷与不偷i-1的时候，在第i间房的最大金额

   dp初始化全为0，长度为n+2

   dp[0], dp[1]表示第1间房前1间、两间的金额都为0

   遍历从2开始

   最终结果：max(dp)

3. DP方程

$$
f(n) = \left\{
\begin{aligned}
0 &,& n=-1 \\
0 &,& n=0 \\
max(f(n-1), f(n-2)+nums(n)) &,& n>0
\end{aligned}
\right.
$$

```python
class Solution:
    def robnn(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [0] * (n + 2)

        for i in range(2, n + 2):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 2])

        return max(dp)
    
    # ====> 优化，去掉最后的取最大值的函数，且降低空间复杂度
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        i_2, i_1, res = 0, 0, 0  # 前两间房的最大金额，前一间房的最大金额，当前房间的最大金额
        for i in range(n):
            # dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 2])
            # 更新偷到当前房间的最大金额
            res = max(i_1, i_2 + nums[i])
            # 上一个res变成前一间房
            # 上一个i_1变成前两间房
            i_1, i_2 = res, i_1

        return res
```















