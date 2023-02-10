def minJump(nums):
    jumps=0
    current_jump_end=0
    far=0
    for i in range(len(nums)-1):
        far=max(far,i+nums[i])
        if i==current_jump_end:
            jumps+=1
            current_jump_end=far
    return jumps

nums1=list(map(int,input("Enter a list of numbers separated by space: ").strip().strip().split()))
print(minJump(nums1))
