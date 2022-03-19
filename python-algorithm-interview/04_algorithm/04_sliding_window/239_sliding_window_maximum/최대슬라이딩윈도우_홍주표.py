from collections import deque
from typing import List


class Solution:
    """
    Runtime: 1873 ms, faster than 82.95% of Python3 online submissions for Sliding Window Maximum.
    Memory Usage: 30.7 MB, less than 17.71% of Python3 online submissions for Sliding Window Maximum.
    """

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = deque()    # window for index of number
        output = []

        for idx, num in enumerate(nums):
            # move window
            if window and window[0] <= idx - k:
                window.popleft()

            # update max number of window
            # pop numbers that are smaller than current number
            while window and nums[window[-1]] < num:
                window.pop()

            # append current number to window
            window.append(idx)

            # add max number of window to output for each slide
            if idx >= k - 1:
                output.append(nums[window[0]])

        return output


class SolutionOnBook:
    """
    Runtime: 1668 ms, faster than 90.20% of Python3 online submissions for Sliding Window Maximum.
    Memory Usage: 29.7 MB, less than 82.62% of Python3 online submissions for Sliding Window Maximum.
    """

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = deque()    # 인덱스 저장 배열
        output = []         # 각 윈도우별 최대값 저장 배열
        for i, n in enumerate(nums):
            # 현재 윈도우에 들어가는 숫자보다 큰 인덱스를 만날 때까지 윈도우 인덱스 제거
            while window and nums[window[-1]] < n:
                window.pop()
            # 현재 인덱스 추가
            window.append(i)
            # 윈도우 크기를 벗어난 인덱스 제거
            # window => window[i-k+1], ..., window[i]
            if window[0] == i - k:
                window.popleft()
            # 윈도우가 완성된 순간부터 최대값 저장
            if i >= k - 1:
                output.append(nums[window[0]])
        return output


if __name__ == "__main__":
    s = Solution()
    print(f'#1: {[1, 3, -1, -3, 5, 3, 6, 7]}')
    print(s.maxSlidingWindow(
        [1, 3, -1, -3, 5, 3, 6, 7], 3), [3, 3, 5, 5, 6, 7])
    print(f'#2: {[1]}')
    print(s.maxSlidingWindow([1], 1), [1])
    print(f'#3: {[1, 2, 3, 4, 5]}')
    print(s.maxSlidingWindow([1, 2, 3, 4, 5], 4), [4, 5])
    print(f'#4: {[1, 3, 1, 2, 0, 5]}')
    print(s.maxSlidingWindow([1, 3, 1, 2, 0, 5], 3), [3, 3, 2, 5])
