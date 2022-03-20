from collections import Counter


class Solution:
    """
    Runtime: 1054 ms, faster than 5.01% of Python3 online submissions for Longest Repeating Character Replacement.
    Memory Usage: 14 MB, less than 68.01% of Python3 online submissions for Longest Repeating Character Replacement.
    """

    def expand_window(self, s, counter, right):
        right += 1
        if right < len(s):
            counter[s[right]] += 1
        return counter, right

    def reduce_window(self, s, counter, left):
        counter[s[left]] -= 1
        left += 1
        return counter, left

    def characterReplacement(self, s: str, k: int) -> int:
        # k개만큼 문자 변환 가능
        # 윈도우를 증가시키면서 윈도우 내 서로다른 문자 갯수 파악
        # 가장 많은 갯수의 문자를 제외한 나머지 문자의 갯수의 합이 k보다 작다면
        # 최대값이 될 수 있는지 확인

        # 예외 처리
        if k >= len(s):
            return k

        # 윈도우 초기화
        left, right, output = 0, k - 1, k
        if k == 0:
            right += 1
            output += 1
        counter = Counter(s[left:right+1])

        while right < len(s):
            _, max_char_num = counter.most_common(1)[0]
            available = k - counter.total() + max_char_num

            if available >= 0:
                # 결과값 갱신
                output = max(output, right - left + 1)
                # 윈도우 확장
                counter, right = self.expand_window(s, counter, right)
            else:
                # 윈도우 축소
                counter, left = self.reduce_window(s, counter, left)

        return output


def characterReplacement(s: str, k: int) -> int:
    left = right = 0
    counts = Counter()
    for right in range(1, len(s) + 1):
        counts[s[right - 1]] += 1
        # 가장 흔하게 등장하는 문자 탐색
        max_char_n = counts.most_common(1)[0][1]
        # 바꿔야할 문자 수가 k 초과시 왼쪽 포인터 이동
        if right - left - max_char_n > k:
            counts[s[left]] -= 1
            left += 1
    return right - left


if __name__ == '__main__':
    sol = Solution()
    print('#1: ABAB', sol.characterReplacement("ABAB", 2), 4)
    print('#2: AABABBA', sol.characterReplacement("AABABBA", 1), 4)
    print('#3: AABABBA', sol.characterReplacement("AABABBA", 0), 2)
    print('#4: AAAA', sol.characterReplacement("AAAA", 0), 4)
    print('#5: AABABBA', sol.characterReplacement("AABABBA", 3), 7)
    print('#6: AABABBA', sol.characterReplacement("AABABBA", 7), 7)
