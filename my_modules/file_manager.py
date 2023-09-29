import os
from .ask_user import AskUserYesOrNo


# En class för att hantera filer
class FileManager:
    # Fråga användaren om sökväg där filen ska sparas
    def input_local_file_path(self, prompt_message):
        try:
            full_path = ""
            # Om 'AskUserYesOrNo' returnerar True,
            if AskUserYesOrNo(prompt_message):
                # Använd nuvarande mapp som bas för att spara filen
                current_directory = os.getcwd()
                path_input = input("Ange filnamn: ")
                full_path = os.path.join(current_directory, path_input)
            else:
                path_input = input("Ange den fulla sökvägen till filen: ")
                full_path = path_input

            return full_path
        except Exception as e:
            print(f"Ett fel inträffade: {str(e)}")

    # Funktion för att skriva innehåll till en fil
    def write_file(self, file_path, file_content):
        try:
            with open(file_path, "wb") as file:
                file.write(file_content.encode("utf-8"))
                print(f"Din text har sparats i filen {file_path}")
        except Exception as e:
            print(f"Ett fel inträffade: {str(e)}")

    # Funktion för att läsa innehållet från en fil
    def read_file(self, file_path):
        try:
            if os.path.exists(file_path):
                with open(file_path, "rb") as file:
                    file_contents = file.read().decode("utf-8").strip()
                    return file_contents
        except FileNotFoundError as e:
            print(f"{e}\nFilen hittades inte!")
        except Exception as e:
            print(f"Ett fel inträffade: {str(e)}")
