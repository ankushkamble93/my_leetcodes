class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        user_times = collections.defaultdict(list)
        for name, time in zip(keyName, keyTime):
            hour, mins = time.split(":")
            total_time = int(hour) * 60 + int(mins)
            user_times[name].append(total_time)
        result = []
        for name, time in user_times.items():
            time.sort()
            for i in range(len(time)-2):
                if time[i+2] - time[i] <= 60:
                    result.append(name)
                    break
        return sorted(result)



        