def majorityElement(nums: list[int]) -> int:
    maj = None
    tested = []
    if len(nums) == 0:
        return
    for x in nums:
        if x in tested:
            continue
        ret = nums.count(x)
        if maj is None or maj[1] < ret:
            maj = (x, ret)
        tested.append(x)
    return maj[0]
