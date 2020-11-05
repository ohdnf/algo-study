from collections import defaultdict
class Solution:
    def findItinerary(self, tickets):
        itinerary = defaultdict(list)
        start = "JFK"
        for ticket in tickets:
            itinerary[ticket[0]].append(ticket[1])

        def get_route(route, remain_ticket):
            if not remain_ticket:
                return route
            departure = route[-1]
            itinerary[departure].sort()
            for destination in itinerary[departure]:
                ticket = [departure, destination]
                if ticket in remain_ticket:
                    remain_ticket.remove(ticket)
                    temp = get_route(route+[destination], remain_ticket)
                    remain_ticket.append(ticket)
                    if temp:
                        return temp

        result = get_route([start], tickets)

        return result


a = Solution().findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]])
print(a)