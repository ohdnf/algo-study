class Solution:
    """
    Runtime: 156 ms, faster than 98.16% of Python3 online submissions for Assign Cookies.
    Memory Usage: 15.8 MB, less than 42.45% of Python3 online submissions for Assign Cookies.
    """

    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        output = 0
        while s:
            cookie = s.pop()    # 가장 큰 쿠키부터 부여
            while g and cookie < g[-1]:
                # 쿠키를 줘야할 아이의 그리드 팩터가
                # 현재 쿠키(남은 쿠키 중 가장 큰 쿠키)보다 크면
                # 해당 아이는 쿠키를 줄 수 없다.
                g.pop()
            if g and cookie >= g[-1]:
                # 쿠키를 줄 수 있는 경우
                g.pop()
                output += 1
            if not g:
                # 남아있는 아이가 없는 경우 중지
                break
        return output


class SolutionBook:
    def findContetnChildrenGreedy(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        child_i = cookie_j = 0
        while child_i < len(g) and cookie_j < len(s):
            if s[cookie_j] >= g[child_i]:
                child_i += 1
            cookie_j += 1

        return child_i

    def findContentChildrenBinarySearch(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        result = 0
        for i in s:
            index = bisect.bisect_right(g, i)
            if index > result:
                # 지금까지 쿠키를 준 아이들 수보다 쿠키를 받을 아이의 순서가 높다면
                # 이 아이는 쿠키를 받은 적이 없는 것이므로 쿠키를 줄 수 있다.
                result += 1
        return result
