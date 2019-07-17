//4	Median of Two Sorted Arrays


//1. 假设nums1.length = m, nums2.length = n; m < n;
//2. 若(m + n) % 2 == 0, 表示两数组之和为偶数，应该是有两个中位数，因此最终结果为第9行的代码所示。否则，结果为第7行的代码所示。
//3. 为了使得方法的统一，在最初时，对数组进行处理，统一使得传进方法的短数组为nums1，即第14行代码所示。
//4. 如果len1-start1 == 0,则表示nums1已经全部加入前k个了，则第k个为nums2[k -1]; 在方法findKth（）中的k是一直变化的，初始时，k为两个数组中排序之后的第k个数的位置；k在方法中的真正含义为“还需要找到多少个数才能达到k个”；因此假设nums1.length ==0;,此时len1-start1 == 0, 则中位数就是nums2[k - 1],即在nums1中找到了0个数，还需要找k个数，第k个数就是nums[k - 1];
//5. 如果k == 1,则表示前k-1小的数已经找过了，则第k个数肯定是nums1[start1]和nums2[start2]中较小的那个数。
//6. 下面接着就是常规的情况：即nums1中包含一部分k,nums2中也包含一部分的k,因此就从每个数组的k/2那里开始比较（也相当于每次都会有一半的数被加入前k个，因此时间复杂度为O（log(m + n)））：
// 采用p1和p2分别记录当前nums1和nums2需要比较的那个位，由于nums1比较短，因此有可能2/k的位置已经超出了nums1的长度，因此nums1还需要做特殊处理，即第19行代码所示；由于p1做了特殊处理，那p2也就要做特殊处理。总之，start1~p1和start2~p2的和一定为k。
// 1）若nums1[p1 - 1] < nums[p2 - 1],则表明【start1, p1)之间的值在前k个数中；
// 2）若nums[p1 - 1] > nums2[p2- 1],则表明【start2, p2)之间的值在前k个数中；
// 3）若两值相等，则表明【start1, p1)+【start2， p2）的个数为k,则结果直接返回其中一个即可。
//为什么比较的p1和p2的前一个位的数，而不是p1和p2位置的数呢？ 举例说明：假设start1== start2 == 0, 则p1 = Math.min(len1, k / 2); p2 = k - p1,即p1 + p2 == k;；假设p1 = 5, p2 = 7;, 则k = 12; 在数组中nums[5]其实是第6个数，nums[7]其实是第8个数，所以我们比较的是nums1[p1 - 1]与nums2[p2 - 1]的值；

public class Solution {
      public double findMedianSortedArrays(int[] nums1, int[] nums2) {
          int len1 = nums1.length;
          int len2 = nums2.length;
          int size = len1 + len2;
          if(size % 2 == 1)
              return findKth(nums1, 0, len1, nums2, 0, len2, size / 2 + 1);
          else
              return (findKth(nums1, 0, len1, nums2, 0, len2, size / 2) + findKth(nums1, 0, len1, nums2, 0, len2, size / 2 + 1)) /2;
     }
     public double findKth(int[] nums1, int start1, int len1, int[] nums2, int start2, int len2, int k)
     {
         if(len1 - start1 > len2 -start2)  // 传进来的时候统一让短的数组为nums1
             return findKth(nums2, start2, len2, nums1, start1, len1, k);
         if(len1 - start1 == 0)  // 表示nums1已经全部加入前K个了，第k个为nums2[k - 1];
             return nums2[k - 1];
         if(k == 1)
             return Math.min(nums1[start1], nums2[start2]); // k==1表示已经找到第k-1小的数，下一个数为两个数组start开始的最小值
         int p1 = start1 + Math.min(len1 - start1, k / 2); // p1和p2记录当前需要比较的那个位
         int p2 = start2 + k - p1 + start1;
         if(nums1[p1 - 1] < nums2[p2 - 1])
             return findKth(nums1,  p1, len1, nums2, start2, len2, k - p1 + start1);
         else if(nums1[p1 - 1] > nums2[p2 -1])
             return findKth(nums1, start1, len1, nums2, p2, len2, k - p2 + start2);
         else
             return nums1[p1 - 1];

     }
 }
