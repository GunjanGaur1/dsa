class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        queue = deque()
        queue.append(("0000", 0))

        visited = {"0000"}

        while queue:
            state, moves = queue.popleft()

            if state == target:
                return moves

            for i in range(len(state)):
                # +1
                digits = list(state)
                digit = int(digits[i])

                forward = (digit + 1) % 10
                digits[i] = str(forward)
                forward_state = ''.join(digits)

                # -1
                digits = list(state)
                backward = (digit - 1) % 10
                digits[i] = str(backward)
                backward_state = ''.join(digits)

                if forward_state not in deadends and forward_state not in visited:
                    visited.add(forward_state)
                    queue.append((forward_state, moves + 1))

                if backward_state not in deadends and backward_state not in visited:
                    visited.add(backward_state)
                    queue.append((backward_state, moves + 1))
                if "0000" in deadends:
                    return -1

        return -1