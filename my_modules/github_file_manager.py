import requests
from .ask_user import AskUserYesOrNo


class GitHubFileManager:
    def __init__(self):
        self.full_path = ""

    def fetch_github_file(self):
        try:
            if AskUserYesOrNo("Vill du ange en egen GitHub-länk? "):
                name_and_repo = input(
                    "Ange användarnamn och repository (username/repo): "
                )
                file_path = input("Ange filnamn: ")

                if name_and_repo.strip() and file_path.strip():
                    self.full_path += "https://github.com/{}/raw/main/{}".format(
                        name_and_repo, file_path
                    )
            else:
                self.full_path += (
                    "https://github.com/AIDEV23S/svText/raw/main/svenskt_text.txt"
                )

            res = requests.get(self.full_path)

            if res.status_code == 200:
                file_content = res.text
                return file_content
            else:
                print(f"Det gick inte att hämta filen. Statuskod: {res.status_code}")
                return None
        except Exception as e:
            print(f"Ett fel inträffade: {str(e)}")
