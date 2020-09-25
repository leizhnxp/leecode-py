import bisect
from typing import List


class Solution:
    @staticmethod
    def subsets(nums: List[int]):
        result = set()

        for i in range(len(nums)):
            tmp_groups = []

            for group in result:
                tmp = list(group)
                bisect.insort(tmp, nums[i])
                tmp_groups.append(tuple(tmp))

            result.update(tmp_groups)
            result.add((nums[i],))

        result = [list(group) for group in result]
        result.append([])
        return result
