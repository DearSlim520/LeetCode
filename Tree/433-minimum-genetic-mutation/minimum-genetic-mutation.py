class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank:
            return -1
        
        q = deque([(startGene, 0)])
        bank_set = set(bank)
        visited = set([startGene])
        while q:
            cur, step = q.popleft()
            # pruning
            if cur == endGene:
                return step
            for i in range(8):
                for char in 'ACGT':
                    nextGene = cur[:i] + char + cur[i+1:]
                    if nextGene in bank_set and nextGene not in visited:
                        q.append((nextGene,step+1))
                        visited.add(nextGene)

        return -1