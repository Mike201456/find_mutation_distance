# find the mutation distance 

def  findMutationDistance(start, end, bank):
    def diff(str1, str2):
        return len([c1 for c1,c2 in zip(str1, str2) if c1 != c2]) <= 1
    def bfs(start, end, bank):
        q = []
        q.append((start, 0))
        while q:
            g = q.pop
            if g[0] == end:
                return g[1]
            ex = [(gx, g[1]+1) for gx, visited in bank.items() if not visited and diff(g[0], gx)]
            q.extend(ex)
            for x in ex:
                bank[x[0]] = True
        return -1;
    return bfs(start, end, {g: False for g in bank})

# the following code is to test this program 

findMutationDistance("AAAAAAAA", "AAAAAATT", ["AAAAAAAA", "AAAAAAAT", "AAAAAATT", "AAAATTT"])