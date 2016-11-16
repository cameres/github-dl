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
        # we can clone the projects, but we only want to download small projects
        git.repo.base.Repo.clone_from(repo.git_url, dst + '/' + repo.full_name)
