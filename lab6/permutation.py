def permute(nums):
    if len(nums) == 0:
        return []
    if len(nums) == 1:
        return [nums]
    result = []
    for i in range(len(nums)):
        n = nums[i]
        rest = nums[:i] + nums[i+1:]
        for permutation in permute(rest):
            result.append([n] + permutation)
            #print(result)
    #print("return")
    return result

print(permute(['b','c']))