import pandas as pd
from github.GithubException import GithubException
from github import Github
import os
import numpy as np

g = Github(os.environ["GITHUB_TOKEN"])
repo = g.get_repo(os.environ["REPO_NAME"])

issues = pd.read_csv("checklist-issues.txt", skiprows=1, 
                     names=["issue", "label", "milestone"])
issues = issues.applymap(lambda x: x.strip())


# create milestones
for m in issues['milestone'].unique():
    try:
        repo.create_milestone(title=m, state='open')
    except GithubException as e:
        if e.data["errors"][0].get("code", None) != "already_exists":
            raise 

milestones = repo.get_milestones()
milestone_titles = [m.title for m in milestones]

# create issue labels
labels = issues["label"]
labels = [l.split(" ") for l in labels]
labels = np.unique(np.hstack(labels))

# seaborn colorblind palette
pal = ['0173b2',
      'de8f05',
      '029e73',
      'd55e00',
      'cc78bc',
      'ca9161',
      'fbafe4',
      '949494',
      'ece133',
      '56b4e9']

for i, l in enumerate(labels):
    try:
        repo.create_label(l, pal[i])
    except GithubException as e:
        if e.data["errors"][0].get("code", None) != "already_exists":
            raise 

labels = repo.get_labels()
label_titles = [l.name for l in labels]

# create issues
for i in issues.index:
    m = issues.loc[i, "milestone"]
    idx = milestone_titles.index(m)
    milestone = milestones[idx]

    title = issues.loc[i,"issue"]

    lname = issues.loc[i,"label"]
    lname = lname.split()
    label = []
    for l in lname:
        lidx = label_titles.index(l)
        label.append(labels[lidx])
    try:
        repo.create_issue(title=title, labels=label, milestone=milestone)

    except GithubException as e:
        print(e)
        if e.data["errors"][0].get("code", None) != "already_exists":
            raise 