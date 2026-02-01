import sys

class Solution:
    def add(self, a: int, b: int) -> int:
        return a + b

# 读取到 EOF
for line in sys.stdin:
    a, b = map(int, line.strip().split())
    result = Solution().add(a, b)
    print(result)