from my_modules.rovarspraket_function import Rovarspraket
from my_modules.fetch_from_github import FetchFileFromGitHub

github_link = "https://github.com/AIDEV23S/svText"
file_name = "svenskt_text.txt"
imported_text_content = FetchFileFromGitHub(github_link, file_name)

rovarspraket = Rovarspraket(imported_text_content)


def main():
    try:
        invalid_chars = rovarspraket.find_invalid_characters()
        if invalid_chars:
            print(rovarspraket.print_invalid_characters())
        else:
            translated_text = rovarspraket.translate_to_rovarspraket()
            print("Översatt text:")
            print(translated_text)

    except Exception as e:
        print(f"Exception: {e}")


if __name__ == "__main__":
    main()
