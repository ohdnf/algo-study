from typing import List
import heapq


class Solution:
    """
    Runtime: 131 ms, faster than 65.07% of Python3 online submissions for Queue Reconstruction by Height.
    Memory Usage: 14.4 MB, less than 70.10% of Python3 online submissions for Queue Reconstruction by Height.
    """

    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        output = []
        hq = []
        for h, k in people:
            # 키 큰 사람, 나보다 큰 사람 수를 우선순위로 재정렬
            heapq.heappush(hq, [-h, k])
        while hq:
            h, k = heapq.heappop(hq)
            # 키 큰 사람부터 순서대로 추가
            # 무조건 정렬이 가능하므로 나보다 큰 사람이 k만큼 존재
            output.insert(k, [-h, k])
        return output


if __name__ == "__main__":
    s = Solution()
    print(s.reconstructQueue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]), [
          [5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]])
    print(s.reconstructQueue([[6, 0], [5, 0], [4, 0], [3, 2], [2, 2], [1, 4]]), [
          [4, 0], [5, 0], [2, 2], [3, 2], [1, 4], [6, 0]])
