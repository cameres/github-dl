import github

def user_gists(user, g):
    """handle grabbing a users public gists.

    entry point for when user provides 'gist-user' command
    """
    # temporary fix for not offering creating a user(?)
    paginated_gists = github.PaginatedList.PaginatedList(
        github.Gist.Gist,
        g._Github__requester,
        '/users/%s/gists' %(user),
        None
    )
    return paginated_gists
