from my_modules.ask_user import AskUserYesOrNo
from my_modules.encrypted_email_handler import EncryptedEmailHandler
from my_modules.github_file_manager import GitHubFileManager
from my_modules.local_file_manager import FileManager


def main():
    try:
        # Skapa en instans av FileManager för filhantering
        file_manager = FileManager()

        # Skapa en instans av GitHubFileManager för att hämta fil från GitHub
        github_file_manager = GitHubFileManager()

        # Hämta filinnehåll från GitHub
        github_file_content = github_file_manager.fetch_github_file()

        # Skapa en instans av EncryptedEmailHandler för att hantera textöversättning
        translator = EncryptedEmailHandler(github_file_content)

        # Hitta och skriv ut ogiltiga tecken i den hämtade texten
        invalid_chars = translator.find_and_print_invalid_characters()

        if invalid_chars:
            print(invalid_chars)
        else:
            # Översätta texten till rövarspråket
            translated_text = translator.translate_to_rovarspraket()

            # Fråga om användaren vill spara översättningen i den här mappen
            translated_file_path = file_manager.input_local_file_path(
                "Vill du spara översättningen i den här mappen? "
            )

            # Skriv den översatta texten till filen (skapar filen om den inte existerar)
            file_manager.write_file(translated_file_path, translated_text)

            # Fråga om användaren vill läsa den översatta texten direkt i terminalen
            ask_to_read = AskUserYesOrNo(
                "Vill du läsa den översatta texten direkt i terminalen?"
            )

            # Om ja, skriv ut texten från filen
            if ask_to_read:
                print("Innehåll i den översatta filen:")
                print(file_manager.read_file(translated_file_path))

    except Exception as e:
        print(f"Exception: {e}")


if __name__ == "__main__":
    main()
