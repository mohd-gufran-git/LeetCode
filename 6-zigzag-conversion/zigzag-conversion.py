class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        # Special case
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows

        current_row = 0
        going_down = True

        for char in s:

            rows[current_row] += char

            # Top -> neeche 
            if current_row == 0:
                going_down = True

            # Bottom -> upar 
            elif current_row == numRows - 1:
                going_down = False

            if going_down:
                current_row += 1
            else:
                current_row -= 1

        return "".join(rows)