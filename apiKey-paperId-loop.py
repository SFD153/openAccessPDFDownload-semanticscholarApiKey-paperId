import requests

S2_API_KEY = "iYTNXXDH278PVXl2FJ2YU1TyZ5joLAZr3WA9IVzt"

def download_paper(paper_id, pdf_path) -> bool:
    paper = requests.get(f"https://api.semanticscholar.org/graph/v1/paper/{paper_id}?fields=isOpenAccess,openAccessPdf", headers={'x-api-key': S2_API_KEY}).json()

    if not paper.get("isOpenAccess", False):
        return False

    response = requests.get(paper["openAccessPdf"]["url"], headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}, stream=True, verify=False)

    with open(pdf_path, 'wb') as f:
        for chunk in response.iter_content():
            f.write(chunk)

    return True

while True:
    paper_id = input("Enter paper ID: ")

    if not paper_id:
        print("Please enter a paper ID.")
        continue

    if download_paper(paper_id, f"papers/{paper_id}.pdf"):
        print("Paper downloaded successfully.")
        break
    else:
        print("Error: Paper is not open access or the ID is incorrect. Please try again.")