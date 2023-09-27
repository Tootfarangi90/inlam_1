import re


class EncryptedEmailHandler:
    def __init__(self, text):
        self.text = text
        self.invalid_characters = []

    # Funktion för att hitta och printa ut ogiltiga tecken med hjälp av regex
    def find_and_print_invalid_characters(self):
        self.invalid_characters = re.findall(
            r'[^a-zA-ZåäöÅÄÖ0-9\s\\:;,._"\-\+?!*()\[\]=%$@##!/]', self.text
        )

        if self.invalid_characters:
            invalid_chars_str = ", ".join(self.invalid_characters)
            return f"Ogiltiga tecken hittade:\n{invalid_chars_str}"
        else:
            return None

    # Funktion för att översätta texten till rövarspråket
    def translate_to_rovarspraket(self):
        result = ""
        consonants = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"

        for c in self.text:
            # Kontrollera om tecknet är en bokstav och lägg till o för konsonanter
            # exempelvis "Hej" blir "Hohejoj"
            if c.isalpha() and c in consonants:
                result += f"{c}o{c.lower()}"
            else:
                result += c
        print(result)
        return result
