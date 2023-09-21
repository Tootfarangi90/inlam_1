import requests


def FetchFileFromGitHub(url, file_name):
    file_url = f"{url}/raw/main/{file_name}"
    res = requests.get(file_url)

    if res.status_code == 200:
        file_content = res.text
        return file_content
    else:
        print(f"Det gick inte att hämta filen. Statuskod: {res.status_code}")
        return None
