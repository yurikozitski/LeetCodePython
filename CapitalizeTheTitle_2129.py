class CapitalizeTitle:
    def capitalizeTitle(self, title: str) -> str:
        words = title.split(" ")
        capitalizedWords = []

        for word in words:            
            if len(word) <= 2:                
                capitalizedWords.append(word.lower())
            else:
                capitalizedWords.append(word.capitalize())

        return " ".join(capitalizedWords)
        