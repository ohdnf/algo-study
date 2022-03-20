from collections import Counter, deque


class Solution:
    """
    Runtime: 224 ms, faster than 30.00% of Python3 online submissions for Minimum Window Substring.
    Memory Usage: 14.9 MB, less than 11.18% of Python3 online submissions for Minimum Window Substring.
    """

    def minWindow(self, s: str, t: str) -> str:
        counter = Counter(t)
        window = deque()
        output = ""
        min_len = float('inf')

        if len(s) < len(t):
            return ""

        for idx, char in enumerate(s):
            if char in counter:
                # expand window when character in t appears
                window.append(idx)
                counter[char] -= 1
                # check whether window can be reduced
                while window and counter[s[window[0]]] < 0:
                    counter[s[window.popleft()]] += 1
                # check every character in t is included
                for val in counter.values():
                    if val > 0:
                        break
                else:
                    # update output
                    if len(window) >= len(t) and min_len > window[-1] - window[0] + 1:
                        output = s[window[0]:window[-1] + 1]
                        min_len = window[-1] - window[0] + 1

        return output


class Solution1:
    """
    투 포인터

    Runtime: 96 ms, faster than 85.14% of Python3 online submissions for Minimum Window Substring.
    Memory Usage: 15 MB, less than 29.62% of Python3 online submissions for Minimum Window Substring.
    """

    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        needs = Counter(t)  # 필요한 문자 각각의 개수
        missing = len(t)    # 필요한 문자의 전체 개수
        left, min_left, min_right = 0, 0, 0

        for right, char in enumerate(s, 1):
            missing -= needs[char] > 0  # 필요한 문자라면 missing 감소
            needs[char] -= 1

            if missing == 0:
                # 윈도우 왼쪽 포인터 이동시켜 윈도우 크기 조절
                while left < right and needs[s[left]] < 0:
                    needs[s[left]] += 1
                    left += 1
                # 최소 윈도우 크기 업데이트
                if min_right == 0 or right - left < min_right - min_left:
                    min_left, min_right = left, right
                needs[s[left]] += 1
                missing += 1
                left += 1

        return s[min_left:min_right]


class Solution2:
    """
    AND 연산자(&) 사용

    Runtime: 1792 ms, faster than 5.01% of Python3 online submissions for Minimum Window Substring.
    Memory Usage: 14.8 MB, less than 66.43% of Python3 online submissions for Minimum Window Substring.
    """

    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        current = Counter()
        target = Counter(t)
        left, min_left, min_right = 0, float('-inf'), float('inf')

        for right, char in enumerate(s):
            current[char] += 1

            while current & target == target:
                if right - left < min_right - min_left:
                    min_left, min_right = left, right
                current[s[left]] -= 1
                left += 1

        return s[min_left:min_right+1] if min_right - min_left + 1 <= len(s) else ""


def minWindow(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    if not t or not s:
        return ""

    dict_t = Counter(t)

    required = len(dict_t)

    # Filter all the characters from s into a new list along with their index.
    # The filtering criteria is that the character should be present in t.
    filtered_s = []
    for i, char in enumerate(s):
        if char in dict_t:
            filtered_s.append((i, char))

    l, r = 0, 0
    formed = 0
    window_counts = {}

    ans = float("inf"), None, None

    # Look for the characters only in the filtered list instead of entire s. This helps to reduce our search.
    # Hence, we follow the sliding window approach on as small list.
    while r < len(filtered_s):
        character = filtered_s[r][1]
        window_counts[character] = window_counts.get(character, 0) + 1

        if window_counts[character] == dict_t[character]:
            formed += 1

        # If the current window has all the characters in desired frequencies i.e. t is present in the window
        while l <= r and formed == required:
            character = filtered_s[l][1]

            # Save the smallest window until now.
            end = filtered_s[r][0]
            start = filtered_s[l][0]
            if end - start + 1 < ans[0]:
                ans = (end - start + 1, start, end)

            window_counts[character] -= 1
            if window_counts[character] < dict_t[character]:
                formed -= 1
            l += 1

        r += 1
    return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]


if __name__ == '__main__':
    s = Solution()
    print(f'#1 ADOBECODEBANC ABC')
    print(s.minWindow("ADOBECODEBANC", "ABC"), "BANC")
    print(f'#2 a aa')
    print(s.minWindow("a", "aa"), "")
    print(f'#3 a a')
    print(s.minWindow("a", "a"), "a")
    print(f'#4 bba ab')
    print(s.minWindow("bba", "ab"), "ba")
