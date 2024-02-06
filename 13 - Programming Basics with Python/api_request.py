import requests

response = requests.get(f"https://api.github.com/users/RashidulApp/repos")
projectList =  response.json()

for project in projectList:
    print(f"Name : {project['name']}  Project Url : {project['html_url']} \n")
