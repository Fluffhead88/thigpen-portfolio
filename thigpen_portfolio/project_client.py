import requests

project_url = "http://127.0.0.1:8000/projects/"

while True:

    option = input("(s)how all or (c)reate? >").lower()

    if option == "s":
        projects = requests.get(project_url).json()
        for project in projects:
            print(project['title'], project['technologies_used'], project['github_link'], project['project_desription'])

    elif option == "c":
        title = input("Title? >")
        technologies_used = input("Technologies Used? >")
        github_link = input("Github_link? > ")
        project_desription = input("Project Description? >")
        requests.post(project_url,
                    data = {"title": title, "technologies_used": technologies_used, "github_link": github_link, "project_desription": project_desription})
