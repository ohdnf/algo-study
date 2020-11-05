class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        path = dict()
        for ticket in tickets:
            from_st = ticket[0]
            to_st = ticket[1]
            if from_st in path:
                path[from_st][0].append(0)
                path[from_st][1].append(ticket[1])
                path[from_st][1].sort()
            else:
                path[ticket[0]] = [[0], [ticket[1]] ]
        def dfs(n, lst):
            if n == len(tickets):
                return lst
            now = lst[n]
            if now not in path: # 더 이상 불가능
                pass
            else:
                for i in range(len(path[now][0])):
                    if path[now][0][i] == 0:
                        path[now][0][i] = 1
                        # print(n+1, lst +  [ path[now][1][i] ])
                        temp = dfs(n+1, lst + [ path[now][1][i] ])
                        if temp: return temp
                        path[now][0][i] = 0
            return False
        # print(path, path["JFK"], path["JFK"][0], )
        return dfs(0, ["JFK"])
# 96 ms	14.8 MB	python3