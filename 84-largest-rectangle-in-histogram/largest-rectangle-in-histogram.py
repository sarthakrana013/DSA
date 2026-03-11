class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = [-1] # Initialize with -1 to handle width calculation for the first element
        max_area = 0
        # Add a sentinel value (0) to the end to flush the stack
        heights.append(0)
        
        for i in range(len(heights)):
            # While the current height is less than the height of the bar at stack top
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                current_height = heights[stack.pop()]
                # Width = current index - new stack top - 1
                current_width = i - stack[-1] - 1
                max_area = max(max_area, current_height * current_width)
            
            stack.append(i)
            
        # Optional: remove the sentinel if you need to keep 'heights' original
        heights.pop() 
        return max_area