class Solution:
    def maxNumberOfFamilies(self, n, reservedSeats):
        rows = {}

        # Store reserved seats row-wise
        for r, seat in reservedSeats:
            if r not in rows:
                rows[r] = set()
            rows[r].add(seat)

        answer = (n - len(rows)) * 2

        for seats in rows.values():
            count = 0

            # Seats 2,3,4,5
            if not (2 in seats or 3 in seats or 4 in seats or 5 in seats):
                count += 1

            # Seats 6,7,8,9
            if not (6 in seats or 7 in seats or 8 in seats or 9 in seats):
                count += 1

            # If neither side is available, check middle
            if count == 0:
                if not (4 in seats or 5 in seats or 6 in seats or 7 in seats):
                    count = 1

            answer += count

        return answer