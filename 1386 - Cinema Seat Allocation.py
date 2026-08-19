class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        seats = defaultdict(set)
        groups = 0

        for row, seat in reservedSeats:
            if seat in {2, 3, 4, 5}: seats[row].add(0)
            if seat in {4, 5, 6, 7}: seats[row].add(1)
            if seat in {6, 7, 8, 9}: seats[row].add(2)

        groups = (n - len(seats)) * 2

        for blocked in seats.values():
            if len(blocked) == 3: groups += 0
            elif not blocked: groups += 2
            else: groups += 1

        return groups
