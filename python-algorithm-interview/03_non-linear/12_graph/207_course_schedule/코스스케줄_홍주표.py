from typing import List
import collections


# 순환 그래프 찾기
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        count = [0] * numCourses

        for course, required in prerequisites:
            graph[required].append(course)
            count[course] += 1

        while 0 in count:
            course = count.index(0)
            while graph[course]:
                count[graph[course].pop()] -= 1
            count[course] = -1

        # print(graph)
        # print(count)

        for remain in count:
            if remain > 0:
                return False
        return True


# DFS + 가지치기
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)

        traced = set()
        taken = set()

        def go(course):
            if course in traced:    # 순환 구조 검사
                return False
            if course in taken:   # 이미 수료한 과목
                return True

            traced.add(course)

            for next_course in graph[course]:
                if not go(next_course):
                    return False

            traced.remove(course)
            taken.add(course)

            return True

        # 순환 그래프 검사
        for course in list(graph):  # 기본값을 생성해주는 defaultdict에서 list로 변환
            if not go(course):
                return False

        return True
