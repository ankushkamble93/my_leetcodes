class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        gaps = [0] * (n+1)
        gaps[0] = startTime[0]
        for i in range(1,n):
            gaps[i] = startTime[i] - endTime[i-1]
        gaps[n] = eventTime - endTime[-1]

        window_size = sum(gaps[:(k+1)])
        max_size = window_size
        for i in range(k+1, n+1):
            window_size += gaps[i] - gaps[i-(k+1)]
            max_size = max(max_size, window_size)
        return max_size