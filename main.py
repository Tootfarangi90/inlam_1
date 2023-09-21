from my_modules.rovarspraket import Rovarspraket


def main():
    try:
        # Test #
        text1 = "Det här är ett test! Faail ÿ ÿ ÿ ÿ ÿ "
        text2 = "Det här är ett test! Detta borde lyckas"
        rovar = Rovarspraket(text2)
        invalid_chars = rovar.find_invalid_characters()

        if invalid_chars:
            print(rovar.print_invalid_characters())
        else:
            translated_text = rovar.translate_to_rovarspraket()
            print("Översatt text:")
            print(translated_text)

    except Exception as e:
        print(f"Exception: {e}")


if __name__ == "__main__":
    main()
