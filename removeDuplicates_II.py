def removeDuplicates(nums: list[int]) -> int:
    """"""

    saved = []
    for x in nums:
        if (saved.count(x) < 2):
            saved.append(x)
    nums[:] = saved
    return (len(saved))
    print(nums)

removeDuplicates([1,1,2])
removeDuplicates([0,0,1,1,1,2,2,3,3,4])