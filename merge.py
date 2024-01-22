def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        def recursive(nums1: list[int], m: int, nums2: list[int], n: int):
            i = 0
            if (n == 0):
                return nums1
            while i < m:
                if (nums2[0] < nums1[i]):
                    if m < len(nums1):
                        nums1.pop(-1)
                    nums1.insert(i, nums2[0])
                    return recursive(nums1, m + 1, nums2[1:], n - 1)
                i += 1
            nums1[i] = nums2[0]
            return recursive(nums1, m + 1, nums2[1:], n - 1)

        nums1 = recursive(nums1, m, nums2, n)
        print(nums1)


merge(list([1,2,3,0,0,0]), 3, list([2,5,6]), 3)
merge(list([1]), 1, list([]), 0)
merge(list([0]), 0, list([1]), 1)