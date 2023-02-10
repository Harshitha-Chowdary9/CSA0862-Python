def solve(nums):
    count=0
    n=len(nums)
    for i in range(n):
        for j in range(i+1,n):
            if nums[i]==nums[j]:
                count+=1
    return count

nums=list(map(int,input("Enter a list of numbers separated by space: ").strip().strip().split()))
print(solve(nums))
