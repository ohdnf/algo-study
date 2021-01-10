class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        from_to = dict()
        for ticket in tickets:
            try:
                for i in range(len(from_to[ticket[0]])):
                    if from_to[ticket[0]][i] > ticket[1]:
                        from_to[ticket[0]].insert(i, ticket[1])
                        break
                else:
                    from_to[ticket[0]].append(ticket[1])
            except:
                from_to[ticket[0]] = [ticket[1]]

        route = []
        stack = ['JFK']
        while stack:
            try:
                while from_to[stack[-1]]:
                    stack.append(from_to[stack[-1]].pop(0))
            except:
                pass
            route.append(stack.pop())

        return route[::-1]