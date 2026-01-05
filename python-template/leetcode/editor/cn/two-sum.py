#
# @lc app=leetcode.cn id=1 lang=python3
# @lcpr version=30305
#
# [1] 两数之和
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i in range(len(nums)):
            need = target - nums[i]
            if need in hash_map:
                return [i , hash_map[need]]
            hash_map[nums[i]] = i
        return []
# @lc code=end

if __name__ == '__main__':
    # your test code here





#
# @lcpr case=start
# [2,7,11,15]\n9\n
# @lcpr case=end

# @lcpr case=start
# [3,2,4]\n6\n
# @lcpr case=end

# @lcpr case=start
# [3,3]\n6\n
# @lcpr case=end

#
