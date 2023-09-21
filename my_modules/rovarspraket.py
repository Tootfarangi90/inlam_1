import re


class Rovarspraket:
    def __init__(self, text):
        self.text = text
        self.invalid_characters = []

    # Hitta ogiltiga tecken med hjälp av regex
    # Om den funktionen hittar ogiltiga tecken kommer den att returnera dessa
    def find_invalid_characters(self):
        self.invalid_characters = re.findall(
            r'[^a-zA-ZåäöÅÄÖ0-9\s\\:;,._"\-\+?!*()\[\]=%$@##!/]', self.text
        )
        return self.invalid_characters

    # Funktion för att översätta text till Rövarspråket
    # Byter ut alla konsonanter från exempelvis "hej" till "Hohejoj"
    def translate_to_rovarspraket(self):
        result = ""
        consonants = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"

        for c in self.text:
            if c in consonants:
                result += f"{c}o{c.lower()}"
            else:
                result += c
        return result

    # Skriv ut ogiltiga tecken i en sträng
    def print_invalid_characters(self):
        if self.invalid_characters:
            invalid_chars_str = ", ".join(self.invalid_characters)
            return f"Ogiltiga tecken hittade:\n{invalid_chars_str}"
        else:
            return "Inga ogiltiga tecken hittades."
