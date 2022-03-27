from collections import Counter
from typing import List


class Solution:
    """
    Runtime: 784 ms, faster than 33.62% of Python3 online submissions for Task Scheduler.
    Memory Usage: 14.3 MB, less than 89.57% of Python3 online submissions for Task Scheduler.
    """

    def leastInterval(self, tasks: List[str], n: int) -> int:
        output = 0
        counter = Counter(tasks)
        while counter.total():
            # 중복된 작업이 많을수록 idle 작업이 많이 필요하므로
            # 가장 많이 남은 작업 순으로 처리한다.
            most_commons = counter.most_common(n + 1)
            # 현재 처리해야 하는 작업 수
            cur_tasks = sum([c for _, c in most_commons])
            if cur_tasks == n + 1:
                # 쿨다운 룰을 만족시키며 서로 다른 n+1개의 작업을 수행할 수 있는 경우
                output += n + 1
            else:
                # idle 작업이 필요한 경우
                if most_commons[0][1] > 1:
                    # 가장 많이 남은 작업이 한 번 이상 있는 경우
                    output += n + 1
                else:
                    # 모든 작업이 한 번만 남은 경우
                    output += cur_tasks
            # 작업 완료 처리
            for e, c in most_commons:
                if c > 0:
                    counter[e] -= 1

        return output


if __name__ == "__main__":
    s = Solution()
    print(s.leastInterval(["A", "A", "A", "B", "B", "B"], 2))
    print(s.leastInterval(["A", "A", "A", "B", "B", "B"], 0))
    print(s.leastInterval(["A", "A", "A", "A", "A",
          "A", "B", "C", "D", "E", "F", "G"], 2))
    print(s.leastInterval(["A", "A", "A", "B", "B",
          "B", "C", "C", "C", "D", "D", "E"], 2))
