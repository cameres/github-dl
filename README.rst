github-dl
=========

|Build Status| |codecov|

github-dl is a lightweight command line tool for downloading
repositories from **`github.com <http://github.com>`__** and gists from
**`gist.github.com <http://gist.github.com>`__**. github-dl has been
tested on python 2.7.12 and python 3.5.2.

Installation
------------

The project was recently added to PYPI. Feel free to submit an issue if
there are any issues with downloading via the command below...

.. code:: bash

    pip install github-dl

Installation (Development)
--------------------------

Install the project by downloading the project as a zip file or cloning
the repository. After downloading the source, run the following command
to install in the root directory of the project...

.. code:: bash

    pip install -e .

Usage
-----

github-dl's functionality is currently fairly limited, but the following
functionality is supported

usage for both commands
~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------+-----------------------------------+
| command line argument/option   | functionality                     |
+================================+===================================+
| ``--help``                     | list arguments/options for tool   |
+--------------------------------+-----------------------------------+
| ``--username``                 | github username for credentials   |
+--------------------------------+-----------------------------------+
| ``--password``                 | github password for credentials   |
+--------------------------------+-----------------------------------+
| ``--token``                    | github token for credentials      |
+--------------------------------+-----------------------------------+
| ``--config``                   | filename for configuration file   |
+--------------------------------+-----------------------------------+

config file
^^^^^^^^^^^

The config file is an optional file that stores github credentials the
following format is required...

.. code:: json

    {
      "username" : "username",
      "password" : "secret_password",
      "token" : "secret_token"
    }

**NOTE: ** None of the credentials are required in the configuration
file and token has the highest priority.

usage specific for ``$ github-dl``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------+-------------------------------------------+
| command line argument/option   | functionality                             |
+================================+===========================================+
| ``queries``                    | query for filtering github repositories   |
+--------------------------------+-------------------------------------------+
| ``destination``                | directory to download repositories to     |
+--------------------------------+-------------------------------------------+

examples:
^^^^^^^^^

Download all machine learning related notebooks matching a criteria: -
``$ github-dl 'machine learning language:jupyter-notebook size:<1000' github-notebooks --config=config.json``

usage specific for ``$ gist-dl``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------+---------------------------------------------------+
| command line argument/option   | functionality                                     |
+================================+===================================================+
| ``sources``                    | list of github users accounts to download gists   |
+--------------------------------+---------------------------------------------------+
| ``destination``                | directory to download gists to                    |
+--------------------------------+---------------------------------------------------+
| ``--extension``                | file extension to download ex: ipynb              |
+--------------------------------+---------------------------------------------------+

examples:
^^^^^^^^^

Download all public jupyter notebooks: -
``$ gist-dl gist-notebooks --config=config.json --extension=ipynb``

Download a specific user's public jupyter notebooks: -
``$ gist-dl cameres gist-notebooks --config=config.json --extension=ipynb``

.. |Build Status| image:: https://travis-ci.org/cameres/github-dl.svg?branch=master
   :target: https://travis-ci.org/cameres/github-dl
.. |codecov| image:: https://codecov.io/gh/cameres/github-dl/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/cameres/github-dl
