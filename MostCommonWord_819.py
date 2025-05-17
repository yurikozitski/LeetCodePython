from typing import List
import re

class MostCommonWord:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraphWords = re.split(r"[!\?',;.\s]+", paragraph)
        paragraphWords = [item for item in paragraphWords if item.strip()]
        wordsTable = {}

        for word in paragraphWords:
            lowerWord = word.lower()

            if lowerWord and lowerWord not in banned:
                 wordsTable[lowerWord] = wordsTable.get(lowerWord, 0) + 1

        return max(wordsTable, key = wordsTable.get)


