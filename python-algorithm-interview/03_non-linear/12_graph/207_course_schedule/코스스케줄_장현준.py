class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        import collections
        did = [0] * numCourses
        must = collections.defaultdict(list)
        # must[후행수업]: [선행수업]
        for a,b in prerequisites:
            must[a].append(b)
        while sum(did) != numCourses: # 모든 클래스 수업 수강할때까지 => True 리턴
            flag = True # 모든 클래스를 돌아도 아무 행동 불가 => 모든 클래스 수강 불가능 => False 리턴
            for n in range(numCourses):
                if did[n]: continue
                for m in must[n]: # 아직 수강하지 않은 클래스를 수강가능한지 판별
                    if not did[m]: # 미수강 선행수업때문에 수강 불가
                        break
                else: # 수강
                    did[n] = 1
                    flag = False
            if flag: # 모든 클래스를 돌아도 아무 행동 불가 => 모든 클래스 수강 불가능 => False 리턴
                break
        else:
            return True # 모든 클래스 수업 수강할때까지 => True 리턴
        return False # 모든 클래스를 돌아도 아무 행동 불가 => 모든 클래스 수강 불가능 => False 리턴