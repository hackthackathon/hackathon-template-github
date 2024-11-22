"""
This is a python script designed to add a PR
based on the created issues of adding new projects

1. writes markdown files to projects/.

"""
import os
import sys
import subprocess
import json
import requests

def check_link_availability(test_url):
    """
    check url validity
    """
    try:
        resp = requests.get(test_url)
        if resp.status_code >= 200 and resp.status_code < 300:
            print(f"The link '{test_url}' is available.")
        else:
            print(f"The link '{test_url}' returned a status code: {resp.status_code}")
            sys.exit('Error : URL need check')
    except requests.exceptions.RequestException as error_msg:
        print(f"An error occurred while checking the link '{test_url}': {error_msg}")
        sys.exit('Error : URL not valid')


if __name__ == '__main__' :
    # bioeco metadata list repo location
    ORGNAME = "hackthackathon"
    #ORGNAME = "hackthackathon"
    REPO_NAME = "hackathon-template-github"
    #REPO_NAME = "hackathon-template-github"
    DEBUG = False

    # A token is automatically provided by GitHub Actions
    # Using the GitHub api to get the issue info
    # Load the contents of the event payload from GITHUB_EVENT_PATH
    if DEBUG :
        ISSUE_NUM = 7
    else :
        event_path = os.environ['GITHUB_EVENT_PATH']
        with open(event_path, 'r') as event_file:
            event_data = json.load(event_file)
        # Access the issue number from the event payload
        ISSUE_NUM = event_data['issue']['number']

    print(f'issue number: {ISSUE_NUM}' )
    url = f"https://api.github.com/repos/{ORGNAME}/{REPO_NAME}/issues/{ISSUE_NUM}"

    response = requests.get(url)
    print(response)
    issue = response.json()
    print(issue)
    print(issue['body'])
    # parsing issue

    # Save the issue contents as project file
    if not DEBUG:

        title = issue['title'].replace('[Project Proposal]: ','')
        fname = title.replace(' ','_')

        with open(f'projects/project-{fname}.md', "w") as f:
            f.write('# '+title+'\n\n'+issue['body'])
        print(f'wrote projects/project-{fname}.md')
