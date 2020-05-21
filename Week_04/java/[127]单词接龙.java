//给定两个单词（beginWord 和 endWord）和一个字典，找到从 beginWord 到 endWord 的最短转换序列的长度。转换需遵循如下规则：
//
//
//
// 每次转换只能改变一个字母。
// 转换过程中的中间单词必须是字典中的单词。
//
//
// 说明:
//
//
// 如果不存在这样的转换序列，返回 0。
// 所有单词具有相同的长度。
// 所有单词只由小写字母组成。
// 字典中不存在重复的单词。
// 你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
//
//
// 示例 1:
//
// 输入:
//beginWord = "hit",
//endWord = "cog",
//wordList = ["hot","dot","dog","lot","log","cog"]
//
//输出: 5
//
//解释: 一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog",
//     返回它的长度 5。
//
//
// 示例 2:
//
// 输入:
//beginWord = "hit"
//endWord = "cog"
//wordList = ["hot","dot","dog","lot","log"]
//
//输出: 0
//
//解释: endWord "cog" 不在字典中，所以无法进行转换。
// Related Topics 广度优先搜索


import javafx.util.Pair;

import java.util.Arrays;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Set;

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        Set<String> dict = new HashSet<>(wordList);
        // 如果endWord不存于字典，返回0
        if (!dict.contains(endWord)) return 0;

        char[] chars = new char[26];
        for (int i = 0; i < 26; i++) chars[i] = (char) ('a' + i);

        Queue<Pair<String, Integer>> queue = new LinkedList<>();
        queue.offer(new Pair<>(beginWord, 1));
        while (!queue.isEmpty()) {
            Pair<String, Integer> current = queue.poll();
            if (current != null) {
                char[] currChars = current.getKey().toCharArray();
                for (int i = 0; i < current.getKey().length(); i++) {
                    char tmpChar = currChars[i];
                    for (char aChar : chars) {
                        currChars[i] = aChar;
                        String targetStr = new String(currChars);
                        if (targetStr.equals(endWord)) return current.getValue() + 1;
                        if (dict.contains(targetStr)) {
                            queue.offer(new Pair<>(targetStr, current.getValue() + 1));
                            dict.remove(targetStr);
                        }
                    }
                    currChars[i] = tmpChar;
                }
            }
        }
        return 0;
    }

    public static void main(String[] args) {

        Solution1 solution1 = new Solution1();

        System.out.println(solution1.ladderLength("hit", "cog",
                Arrays.asList("hot", "dot", "dog", "lot", "log", "cog")));
    }
}
//leetcode submit region end(Prohibit modification and deletion)
