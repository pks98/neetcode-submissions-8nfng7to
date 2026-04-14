class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        map={')':'(',']':'[','}':'{'}

        for i in s:
            if i in map.values():
                l.append(i)
            elif i in map.keys():
                if l and l[-1] == map[i]:
                    l.pop()
                else:
                    return False

        return (len(l) == 0)

    
            