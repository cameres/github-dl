import getpass
import json

from github import Github

def setup_github(username, password, token, config):
    if(config):
        config = json.load(open(config, "r"))
        # we need either token
        token = config.get('token', None)

        # or username and password
        username = config.get('username', None)
        password = config.get('password', None)
    if(token):
        return Github(token, per_page=100)
    else:
        username = username if username else raw_input("username:")
        password = password if password else getpass.getpass("password:")
        return Github(username, password, per_page=100)
