class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def get_key(log:str):
            log_id, rest = log.split(" ", 1)
            if rest[0].isdigit():
                return (1,)
            else:
                return (0,rest, log_id)
        logs.sort(key=get_key)
        return logs
