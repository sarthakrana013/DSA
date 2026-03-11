class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        # Use a stack to store (index, height)
        stack = [] # Pairs of (index, height)
        max_area = 0
        
        for i, h in enumerate(heights):
            start = i
            # If current height is lower, pop from stack and calculate area
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                # The current bar's 'start' moves back to the popped index
                start = index
            
            stack.append((start, h))
            
        # Clear out the remaining bars in the stack
        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))
            
        return max_area