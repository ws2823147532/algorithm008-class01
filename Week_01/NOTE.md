[TOC]



学习笔记

#### Homework

#### 数据结构

##### Array

###### WHAT

数组是最基础的一种数据结构，但也是最重要的一种数据结构，它表示了内存中的一段`连续的内存地址`，可以根据元素的下标直接访问元素的内容，但是由于数组最简单，以至于他`没有其他额外的信息`给到人，所以数组的查找工作是O(n)的时间复杂度

> 蕴含的信息：内存起始地址、元素数量、下标、单个元素占用的内存大小

###### 特性

- 内存连续性

  > 内存连续的特点导致数组使用的时候会有一些限制：
  >
  > ​	1、必须要求内存空间是足够且连续的，否则空间申请会失败
  >
  > ​	2、查找、插入、删除、扩容的时间复杂度是O(n)的

- 支持随机访问

  - 寻址公式：a[i]_address = base_address + i * data_type_size
  - data_type_size 在各种不同的语言中定义有所不同，常见的data_type有：byte、int、long、float、double

- 查找、插入、删除、扩容的时间复杂度是O(n)

###### 常用解题思路

- 双指针：

  - 快慢指针：一个跑得慢，一个跑的快   如：[[283]移动零](<https://leetcode-cn.com/problems/move-zeroes/>)
  - 双向指针：从两头开始，往中间夹击

- 两个有序数组的合并：这是mergesort的简化版吗   时间复杂度O(n)

  > step1、先申请一个能盛下两个数组所有元素的新数组
  >
  > step2、从后往前或者从前往后依次遍历两个数组，按照大小顺序将元素写入新数组



###### 常见的问题

- 什么叫做原地排序

  > 指在排序过程中不申请多余的存储空间，只利用原来存储待排数据的存储空间进行比较和交换的数据排序

- 数组下标越界异常 ArrayIndexOutOfBoundsException(java)\IndexError(python)



###### Tips

- 可以通过在数组头部预留一点空间，使得preppend操作的时间复杂度减小到O(1)，但是预留的空间不能太大
- 二分查找：可以在有序数组中实现O(log n)的时间复杂度

###### JAVA中对数组的封装学习

- ArrayList





##### Linked List

###### WHAT

链表是除了数组之外的另一个基础的数组结构，他的结构比数组要稍微复杂一点，因为他要打破数组的那种必须要连续的内存空间才能使用的特性，所以链表的每一个节点势必要保留下一个节点的内存地址，这样才能将离散的内存空间连起来，所以链表的查找工作是O(n)的时间复杂度

> 头结点、下一个节点的地址、尾节点、上一个节点的地址(双向链表)

###### 特性

- 节点离散的分布在内存的各个地址

- 理论上没有内存的限制，除非内存大小不够

- 查找时间复杂度 O(n)

- 插入、删除的时间复杂度都是O(1)

  > 思考🤔：从Linked List的特性中可以看出来，链表有一个致命的缺陷，那就是查找的时间复杂度是O(n)的，这就导致：虽然它的插入、删除很高效，但是在插入和删除之前还是需要找到对应的节点。所以如果能实现找到对应节点的时间复杂度降低，那就非常完美了。
  >
  > Map结构就可以实现找到元素的O(1)的时间复杂度，但是呢，如果没有额外的需求，只需要map就足矣了，也没有使用链表的必要了。故如果有要求 除了要达到 查找元素的时间复杂度为O(1)的同时，还需要元素之间满足某种关系，比如我要求最不经常使用的节点在容量不够的时候可以自动释放掉，而经常使用的节点要保留下来，这就可以使用Map和链表(双向链表)的结合来实现。也就是下面要说的LRU cache
  >
  > 可能还有其他的应用，我这里暂时还没有接触到...



###### 衍生的数据结构

- 双向链表：每个节点记录上一个节点的地址
- 循环链表：尾节点的next指针指向头结点

###### 常用解题思路

- 快慢指针：链表的有环检测 [快慢指针](<https://code-examples.net/zh-CN/q/4e4806>)
- stack：链表翻转
- 递归：

###### 常见的问题

- 节点指针交换时需要注意

  > 遍历的时候，只能处理当前节点的前驱节点，如果要改变当前节点的后驱，那么一定要先保存原始的后驱节点
  >
  > ```python
  > def reverseList1(self, head: ListNode) -> ListNode:
  >     prev = None
  >     curr = head
  >     while curr:
  >         tmp = curr.next
  >         curr.next = prev
  >         prev = curr
  >         curr = tmp
  >     return prev
  > ```

###### Tips

- 哨兵 [Sentinel](<https://blog.csdn.net/w453908766/article/details/50916790>) [2](<https://www.520mwx.com/view/9054>)

  > sentinel往往能够简化边界条件，从而防止对特殊条件的判断，使代码更为简便优雅，在链表中应用最为典型。
  >
  > ```java
  > // 无哨兵的情况
  > // 在链表的尾部添加一个节点。那么就需要判断头结点是否为空，
  > // 为空的话，直接new一个新的节点，并将头结点指向该节点
  > // 否则的话，遍历链表，找到最后一个节点，然后在链表的尾部添加这个节点
  > void addLast(int x) {
  >     if (first == null) {
  >         first = new Node(x, null);
  >         return;
  >     }
  >     Node p = first;
  >     while (p.next != null) {
  >         p = p.next;
  >     }
  >     p.next = new Node(x, null);
  > }
  > 
  > // 有哨兵的情况
  > // 不需要特殊判断头结点是否为空，因为肯定不为空
  > // 操作就变得十分的简洁
  > void addLast(int x) {
  >     Node p = first;
  >     while (p.next != null) {
  >         p = p.next;
  >     }
  >     p.next = new Node(x, null);
  > }
  > 
  > // 删除指定节点、删除指定位置的节点、在某节点前插入指定节点、在指定位置插入节点
  > // 在没有哨兵的情况下，都需要对头结点是否为空做特殊判断
  > ```



###### JAVA中对链表的封装学习

- LinkedList

  >



##### Skip List

###### WHAT

对于有序的链表进行升维操作(使用类似二分查找的方案)，从而加速元素的查询，可以使得查询的时间复杂度变成$$O(log n)$$

当数据量很大的时候，建立索引的层级越多，需要占用的额外存储 空间也就越多，这样就涉及到如何权衡空间与效率的问题。 另外如果底层的原始链表会经常变化，新增或删除 元素都会导致索引的改变，如果变化频率过高，最终索引的位置可能并不理想，例如两个索引之间相隔的元素太多 会导致查询效率下降。

#### 其他

##### 递归的解题思路

> 找出递归公式，我的一般思路是：当前的问题需要借助下一个问题的结果，那就假设当前的问题解决了，直接去解决下一个问题，直到到达了结束条件，返回。反过来看的话，就是拿着下一个问题的结果(**已知下一个问题的结果**)来解决当前的问题
>
> 找到结束条件，结束条件不对可能导致死循环，直到最后栈溢出(**Stack Overflow**)
>
> 优化：
>
> ​	记忆式递归：如果分析中发现，在递归的过程中会有很多的重复计算单元，可以把相应的计算结果缓存下来
>
> ​	尾递归：这个是编译器对递归的优化，要求使用的高级语言支持尾递归优化(Python并没有支持，但是可以使用其他的方式来间接的优化，比如改成生成器的模式———需要再研究下[...](<https://zhuanlan.zhihu.com/p/37060182>) )



##### 工程中的运用

###### LRU cache [推荐阅读](<https://www.jianshu.com/p/b1ab4a170c3c>)

- LRU：Least Recently Used - 最近最少使用算法

- cache：缓存

  > 从本质上来说，缓存之所以有效是因为程序和数据的局部性（locality）。程序会按固定的顺序执行，数据会存放在连续的内存空间并反复读写。这些特点使得我们可以缓存那些经常用到的数据，从而提高读写速度
  >
  > 缓存的大小是固定的，它应该只保存最常被访问的那些数据。然而未来不可预知，我们只能从过去的访问序列做预测，于是就有了各种各样的缓存替换策略。本文介绍一种简单的缓存策略，称为最近最少使用（LRU，Least Recently Used）算法。

  LRU cache需要满足的条件是：

  - 查找和插入(更新)一条数据的时间复杂度是O(1)   -  HashMap
  - 能够按照元素的访问情况排序：当缓存空间不够的时候，先删除那些不经常被访问的元素  -  双向链表

  设计方案：

  - 使用HashMap存储元素节点，以达到O(1)的时间复杂度读写数据
  - 使用双向链表维持元素的访问情况：
    - 将新加的节点、新访问的节点、新更新的节点移动到链表的尾部
    - 如果缓存空间不足，则删除头部的节点(最不常用的元素)

###### Redis中对跳表的使用 [跳表](<https://redisbook.readthedocs.io/en/latest/internal-datastruct/skiplist.html>)

跳跃表在 Redis 的唯一作用， 就是实现有序集数据类型 

java中也有对skiplist的实现：java.util.concurrent.ConcurrentSkipListMap









 ##### 作业一：用add first或add last这套新的API改写Deque的代码

```java
// push -> addFirst
// pop -> removeFirst
Deque<String> deque = new LinkedList<String>();
deque.addFirst("a");
deque.addFirst("b");
deque.addFirst("c");
System.out.println(deque);
String str = deque.peek();
System.out.println(str);
System.out.println(deque);
while (deque.size() > 0) {
 System.out.println(deque.removeFirst());
}
System.out.println(deque);
```



##### 作业二：分析Queue和Priority Queue的源码

###### Queue

设计了一套支持队列操作的接口，它的Class Diagram如下：

|         | Method    | Return  | Comment                                                      |
| ------- | --------- | ------- | ------------------------------------------------------------ |
| Insert  | add(E)    | boolean | 向队列添加一个元素，如果没有空间会抛出IllegalStateException  |
| Insert  | offer(E)  | boolean | 向队列添加一个元素，如果没有空间会返回special value          |
| Remove  | remove()  | E       | 移除并返回头结点，如果队列为空的话，会抛NoSuchElementException |
| Remove  | poll()    | E       | 移除并返回头结点，如果队列为空的话，会返回null               |
| Examine | element() | E       | 返回头结点，如果队列为空的话，会抛NoSuchElementException     |
| Examine | peek()    | E       | 返回头结点，如果队列为空的话，会返回null                     |



###### Priority Queue [jdk8]

方法同Queue

```java
// 删除了一些额外的方法和内部类，只保留了主要的方法和字段
// 关于最小堆的调整就暂时不做分析了
public class PriorityQueue<E> extends AbstractQueue<E>
    implements java.io.Serializable {

    private static final long serialVersionUID = -7720805057305804111L;

    private static final int DEFAULT_INITIAL_CAPACITY = 11; // 默认的容量是11

    transient Object[] queue; // 使用一维数组存储队列的数据。transient关键字表示序列化的时候会被排除

    private int size = 0; // 队列当前大小

    private final Comparator<? super E> comparator; // 优先级比较器

    transient int modCount = 0; // 

    
    private static final int MAX_ARRAY_SIZE = Integer.MAX_VALUE - 8; // 队列最大大小

    private void grow(int minCapacity) {
        int oldCapacity = queue.length;
        // Double size if small; else grow by 50%
        int newCapacity = oldCapacity + ((oldCapacity < 64) ?
                                         (oldCapacity + 2) :
                                         (oldCapacity >> 1));
        // 如果新增的空间 比 MAX_ARRAY_SIZE还要大，那么在minCapacity基础上重新计算容量
        if (newCapacity - MAX_ARRAY_SIZE > 0)
            newCapacity = hugeCapacity(minCapacity);
        // 调用System.arraycopy() 实现快速的数组拷贝
        queue = Arrays.copyOf(queue, newCapacity);
    }

    private static int hugeCapacity(int minCapacity) {
        if (minCapacity < 0) // overflow
            throw new OutOfMemoryError();
        return (minCapacity > MAX_ARRAY_SIZE) ?
            Integer.MAX_VALUE :
            MAX_ARRAY_SIZE;
    }

    public boolean add(E e) {
        return offer(e);
    }

    public boolean offer(E e) {
        if (e == null)
            throw new NullPointerException();
        modCount++;
        int i = size;
        if (i >= queue.length)
            grow(i + 1); // 如果当前队列的大小已经大于等于队列的容量，那么就进行扩容操作
        size = i + 1;
        if (i == 0)
            queue[0] = e;
        else
            siftUp(i, e);
        return true;
    }

    @SuppressWarnings("unchecked")
    public E peek() {
        return (size == 0) ? null : (E) queue[0];
    }

    private int indexOf(Object o) {
        if (o != null) {
            for (int i = 0; i < size; i++)
                if (o.equals(queue[i]))
                    return i;
        }
        return -1;
    }

    public boolean remove(Object o) {
        int i = indexOf(o);
        if (i == -1)
            return false;
        else {
            removeAt(i);
            return true;
        }
    }

    boolean removeEq(Object o) {
        for (int i = 0; i < size; i++) {
            if (o == queue[i]) {
                removeAt(i);
                return true;
            }
        }
        return false;
    }

    public boolean contains(Object o) {
        return indexOf(o) != -1;
    }

    public int size() {
        return size;
    }

    /**
     * Removes all of the elements from this priority queue.
     * The queue will be empty after this call returns.
     */
    public void clear() {
        modCount++;
        for (int i = 0; i < size; i++)
            queue[i] = null;
        size = 0;
    }

    @SuppressWarnings("unchecked")
    public E poll() {
        if (size == 0)
            return null;
        int s = --size;
        modCount++;
        E result = (E) queue[0];
        E x = (E) queue[s];
        queue[s] = null;
        if (s != 0)
            siftDown(0, x);
        return result;
    }

    @SuppressWarnings("unchecked")
    private E removeAt(int i) {
        // assert i >= 0 && i < size;
        modCount++;
        int s = --size;
        if (s == i) // removed last element
            queue[i] = null;
        else {
            E moved = (E) queue[s];
            queue[s] = null;
            siftDown(i, moved);
            if (queue[i] == moved) {
                siftUp(i, moved);
                if (queue[i] != moved)
                    return moved;
            }
        }
        return null;
    }

    private void siftUp(int k, E x) {
        if (comparator != null)
            siftUpUsingComparator(k, x);
        else
            siftUpComparable(k, x);
    }

    @SuppressWarnings("unchecked")
    private void siftUpComparable(int k, E x) {
        Comparable<? super E> key = (Comparable<? super E>) x;
        while (k > 0) {
            int parent = (k - 1) >>> 1;
            Object e = queue[parent];
            if (key.compareTo((E) e) >= 0)
                break;
            queue[k] = e;
            k = parent;
        }
        queue[k] = key;
    }

    @SuppressWarnings("unchecked")
    private void siftUpUsingComparator(int k, E x) {
        while (k > 0) {
            int parent = (k - 1) >>> 1;
            Object e = queue[parent];
            if (comparator.compare(x, (E) e) >= 0)
                break;
            queue[k] = e;
            k = parent;
        }
        queue[k] = x;
    }


    private void siftDown(int k, E x) {
        if (comparator != null)
            siftDownUsingComparator(k, x);
        else
            siftDownComparable(k, x);
    }

    @SuppressWarnings("unchecked")
    private void siftDownComparable(int k, E x) {
        Comparable<? super E> key = (Comparable<? super E>)x;
        int half = size >>> 1;        // loop while a non-leaf
        while (k < half) {
            int child = (k << 1) + 1; // assume left child is least
            Object c = queue[child];
            int right = child + 1;
            if (right < size &&
                ((Comparable<? super E>) c).compareTo((E) queue[right]) > 0)
                c = queue[child = right];
            if (key.compareTo((E) c) <= 0)
                break;
            queue[k] = c;
            k = child;
        }
        queue[k] = key;
    }

    @SuppressWarnings("unchecked")
    private void siftDownUsingComparator(int k, E x) {
        int half = size >>> 1;
        while (k < half) {
            int child = (k << 1) + 1;
            Object c = queue[child];
            int right = child + 1;
            if (right < size &&
                comparator.compare((E) c, (E) queue[right]) > 0)
                c = queue[child = right];
            if (comparator.compare(x, (E) c) <= 0)
                break;
            queue[k] = c;
            k = child;
        }
        queue[k] = x;
    }

    @SuppressWarnings("unchecked")
    private void heapify() {
        for (int i = (size >>> 1) - 1; i >= 0; i--)
            siftDown(i, (E) queue[i]);
    }
}
```



















