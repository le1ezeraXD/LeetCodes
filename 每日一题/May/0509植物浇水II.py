class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:

        n1, n2 = 0, 0
        Ainit, Binit = capacityA, capacityB
        p, q = 0, len(plants)-1
        while p <= q:
            if p == q:
                if plants[p] > capacityA and plants[q] > capacityB:
                    n1 += 1
                break
            if plants[p] <= capacityA:
                capacityA -= plants[p]
            else:
                capacityA = Ainit - plants[p]
                n1 += 1
            if plants[q] <= capacityB:
                capacityB -= plants[q]
            else:
                capacityB = Binit - plants[q]
                n2 += 1
            p += 1
            q -= 1
        return n1 + n2
