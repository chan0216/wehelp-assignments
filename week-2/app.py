#要求一：函式與流程控制
def calculate(min, max):
    sum=0
    for i in range(min,max+1):
        sum=sum+min
        min+=1
    print(sum)    
calculate(1, 3) 
calculate(4, 8) 

#要求二：Python 字典與列表
def avg(data):
    i=0
    sum=0
    while i<len(data["employees"]):
        sum=sum+data["employees"][i]["salary"]
        i+=1
    mean=sum/len(data["employees"])
    print(mean)
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
}
]
})

#要求三：演算法
def maxProduct(nums):
        res =float('-inf')
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i]*nums[j] > res :
                    res = (nums[i])*(nums[j])
        print (res)

maxProduct([5, 20, 2, 6]) 
maxProduct([10, -20, 0, 3]) 
maxProduct([-1, 2]) 
maxProduct([-1, 0, 2])
maxProduct([-1, -2, 0]) 

#要求四：演算法
def twoSum(nums, target):
    n=len(nums)
    for i in range(n):
        for j in range(n):
            if nums[i]+nums[j]==target:
                return [i,j]

result=twoSum([2, 11, 7, 15], 9)
print(result) 

#要求五 ( Optional )：演算法
def maxZeros(nums):
        count = 0
        maxcount = 0
        for i in range(0, len(nums)) :
            if (nums[i] == 0): 
                count += 1
            else:
                maxcount=max(maxcount,count)
                count=0
        maxcount=max(maxcount,count)
        print(maxcount)

maxZeros([0, 1, 0, 0]) 
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) 
maxZeros([1, 1, 1, 1, 1]) 
maxZeros([0, 0, 0, 1, 1]) 


