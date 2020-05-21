//n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
//
//
//
// 上图为 8 皇后问题的一种解法。
//
// 给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。
//
// 每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
//
// 示例:
//
// 输入: 4
//输出: [
// [".Q..",  // 解法 1
//  "...Q",
//  "Q...",
//  "..Q."],
//
// ["..Q.",  // 解法 2
//  "Q...",
//  "...Q",
//  ".Q.."]
//]
//解释: 4 皇后问题存在两个不同的解法。
//
//
//
//
// 提示：
//
//
// 皇后，是国际象棋中的棋子，意味着国王的妻子。皇后只做一件事，那就是“吃子”。当她遇见可以吃的棋子时，就迅速冲上去吃掉棋子。当然，她横、竖、斜都可走一到七步
//，可进可退。（引用自 百度百科 - 皇后 ）
//
// Related Topics 回溯算法


import java.util.ArrayList;
import java.util.List;

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    /**
     * 回溯算法：
     * 递归遍历每一层的每一个位置，看是否能够放置一个Queen
     * 结束条件：
     * 1、有效：到达最后一层，那么返回一个解法
     * 2、无效：当前层没有合适的位置放置Queen，直接回退
     * 回溯：
     * 重置当前层的状态，继续当前层的下一个位置的递归
     * <p>
     * 递归的过程中，记录每一层可以放置Queen的位置，最后返回的时候构造结果集
     *
     * @param n
     * @return
     */
    public List<List<String>> solveNQueens(int n) {
        if (n <= 0) return null;
        List<List<String>> queens = new ArrayList<>(); // 记录Queen的位置
        List<Integer> res = new ArrayList<>(); // 记录当前位置的竖上是否有Queen
        List<Integer> pie = new ArrayList<>(); // 记录当前位置的撇上是否有Queen
        List<Integer> na = new ArrayList<>();  // 记录当前位置的捺上是否有Queen

        dfs(n, 0, queens, res, pie, na);

        return queens;
    }

    private void dfs(int n, int level, List<List<String>> queens,
                     List<Integer> res, List<Integer> pie, List<Integer> na) {
        // 终结条件
        if (n == level) {
            queens.add(queen(res, n));
            return;
        }
        // 处理当前层的数据
        for (int i = 0; i < n; i++) {
            if (canPutQueen(level, i, res, pie, na)) { // 当前位置可以放置Queen，那么更新当前位置的res、pie、na
                res.add(i);
                pie.add(level + i);
                na.add(level - i);
                // drill down next level
                dfs(n, level + 1, queens, res, pie, na);
                // 回溯
                res.remove(level);
                pie.remove(level);
                na.remove(level);
            }
        }
    }

    private List<String> queen(List<Integer> res, int n) {
        List<String> queens = new ArrayList<>();
        for (int col : res) {
            StringBuilder sb = new StringBuilder();
            for (int j = 0; j < col; ++j) sb.append(".");
            sb.append("Q");
            for (int j = 0; j < n - col - 1; ++j) sb.append(".");
            queens.add(sb.toString());
        }
        return queens;
    }

    private boolean canPutQueen(int level, int i, List<Integer> res, List<Integer> pie, List<Integer> na) {
        for (Integer r : res) {
            if (i == r) return false;
        }
        for (Integer p : pie) {
            if (level + i == p) return false;
        }
        for (Integer n : na) {
            if (level - i == n) return false;
        }
        return true;
    }

//    public static void main(String[] args) {
//
//        List<List<String>> lists = new Solution1().solveNQueens(4);
//        System.out.println(lists);
//    }

}
//leetcode submit region end(Prohibit modification and deletion)
