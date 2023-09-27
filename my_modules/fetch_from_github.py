import requests
from .ask_user import YesOrNo


# Funktion för att fråga användaren om de vill ange en egen GitHub-länk
def GitHubPath(prompt_message):
    try:
        if YesOrNo(prompt_message):
            github_url = input("Ange url till GitHub repo: ")
            custom_file_name = input("Ange filnamn: ")
            if github_url.strip() and custom_file_name.strip():
                return github_url, custom_file_name
        else:
            return (
                "https://github.com/AIDEV23S/svText",
                "svenskt_text.txt",
            )
    except Exception as e:
        print(f"Ett fel inträffade: {str(e)}")


def FetchGitHubFile(url, file_name):
    file_url = f"{url}/raw/main/{file_name}"
    res = requests.get(file_url)

    if res.status_code == 200:
        file_content = res.text
        return file_content
    else:
        print(f"Det gick inte att hämta filen. Statuskod: {res.status_code}")
        return None
