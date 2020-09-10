import heapq
from typing import List


def groups(last_sorted, target):
    return groups
    pass


def comb_i_lasts(i, sorted_candidates, target):
    num = sorted_candidates[i]
    groups = groups(sorted_candidates[i+1:len(sorted_candidates)],target)
    pass


def combination_sum2(candidates: List[int], target: int) -> List[List[int]]:
    result = []
    heap_candidates = []
    for n in candidates:
        if n > target:
            continue
        if n == target:
            result.append((n,))
        if n < target:
            heapq.heappush(heap_candidates, n)
    sorted_candidates = [heapq.heappop(heap_candidates) for i in range(len(heap_candidates))]
    result_comb = comb(len(sorted_candidates), sorted_candidates, target)
    for i in range(len(sorted_candidates)):
        comb_i_lasts(i, sorted_candidates ,target)
    result += result_comb
    return [x for x in result if sum(x) == target]


def comb(group_len, sorted_candidates, target) -> List:
    if group_len == 2:
        pairs = set()
        for i in range(len(sorted_candidates)):
            for j in range(len(sorted_candidates)):
                if i == j:
                    continue
                tmp = [sorted_candidates[i], sorted_candidates[j]]
                if sum(tmp) <= target:
                    heapq.heapify(tmp)
                    pairs.add(tuple(tmp))
                else:
                    pass
        return [list(x) for x in pairs]

    candidates_groups = comb(group_len - 1, sorted_candidates, target)
    result = set()
    for num in sorted_candidates:
        for group in candidates_groups:
            checked_group = group_check(group, num, len(sorted_candidates), target)
            result.add(tuple(checked_group))
    return result


def group_check(group, num, group_max_len, target):
    group = list(group)
    if len(group) + 1 < group_max_len and sum(group) + num < target:
        heapq.heappush(group, num)
        return group
    elif sum(group) + num == target:
        heapq.heappush(group, num)
        return [heapq.heappop(group) for i in range(len(group))]
    elif sum(group) == target:
        return [heapq.heappop(group) for i in range(len(group))]
    return []


if __name__ == '__main__':
    combination_sum2([10, 1, 2, 7, 6, 1, 5], 8)
