#### 算法分类

十种常见排序算法可以分为两大类：

- **比较类排序**：通过比较来决定元素间的相对次序，由于其时间复杂度不能突破O(nlogn)，因此也称为非线性时间比较类排序。
- **非比较类排序**：不通过比较来决定元素间的相对次序，它可以突破基于比较排序的时间下界，以线性时间运行，因此也称为线性时间非比较类排序。

![排序算法1](/images/%E6%8E%92%E5%BA%8F%E7%AE%97%E6%B3%951.png)

### 算法复杂度

![排序算法](/images/%E6%8E%92%E5%BA%8F%E7%AE%97%E6%B3%95.png)

### 相关概念

- **稳定**：如果a原本在b前面，而a=b，排序之后a仍然在b的前面。
- **不稳定**：如果a原本在b的前面，而a=b，排序之后 a 可能会出现在 b 的后面。
- **时间复杂度**：对排序数据的总的操作次数。反映当n变化时，操作次数呈现什么规律。
- **空间复杂度：**是指算法在计算机

内执行时所需存储空间的度量，它也是数据规模n的函数

[参考](https://www.cnblogs.com/onepixel/p/7674659.html)

### O(n^2)

#### 冒泡排序(Bubble Sort)

> 算法描述

冒泡排序只会操作相邻的两个数据。每次冒泡操作都会对相邻的两个元素进行比较，看是否符合大小关系要求。如果不满足就互换位置。一次冒泡至少会让一个元素移动到它应该在的位置，重复n次，就完成了n个元素的排序工作。

![冒泡](/images/%E5%86%92%E6%B3%A1.png)

> 算法实现

```python
def bubble_sort(nums):
    """
    冒泡排序：从小到大
    :param nums:
    :return:
    """
    if len(nums) <= 1:
      return nums
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]

    return nums
  
def bubble_sort1(nums):
    if len(nums) <= 1:
      return nums
    for i in range(len(nums) - 1):
        for j in range(len(nums) - 1 - i):
            if nums[j] > nums[j + i]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


if __name__ == '__main__':
    nums = [-23, 0, 6, -4, 34]
    print(bubble_sort(nums))
```



#### 插入排序

> 算法描述

将一个元素插入一个已经有序的序列，使其依然有序。首先，将原始的序列分为两个子序列，有序的和无序的，然后，从无序的序列中依次拿出一个元素，插入到有序的序列的合适位置，并保持有序的序列依然有序，直到无序的序列中没有元素了。

![插入排序](/images/%E6%8F%92%E5%85%A5%E6%8E%92%E5%BA%8F.png)

> 算法实现

```python
def insert_sort(nums):
    if len(nums) <= 1:
        return nums
    for i in range(1, len(nums)):  # 遍历无序数组的每一个元素
        tmp = nums[i]  # 待插入元素
        j = i - 1  # 待插入子数组
        for j in range(i - 1, -1, -1):  # 从后往前遍历待插入子数组
            if tmp >= nums[j]: break  # tmp大于等于当前元素，停止遍历   
                					# 相等元素不会改变其相对位置，故是稳定的
            nums[j + 1] = nums[j]  # 将nums[j]后移1个位置
        nums[j + 1] = tmp  # 插入待插入元素 tmp

    return nums
 
if __name__ == '__main__':
    nums = [-23, 0, 6, -4, 34, 2]
    print(insert_sort(nums))
```



#### 选择排序

> 算法描述

选择排序是选择无序序列中的最小的元素放到有序序列的末尾，直到无序序列没有元素。

![插入排序](/images/%E9%80%89%E6%8B%A9%E6%8E%92%E5%BA%8F.png)

> 算法实现

```python
def selection_sort(nums):
    if len(nums) <= 1:
        return nums
    for i in range(len(nums) - 1):  # 遍历无序数组的每一个元素
        # i和nums[i]
        min_val = nums[i] 
        min_j = i
        for j in range(i + 1, len(nums)):  # 寻找剩余待排数组的最小元素
            if min_val > nums[j]:
                min_val = nums[j]
                min_j = j
        nums[i], nums[min_j] = nums[min_j], nums[i]  # 交换最小元素和
    return nums


if __name__ == '__main__':
    nums = [-23, 0, 6, -4, 34, 2]
    print(selection_sort(nums))
```



#### 希尔排序

> 算法描述

```
希尔排序是对插入排序的优化。
希尔排序，通过将原始序列按照一定的步长划分为多个子序列
	将原始的一维数组映射成二维数组，
	然后按列进行插入排序，
这样的话，可以让一个元素在一次比较中跨越较大的区间，随后算法在使用较小的步长，一直到步长为1
(已知当对有序度较高数组进行排序时，插入排序的时间复杂度接近O(N)，因此可以大幅度提高插入排序的效率)。
```

![希尔排序](/images/%E5%B8%8C%E5%B0%94%E6%8E%92%E5%BA%8F.png)

> 维基百科：https://zh.wikipedia.org/wiki/%E5%B8%8C%E5%B0%94%E6%8E%92%E5%BA%8F

> 算法实现

```python
def shell_sort(list):
    n = len(list)
    # 初始步长
    gap = n // 2
    while gap > 0:
        print(gap)
        for i in range(gap, n):
            # 每个步长进行插入排序
            temp = list[i]
            j = i
            # 插入排序
            while j >= gap and list[j - gap] > temp:
                list[j] = list[j - gap]
                j -= gap
                print('inner=', list)
            list[j] = temp
        print(list)
        # 得到新的步长
        gap = gap // 2
    return list


def shell_sort1(collection):
    # Marcin Ciura's gap sequence
    gaps = [701, 301, 132, 57, 23, 10, 4, 1]

    for gap in gaps:
        i = gap
        while i < len(collection):
            temp = collection[i]
            j = i
            while j >= gap and collection[j - gap] > temp:
                collection[j] = collection[j - gap]
                j -= gap
            collection[j] = temp
            i += 1

    return collection


if __name__ == '__main__':
    nums = [-23, 0, 6, -4, 34, 2]
    print('\n', shell_sort1(nums))

```



### O(nlogn)

#### 归并排序

> 算法描述

将数组分为两部分，分别排序，最后将两部分排好序的数组合并成一个有序的数组。利用递归的方式，重复上述过程。

![归并排序](/images/%E5%BD%92%E5%B9%B6%E6%8E%92%E5%BA%8F.png)

> 算法实现

```python
def merge_sort(nums):
    print('before=', nums)
    length = len(nums)
    if length > 1:
        midpoint = length // 2
        left_half = merge_sort(nums[:midpoint])
        right_half = merge_sort(nums[midpoint:])
        i = 0
        j = 0
        k = 0
        left_length = len(left_half)
        right_length = len(right_half)
        while i < left_length and j < right_length:
            if left_half[i] < right_half[j]:
                nums[k] = left_half[i]
                i += 1
            else:
                nums[k] = right_half[j]
                j += 1
            k += 1

        while i < left_length:
            nums[k] = left_half[i]
            i += 1
            k += 1

        while j < right_length:
            nums[k] = right_half[j]
            j += 1
            k += 1
    print('after=', nums)

    return nums


if __name__ == '__main__':
    nums = [-23, 0, 6, -4, 34, 2]
    print('\n', merge_sort(nums))

```

```python
def merge_sort(nums, left, right):
    if left >= right: return
    mid = (left + right) >> 1  # 二分
    merge_sort(nums, left, mid)  # 排列左半部分
    merge_sort(nums, mid + 1, right)  # 排列右半部分
    merge(nums, left, mid, right)  # 合并左右两个已经有序的数组


def merge(nums, left, mid, right):
    tmp = [0] * (right - left + 1)
    i, j, k = left, mid + 1, 0
    while i <= mid and j <= right:
        if nums[i] < nums[j]: tmp[k], i = nums[i], i + 1
        else: tmp[k], j = nums[j], j + 1
        k += 1
    while i <= mid: tmp[k], k, i = nums[i], k + 1, i + 1
    while j <= right: tmp[k], k, j = nums[j], k + 1, j + 1
    nums[left:right+1] = tmp[:]


nums = [-23, 0, 6, -4, 34, 2]
merge_sort(nums, 0, len(nums) - 1)
print(nums)

```

```python
def merge_sort(nums, left, right):
    if left >= right: return
    mid = (left + right) >> 1  # 二分
    merge_sort(nums, left, mid)  # 排列左半部分
    merge_sort(nums, mid + 1, right)  # 排列右半部分
    merge(nums, left, mid, right)  # 合并左右两个已经有序的数组


def merge(nums, left, mid, right):
    tmp = []
    i, j = left, mid + 1
    while i <= mid and j <= right:
        if nums[i] < nums[j]:
            tmp.append(nums[i])
            i += 1
        else:
            tmp.append(nums[j])
            j += 1
    tmp.extend(nums[i:mid + 1] if i <= mid else nums[j:right + 1])
    nums[left:right + 1] = tmp[:]


nums = [-23, 88, 4, 2, 99, 12, 0, 6, -4, 34, 2]
merge_sort(nums, 0, len(nums) - 1)
print(nums)
```

```java
// Java

public static void mergeSort(int[] array, int left, int right) {
    if (right <= left) return;
    int mid = (left + right) >> 1; // (left + right) / 2

    mergeSort(array, left, mid);
    mergeSort(array, mid + 1, right);
    merge(array, left, mid, right);
}

public static void merge(int[] arr, int left, int mid, int right) {
    int[] temp = new int[right - left + 1]; // 中间数组
    int i = left, j = mid + 1, k = 0;

    while (i <= mid && j <= right) {
        temp[k++] = arr[i] <= arr[j] ? arr[i++] : arr[j++];
    }

    while (i <= mid)   temp[k++] = arr[i++];
    while (j <= right) temp[k++] = arr[j++];

    for (int p = 0; p < temp.length; p++) {
        arr[left + p] = temp[p];
    }
    // 也可以用 System.arraycopy(a, start1, b, start2, length)
}


public static void merge(int[] arr, int left, int mid, int right) {
    int[] temp = new int[right - left + 1]; // 中间数组
    int i = left, j = mid + 1, k = 0;

    while (i <= mid && j <= right) {
        temp[k++] = arr[i] <= arr[j] ? arr[i++] : arr[j++];
    }

    if (i<=mid) System.arraycopy(arr, i, temp, k, mid-i+1);
    if (j<=right) System.arraycopy(arr, j, temp, k, right-j+1);

	System.arraycopy(arr, left, temp, 0, temp.length);
}
```



#### 快速排序

> 算法描述

随机选择一个pivot节点，然后将数组中的数据分成大于pivot和小于pivot的两部分，然后递归地将大于pivot和小于pivot的部分再按照相同的思路处理，直到每个pivot两端的部分都只有最多一个元素

![快排](/images/%E5%BF%AB%E6%8E%92.png)

> 算法实现

```python
def quick_sort(collection):
    length = len(collection)
    if length <= 1:
        return collection
    else:
        pivot = collection[0]
        greater = [element for element in collection[1:] if element > pivot]
        lesser = [element for element in collection[1:] if element <= pivot]
        return quick_sort(lesser) + [pivot] + quick_sort(greater)
```

> O(n) 时间复杂度内求无序数组中的第 K 大元素

```python
# 选择数组的最后一个元素，作为pivot，然后将数组的所有元素分为大于pivot和小于pivot的两部分，
# 如果 len(lesser) == k - 1，则返回pivot
# 如果 len(lesser) >= k，则说明要查找的元素在小于pivot的部分，那么继续在lesser中查找
# 否则的话，说明要查找的元素在大于pivot的部分，那么继续在greater中查找
def find_k_max(nums, k):
    length = len(nums)
    if length < k:
        return None
    pivot = nums[length - 1]
    greater = [element for element in nums[:length - 1] if element > pivot]
    lesser = [element for element in nums[:length - 1] if element <= pivot]
    if len(lesser) == k - 1:
        return pivot
    elif len(lesser) >= k:
        return find_k_max(lesser, k)
    else:
        return find_k_max(greater, k - len(lesser) - 1)
```

> In-place算法实现

```python
def quick_sort(nums, begin, end):
    if begin>=end: return
    pivot = partition(nums, begin, end)  # 找到[begin,end]的pivot点，pivot点已经固定了，是不需要对它进行排序的
    quick_sort(nums, begin, pivot-1)  # 递归调用nums[begin, pivot-1]
    quick_sort(nums, pivot+1, end)  # 递归调用nums[pivot+1, end]
   	return nums

def partition(nums, begin, end):
    # pivot是作为对比的值
    # last_smaller是指向小于pivot的子数组的下一个位置的指针   类似于leetcode [移动零] 那一题的解法
    pivot, last_smaller = end, begin
    
    for i in range(begin, end): # 从前往后遍历待排数组
        if nums[i]<nums[pivot]: # 如果当前元素小于pivot，那么调换当前元素和last_smaller位置的元素
            nums[i], nums[last_smaller] = nums[last_smaller], nums[i]
            last_smaller+=1  # last_smaller 向后移动一位
    # 把pivot的值移动到last_smaller位置
    nums[last_smaller], nums[pivot] = nums[pivot], nums[last_smaller]
    return last_smaller
    
    
nums = []
quick_sort(nums, 0, len(nums)-1)

```

```java
// Java
public static void quickSort(int[] array, int begin, int end) {
    if (end <= begin) return;
    int pivot = partition(array, begin, end);
    quickSort(array, begin, pivot - 1);
    quickSort(array, pivot + 1, end);
}

static int partition(int[] a, int begin, int end) {
    // pivot: 标杆位置
    // last_smaller是指向小于pivot的子数组的下一个位置的指针   类似于leetcode [移动零] 那一题的解法
    int pivot = end, last_smaller = begin;
    for (int i = begin; i < end; i++) {
        if (a[i] < a[pivot]) {
            int temp = a[last_smaller]; a[last_smaller] = a[i]; a[i] = temp;
            last_smaller++;
        }
    }
    int temp = a[pivot]; a[pivot] = a[last_smaller]; a[last_smaller] = temp;
    return counter;
}
```





#### 堆排序

> 算法描述

使用大顶堆和小顶堆的数据结构，进行排序：大顶堆，每次取堆顶元素，遍历完则得到从大到小的序列；小顶堆则相反。

堆有很多种实现，这里只看二叉堆。二叉堆是一种近似完全二叉树，所以可以使用数组存储，每个父亲节点都要比其孩子节点大(大顶堆，小顶堆相反)

利用堆进行排序，包含两个步骤：第一、将数据放入堆中以满足堆的条件；第二、将数据从堆中取出。即为有序数组

![堆排序](/images/%E5%A0%86%E6%8E%92%E5%BA%8F.png)

> 算法实现

```python
#Python

def heapify(parent_index, length, nums):
    temp = nums[parent_index]
    child_index = 2*parent_index+1 # 取到左孩子
    while child_index < length: 
        # 先检查右孩子，看右孩子是不是比左孩子大，是的话更新孩子节点索引到 右孩子
        if child_index+1 < length and nums[child_index+1] > nums[child_index]:
            child_index = child_index+1
        # 如果父结点大于孩子节点，那么停止循环
        if temp > nums[child_index]:
            break
        # 将父结点更新到新检查的孩子节点，重复上面的操作
        nums[parent_index] = nums[child_index]
        parent_index = child_index
        child_index = 2*parent_index + 1
    nums[parent_index] = temp  # 最后，把父结点元素归位


def heapsort(nums):
    ## start from (len(nums)-2)//2:看一下图就知道了
    for i in range((len(nums)-2)//2, -1, -1):
        heapify(i, len(nums), nums)
    for j in range(len(nums)-1, 0, -1):
        nums[j], nums[0] = nums[0], nums[j]
        heapify(0, j, nums)
```

![image-20200614085943287](/images/%E4%BA%8C%E5%8F%89%E5%A0%86.png)

当len=12，那么从数组下标为5开始调整，图中的6位置

当len=11，那么从数组下标为4开始调整，图中的6位置

依次类推

```java
// Java

static void heapify(int[] array, int length, int i) {
    int left = 2 * i + 1, right = 2 * i + 2；
    int largest = i;

    if (left < length && array[left] > array[largest]) {
        largest = left;
    }
    if (right < length && array[right] > array[largest]) {
        largest = right;
    }

    if (largest != i) {
        int temp = array[i]; array[i] = array[largest]; array[largest] = temp;
        heapify(array, length, largest);
    }
}

public static void heapSort(int[] array) {
    if (array.length == 0) return;

    int length = array.length;
    for (int i = length / 2-1; i >= 0; i--) 
        heapify(array, length, i);

    for (int i = length - 1; i >= 0; i--) {
        int temp = array[0]; array[0] = array[i]; array[i] = temp;
        heapify(array, i, 0);
    }
}
```



### O(n)

#### 计数排序

> 算法描述

计数排序不是基于比较的排序算法，其核心在于将输入的数据值转化为键存储在额外开辟的数组空间中。 作为一种线性时间复杂度的排序，计数排序要求输入的数据必须是有确定范围的整数。

计数排序是一个稳定的排序算法。当输入的元素是 n 个 0到 k 之间的整数时，时间复杂度是O(n+k)，空间复杂度也是O(n+k)，其排序速度快于任何比较排序算法。当k不是很大并且序列比较集中时，计数排序是一个很有效的排序算法。

步骤

- 找出待排序的数组中最大和最小的元素；
- 统计数组中每个值为i的元素出现的次数，存入数组C的第i项；
- 对所有的计数累加（从C中的第一个元素开始，每一项和前一项相加）；
- 反向填充目标数组：将每个元素i放在新数组的第C(i)项，每放一个元素就将C(i)减去1。

使用的局限性：

1. 待排序的数组元素只能为有确定范围的整数，因为要使用数组的索引来标识元素的顺序

   有时候，小数和负数，可以通过乘以一个倍数或者加上一个正数，来调整成可以使用计数排序的形式

2. 待排序数组的范围不能太大，否则会占用大量的内存，如果数据倾斜严重，可能只会使用到一小部分的位置，会造成大量的内存白白消耗

升级：

可以使用下面要讲的桶排序，来弥补计数排序的两点不足

![计数排序](/images/%E8%AE%A1%E6%95%B0%E6%8E%92%E5%BA%8F.png)

> 算法实现

```python
max_value = 1000


def count_sort(nums):
    bucket = [0] * max_value
    for num in nums:
        bucket[num] += 1
    j = 0
    for i in range(max_value):
        nums[j:j + bucket[i]] = ([i] * bucket[i])[:]
        j += bucket[i]
    return nums


nums = [9, 2, 3, 1, 12, 3, 0, 3, 3, 3, 3, 3, 3, 4, 4, 4, 5, 56, 6, 7, 7, 78, 8, 8, 8, 8]
count_sort(nums)
print(nums)
```





#### 基数排序

> 算法描述

基数排序是按照低位先排序，然后收集；再按照高位排序，然后再收集；依次类推，直到最高位。有时候有些属性是有优先级顺序的，先按低优先级排序，再按高优先级排序。最后的次序就是高优先级高的在前，高优先级相同的低优先级高的在前。

步骤

- 取得数组中的最大数，并取得位数；
- arr为原始数组，从最低位开始取每个位组成radix数组；
- 对radix进行计数排序（利用计数排序适用于小范围数的特点）；

![849589-20171015232453668-1397662527](/images/%E5%9F%BA%E6%95%B0%E6%8E%92%E5%BA%8F.png)

基数排序基于分别排序，分别收集，所以是稳定的。但基数排序的性能比桶排序要略差，每一次关键字的桶分配都需要O(n)的时间复杂度，而且分配之后得到新的关键字序列又需要O(n)的时间复杂度。假如待排数据可以分为d个关键字，则基数排序的时间复杂度将是O(d*2n) ，当然d要远远小于n，因此基本上还是线性级别的。

基数排序的空间复杂度为O(n+k)，其中k为桶的数量。一般来说n>>k，因此额外空间需要大概n个左右。

> 算法实现

```python
def radix_sort(nums, max_digit):
    """
    max_digit 表示最大的位数
    """
    bucket = [[] for _ in range(10)]  # 十进制数每位只能有10个选择：0-9
    for digit in range(max_digit):  # 从低位开始分桶
        for num in nums:
            # 对每个数整除10的倍数 取余，填入对一个的坑位
            bucket[(num // (10 ** digit)) % 10].append(num)
        j = 0
        for i in range(10):  # 遍历10个坑位，把数据回填入nums
            nums[j:j + len(bucket[i])] = bucket[i][:]
            j += len(bucket[i])

        bucket = [[] for _ in range(10)]  # 一轮结束后，清空原来的bucket
    return nums


res = radix_sort([32, 43, 4, 54, 24, 1, 34, 3, 1, 13, 4, 4, 134, 4, 53, 34, 1, 34, 3, 3, 4, 2, 1, 4, ], 3)
print(res)
```





#### 桶排序

> 算法描述

桶排序是计数排序的升级版。它利用了函数的映射关系，高效与否的关键就在于这个映射函数的确定。桶排序 (Bucket sort)的工作的原理：假设输入数据服从均匀分布，将数据分到有限数量的桶里，每个桶再分别排序（有可能再使用别的排序算法或是以递归方式继续使用桶排序进行排）。

桶排序最好情况下使用线性时间O(n)，桶排序的时间复杂度，取决与对各个桶之间数据进行排序的时间复杂度，因为其它部分的时间复杂度都为O(n)。很显然，桶划分的越小，各个桶之间的数据越少，排序所用的时间也会越少。但相应的空间消耗就会增大

![桶排序](/images/%E6%A1%B6%E6%8E%92%E5%BA%8F.png)

> 算法实现

```python
import math

from TheAlgorithms.sorts.insert_sort import insert_sort1

DEFAULT_BUCKET_SIZE = 5


def bucket_sort(my_list, bucket_size=DEFAULT_BUCKET_SIZE):
    if len(my_list) == 0:
        print('You don\'t have any elements in array!')

    minValue = my_list[0]
    maxValue = my_list[0]

    # For finding minimum and maximum values
    for i in range(0, len(my_list)):
        if my_list[i] < minValue:
            minValue = my_list[i]
        elif my_list[i] > maxValue:
            maxValue = my_list[i]

    # Initialize buckets
    bucketCount = math.floor((maxValue - minValue) / bucket_size) + 1
    buckets = []
    for i in range(0, bucketCount):
        buckets.append([])

    # For putting values in buckets
    for i in range(0, len(my_list)):
        buckets[math.floor((my_list[i] - minValue) / bucket_size)].append(my_list[i])

    # Sort buckets and place back into input array
    sorted_array = []
    for i in range(0, len(buckets)):
        insert_sort1(buckets[i])
        for j in range(0, len(buckets[i])):
            sorted_array.append(buckets[i][j])

    return sorted_array


if __name__ == '__main__':
    sorted_array = bucket_sort([12, 23, 4, 5, 3, 2, 12, 81, 56, 95])
    print(sorted_array)

```







