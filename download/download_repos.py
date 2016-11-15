import os
import re
import git


def download_repos(dst, repos):
    '''
    download repos from github

    input: destination and repositories
    output: None
    '''
    for repo in repos:
        # we can clone the projects, but we only want to download small projects
        git.repo.base.Repo.clone_from(repo.git_url, dst + '/' + repo.full_name)
