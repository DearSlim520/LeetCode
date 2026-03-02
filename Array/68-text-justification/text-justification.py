class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # which row to assign current word
        # assign spaces

        n = len(words)
        curRow = []
        curLen = 0
        res = []

        for word in words:
            wordLen = len(word)
            addLen = wordLen + (1 if curRow else 0)

            # 1 / 2) this row 
            if addLen + curLen <= maxWidth:
                curRow.append(word)
                curLen += addLen
            # 2) next row
            else:
                res.append(self.justify_line(curRow, maxWidth, False))
                curRow = [word]
                curLen = wordLen

        # last row
        res.append(self.justify_line(curRow, maxWidth, True))

        return res

    def justify_line(self, curRow: List[str], maxWidth: int, is_last: bool) -> str:
        line = ''
        # 1) if last or only 1 word
        if is_last or len(curRow) == 1:
            line += ' '.join(curRow)
            return line + ' ' * (maxWidth - len(line))

        # 2) evenly distribute spaces
        total_chars = sum(len(c) for c in curRow)
        total_spaces = maxWidth - total_chars
        gaps = len(curRow) - 1

        base_spaces = total_spaces // gaps
        extra_spaces = total_spaces % gaps

        for i in range(len(curRow)):
            line += curRow[i]
            if i < gaps:
                space_cnt = base_spaces + (1 if i < extra_spaces else 0)
                line += ' ' * space_cnt

        return line
