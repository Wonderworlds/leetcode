class RotateArray:
    def reverse(self, nums, i, j):
        li = i
        ri = j

        while li < ri:
            temp = nums[li]
            nums[li] = nums[ri]
            nums[ri] = temp

            li += 1
            ri -= 1

    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if k < 0:
            k += len(nums)

        self.reverse(nums, 0, len(nums) - k - 1)
        self.reverse(nums, len(nums) - k, len(nums) - 1)
        self.reverse(nums, 0, len(nums) - 1)
        print(nums)


test = RotateArray()
test.rotate([1, 2, 3, 4, 5, 6, 7], 3)
test.rotate([-1, -100, 3, 99], 10)
