class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = defaultdict(int)
        for t in tasks:
            counter[t] += 1
        max_f = max(counter.values())
        number_max = 0
        for t in counter:
            if counter[t] == max_f:
                number_max += 1
        return max((max_f-1)*n + +max_f + number_max-1, len(tasks))