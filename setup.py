from setuptools import setup

setup(
    name='github-dl',
    version='0.0.1',
    py_modules=['github_dl'],
    install_requires=[
        'click',
        'pygithub',
        'gitpython',
        'requests'
    ],
    entry_points='''
        [console_scripts]
        github-dl=github_dl:github_dl
        gist-dl=github_dl:gist_dl
    ''',
)
