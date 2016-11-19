from setuptools import setup, find_packages

setup(
    name='github-dl',
    version='0.1a6',
    description='a command line tool for downloading repositories and gists',
    url='https://github.com/cameres/github-dl',
    author='Connor Ameres',
    author_email='connorameres@gmail.com',
    license='Mozilla Public License 2.0 (MPL 2.0)',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
        'Topic :: Software Development',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5'
    ],
    keywords='github gists download',
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
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
    '''
)
