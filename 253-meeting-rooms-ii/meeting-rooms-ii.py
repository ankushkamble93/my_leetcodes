class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        sorted_start = sorted(i[0] for i in intervals)
        sorted_end = sorted(i[1] for i in intervals)
        start_ptr = 0
        end_ptr = 0
        rooms = 0
        while start_ptr < len(intervals):
            if sorted_start[start_ptr] >= sorted_end[end_ptr]:
                end_ptr += 1
            else:
                rooms += 1
            start_ptr += 1
        return rooms