class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        user_times = collections.defaultdict(list)
        for name, time_str in zip(keyName,keyTime):
            hour, mins = time_str.split(":")
            total_mins = int(hour) * 60 + int(mins)
            user_times[name].append(total_mins)
        result = []
        for name, times in user_times.items():
            times.sort()
            for i in range(len(times)-2):
                if times[i+2] - times[i] <= 60:
                    result.append(name)
                    break
        return sorted(result)

        