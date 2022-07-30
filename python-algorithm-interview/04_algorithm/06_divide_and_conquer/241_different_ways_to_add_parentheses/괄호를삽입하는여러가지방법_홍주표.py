from typing import List, Deque
from collections import deque
from itertools import islice


class Solution:
    """
    Runtime: 203 ms, faster than 5.08% of Python3 online submissions for Different Ways to Add Parentheses.
    Memory Usage: 43.8 MB, less than 17.42% of Python3 online submissions for Different Ways to Add Parentheses.
    """

    def diffWaysToCompute(self, expression: str) -> List[int]:

        # 숫자와 연산자 단위로 구분
        exp = deque()
        num = ''
        for char in expression:
            if char in '*+-':
                exp.extend([num, char])
                num = ''
            else:
                num += char
        exp.append(num)

        output = set()

        # 연산자 기준으로 괄호를 묶고, 전체가 묶일 때까지 진행
        queue = deque()
        queue.append(exp)
        while queue:
            exp: Deque = queue.popleft()

            # 식 완성
            if len(exp) == 1:
                output.add(exp[0])
                continue

            # 탐색
            forward = deque()
            while exp:
                var = exp.popleft()
                # 식에서 연산자가 나오면 앞뒤 항을 괄호로 묶기
                if var in '*+-':
                    temp = deque()
                    # 괄호에 묶이지 않는 이전 항들 처리
                    if len(forward) > 1:
                        temp = deque(islice(forward, 0, len(forward) - 1))
                    # 괄호 묶기
                    temp.append(f'({forward[-1]}{var}{exp[0]})')
                    # 괄호로 묶이지 않는 이후 항들 처리
                    if len(exp) > 1:
                        temp.extend(deque(islice(exp, 1, len(exp))))
                    queue.append(temp)
                forward.append(var)

        return [eval(exp) for exp in output]


class SolutionInTextbook:
    """
    Runtime: 125 ms, faster than 5.57% of Python3 online submissions for Different Ways to Add Parentheses.
    Memory Usage: 14 MB, less than 52.65% of Python3 online submissions for Different Ways to Add Parentheses.
    """

    def compute(self, left: List, right: List, op: str) -> List:
        return [eval(str(l) + op + str(r)) for l in left for r in right]

    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression.isdigit():
            return [int(expression)]

        output = []
        for idx, val in enumerate(expression):
            if val in '*+-':
                left = self.diffWaysToCompute(expression[:idx])
                right = self.diffWaysToCompute(expression[idx + 1:])

                output.extend(self.compute(left, right, val))
        return output


if __name__ == '__main__':
    # s = Solution()
    s = SolutionInTextbook()
    print(s.diffWaysToCompute('2-1-1'))
    print(s.diffWaysToCompute('2*3-4*5'))
    print(s.diffWaysToCompute('10*2-3*12'))
