学习笔记



#### DFS

递归写法

```python
visited = set() 

def dfs(node, visited):
    if node in visited: # terminator
    	# already visited 
    	return 

	visited.add(node) 

	# process current node here. 
	...
	for next_node in node.children(): 
		if next_node not in visited: 
			dfs(next_node, visited)
```

非递归写法

```python
def DFS(self, tree): 

	if tree.root is None: 
		return [] 

	visited, stack = [], [tree.root]

	while stack: 
		node = stack.pop() 
		visited.add(node)

		process (node) 
		nodes = generate_related_nodes(node) 
		stack.push(nodes) 

	# other processing work 
	...
```



#### BFS

```python
def BFS(graph, start, end):
    visited = set()
	queue = [] 
	queue.append([start]) 

	while queue: 
		node = queue.pop() 
		visited.add(node)

		process(node) 
		nodes = generate_related_nodes(node) 
		queue.push(nodes)

	# other processing work 
	...
```

#### 贪心

[leetcode的文章](<https://leetcode-cn.com/circle/article/yXFal5/>)

贪心算法是指，在对问题求解时，总是做出在当前看来是最好的选择。也就是说，不从整体最优上加以考虑，它所做出的仅仅是在某种意义上的局部最优解。

贪心算法的特征：

1. 最优子结构：贪心算法也是将原问题分解成多个性质相同的子问题，每个问题都是局部最优。
2. 贪心选择性质：在做贪心选择时，我们直接做出当前子问题中看起来最优的解，这也是贪心算法和动态规划的不同之处。
3. 遍历状态集：遍历状态集，做出局部最优选择，更新结果。
4. 无后效性：某个状态以后的过程不会影响以前的状态，只与当前状态有关。

> 贪心算法的核心性质：只适用于求解可行解，不适用于求最值以及所有解

```java
class Solution {
    public boolean canJump(int[] nums) {
        int max_pos = 0; // 最大能到达的位置
   
        // 遍历状态集
        for (int i = 0; i < nums.length; i++) {
            if (i > max_pos) return false;
            // 对每一个状态都做局部最优解
            max_pos = Math.max(max_pos, i + nums[i]);
            if (max_pos > nums.length) return true;
        }

        return true;
    }
}
```

#### 二分

```python
left, right = 0, len(array) - 1 
while left <= right: 
	  mid = (left + right) / 2 
	  if array[mid] == target: 
		    # find the target!! 
		    break or return result 
	  elif array[mid] < target: 
		    left = mid + 1 
	  else: 
		    right = mid - 1
```

作业：使用二分查找，寻找一个半有序数组 [4, 5, 6, 7, 0, 1, 2] 中间无序的地方

```python
    def find_change_point(self, nums) -> int:
        """
        返回一个半有序数组中间变作无序的index
        找不到，返回-1
        """
        if not nums or len(nums)==1 or nums[0] < nums[-1]: return -1 # nums为空或者没有发生旋转
        left, right, first = 0, len(nums) - 1, nums[0]
        while left <= right:
            mid = (left + right) >> 1
            if first < nums[mid]:  # 说明突变点在mid右侧
                if nums[mid] > nums[mid + 1]: return mid + 1  # 说明在mid+1处发生了突变
                left = mid + 1
            else:  # 说明突变点在mid左侧
                if nums[mid] < nums[mid - 1]: return mid
                if nums[mid] > nums[mid - 1]: return mid - 1
                right = mid - 1
        return -1
    
```

