import git


def download_repos(dst, repos):
    """
    handles downloading paginated gists

    Arguments
    ---------
    dst : string
        folder to write repositories to

    repos : array-like of git.repo.base.Repo
        repositories to download
    """
    for repo in repos:
        try:
            # we can clone the projects, but we only want to download small projects
            print("downloading repo {}/{}".format(repo.owner.login, repo.name))
            git.repo.base.Repo.clone_from(repo.git_url, dst + '/' + repo.full_name)
        except git.exc.GitCommandError as e:
            # if the repositority already exists we want to move on
            if not e.stderr.endswith('already exists and is not an empty directory.\n\''):
                raise e
