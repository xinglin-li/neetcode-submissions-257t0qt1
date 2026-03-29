class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # I have a naive solution previously, but there is a more efficient way to solve this question
        # 'res' will store the final list of valid strings.
        res = []
        # 'stack' will temporarily hold the current combination being built.
        stack = []

        def backtrack(open_count, closed_count):
            # Base Case: When the current combination has the correct total length.
            if open_count == n and closed_count == n:
                res.append("".join(stack))
                return

            # Recursive Step 1: Add an open parenthesis '('
            # We can add an open parenthesis as long as we haven't used all 'n' of them.
            if open_count < n:
                stack.append("(")
                backtrack(open_count + 1, closed_count)
                stack.pop() # Backtrack: remove the '(' to explore other possibilities.

            # Recursive Step 2: Add a closed parenthesis ')'
            # We can add a closed parenthesis only if the number of closed parentheses
            # is strictly less than the number of open parentheses already in the stack.
            # This ensures validity at every step (prefix validity).
            if closed_count < open_count:
                stack.append(")")
                backtrack(open_count, closed_count + 1)
                stack.pop() # Backtrack: remove the ')' to explore other possibilities.
        
        # Start the backtracking process with zero open and zero closed parentheses.
        backtrack(0, 0)
        return res