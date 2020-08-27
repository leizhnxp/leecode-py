from typing import List


class Solution:

    @staticmethod
    def find_sub_sequences(nums: List[int]) -> List[List[int]]:
        result = []
        for pos in range(len(nums)):
            num_pos = nums[pos]
            if pos == 0:
                result.append([num_pos, ])
                continue
            tmp = [[num_pos, ], ]
            for ele in result:
                if num_pos >= ele[len(ele) - 1]:
                    tmp.append(ele + [num_pos, ])
            result = result + tmp

        result = [tuple(x) for x in filter(lambda e: len(e) > 1, result)]
        result = [list(x) for x in set(result)]
        return result

