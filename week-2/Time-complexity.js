//要求三：演算法，時間複雜度是O(n2)
function maxProduct(nums) {
  let max = -Infinity;
  const length = nums.length;
  for (let i = 0; i < length; i++) {
    for (let j = i + 1; j < length; j++) {
      max = Math.max(max, nums[i] * nums[j]);
    }
  }
  console.log(max);
}
maxProduct([5, 20, 2, 6]);
maxProduct([10, -20, 0, 3]);
maxProduct([-1, 2]);
maxProduct([-1, 0, 2]);
maxProduct([-1, -2, 0]);

//要求五 ( Optional )：演算法，時間複雜度是O(n)
function maxZeros(nums) {
  let maxcount = 0;
  let count = 0;
  const n = nums.length;
  for (let i = 0; i < n; i++) {
    if (nums[i] === 0) {
      count++;
    } else {
      maxcount = Math.max(maxcount, count);
      count = 0;
    }
  }
  maxcount = Math.max(maxcount, count);
  console.log(maxcount);
}
maxZeros([0, 1, 0, 0]);
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]);
maxZeros([1, 1, 1, 1, 1]);
maxZeros([0, 0, 0, 1, 1]);
