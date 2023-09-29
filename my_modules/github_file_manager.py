import requests
from .ask_user import AskUserYesOrNo


# En class för att hämta och hantera filer från GitHub
class GitHubFileManager:
    def __init__(self):
        # Default värde om användare inte anger något
        self.full_path = "https://github.com/AIDEV23S/svText/raw/main/svenskt_text.txt"

    # Hämta en textfil från github
    def fetch_github_file(self):
        try:
            # Frågar användaren om de vill ange egen GitHub-länk
            if AskUserYesOrNo("Vill du ange en egen GitHub-länk? "):
                name_and_repo = input(
                    "Ange användarnamn och repository (username/repo): "
                )
                file_path = input("Ange filnamn: ")

                if name_and_repo.strip() and file_path.strip():
                    # Skapar den fullständiga GitHub-url med användarens inmatning
                    self.full_path = "https://github.com/{}/raw/main/{}".format(
                        name_and_repo, file_path
                    )
            # GET-request till GitHub-url
            res = requests.get(self.full_path)
            # Kontrollera HTTP-statuskod 200 dvs om det är ok
            if res.status_code == 200:
                file_content = res.text
                return file_content
            else:
                # Om det inte går att hämta filen returneras ett felmeddelande med statuskod
                print(f"Det gick inte att hämta filen. Statuskod: {res.status_code}")
                return None
        except Exception as e:
            # Andra fel som kan uppstå
            print(f"Ett fel inträffade: {str(e)}")
