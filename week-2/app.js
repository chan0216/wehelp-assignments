//要求一：函式與流程控制
function calculate(min, max){
    let sum=0
    for(let i=min;i<=max;i++){
        sum=sum+min
        min++
    }
    console.log(sum)
}
calculate(1, 3); 
calculate(4, 8); 

//要求二：JavaScript 物件與陣列
function avg(data){
    let sum=0
    for(let i=0;i<data.employees.length;i++){
        sum+=data.employees[i]["salary"]
    }
    let mean=sum/data.employees.length
    console.log (mean)
}
avg({
"count":3,
"employees":[
{
"name":"John",
"salary":30000
},
{
"name":"Bob",
"salary":60000
},
{
"name":"Jenny",
"salary":50000
},
]
}); 

//要求三：演算法
function maxProduct(nums){
    let max =-Infinity;
    const length = nums.length;
    for (let i = 0; i < length; i++) {
        for (let j = i +1; j < length; j++) {
        max = Math.max(max,(nums[i]) * (nums[j]));
        }
    }
    console.log(max) 
}    
maxProduct([5, 20, 2, 6]) 
maxProduct([10, -20, 0, 3]) 
maxProduct([-1, 2]) 
maxProduct([-1, 0, 2]) 
maxProduct([-1, -2, 0])     

//要求四 ：演算法
function twoSum(nums, target){
    for(let i=0;i<nums.length;i++){
        for(let j=1;j<nums.length;j++){
            if(nums[i]+nums[j]==target){
                let answer=new Array(i,j)
                return answer
                }
            }
        }
    }
let result=twoSum([2, 11, 7, 15], 9);
console.log(result); 
  
//要求五 ( Optional )：演算法
function maxZeros(nums){
    let maxcount = 0
    let count = 0;
    const n = nums.length;
    for (let i=0;i<n;i++) {
        if (nums[i] === 0) {
                count++;
        }else {
            maxcount = Math.max(maxcount, count);
            count = 0;
        }
    }
    maxcount = Math.max(maxcount, count);
    console.log(maxcount);
};
    maxZeros([0, 1, 0, 0]); 
    maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]); 
    maxZeros([1, 1, 1, 1, 1]); 
    maxZeros([0, 0, 0, 1, 1]) 


 