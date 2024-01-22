def removeDuplicates(nums: list[int]) -> int:
    """"""

    saved = []
    for x in nums:
        if not (x in saved):
            saved.append(x)
    nums.clear()
    nums.extend(saved)
    print(nums)

removeDuplicates([1,1,2])
removeDuplicates([0,0,1,1,1,2,2,3,3,4])