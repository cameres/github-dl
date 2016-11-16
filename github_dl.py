import click

from download import setup_github
from download import public_gists
from download import user_gists
from download import download_gists
from download import search_repos
from download import download_repos


@click.command()
@click.argument('queries', nargs=-1)
@click.argument('dst', nargs=1)
@click.option('--username', help='your github username')
@click.option('--password', help='your github password')
@click.option('--token', help='your github token')
@click.option('--config', help='directory to a configuration file')
def github_dl(queries, dst, username, password, token, config):
    g = setup_github(username, password, token, config)
    for query in queries:
        # todo: can also pass sort, order, qualifiers...
        # currently expects user to pass parameters like...
        # 'machine learning language:jupyter-notebook size:<1000'
        repos = search_repos(g, query)
        download_repos(dst, repos)


@click.command()
@click.argument('users', nargs=-1)
@click.argument('dst', nargs=1)
@click.option('--username', help='your github username')
@click.option('--password', help='your github password')
@click.option('--token', help='your github token')
@click.option('--config', help='directory to a configuration file')
@click.option('--extension', help='gists containing a particular file type to download ex: ipynb')
def gist_dl(users, dst, username, password, token, config, extension):
    g = setup_github(username, password, token, config)
    if(users):
        # get the users' gists
        for user in users:
            gists = user_gists(user, g)
            download_gists(dst, gists, extension)
    else:
        # get the public gists
        gists = public_gists(g)
        download_gists(dst, gists, extension)
