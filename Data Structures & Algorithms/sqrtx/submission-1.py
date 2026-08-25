class Solution:
    def mySqrt(self, x: int) -> int:
        L, R = 0, x
        while L <= R:
            m = (L+R) // 2
            m_sq = m * m
            if m_sq == x:
                return m
            elif m_sq < x:
                L = m + 1
            else:
                R = m - 1

        return R