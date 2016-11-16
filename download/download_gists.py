import os
import re
import requests as r


def download_gists(dst, gists, extension):
    """
    handles downloading paginated gists

    Arguments
    ---------
    dst : string
        folder to write gists to

    gists : github.PaginatedList.PaginatedList
        gist objects used to download raw files

    extension : string
        string extension for downloading gists
        that contain specific files
        ex: ipynb
    """
    if not os.path.isdir(dst):
        os.makedirs(dst)

    # create regular expression for matching end of file
    pattern = r'.*\.%s$' % (extension) if extension else None

    for gist in gists:
        # download entire gist e.g. could have json files to use
        file_names = gist.files.keys()
        if not pattern or any([re.match(pattern, file_name) for file_name in file_names]):
            # download the files
            owner = gist.owner.login if gist.owner else 'anonymous'
            id = gist.id
            file_directory = dst + '/' + owner + '/' + id + '/'

            if not os.path.isdir(file_directory):
                os.makedirs(file_directory)
            for (file_name, gist_file) in gist.files.items():
                if(gist_file.content):
                    contents = gist_file.content
                else:
                    contents = r.get(gist_file.raw_url).text

                # TODO: handle overwriting files
                file = open(file_directory + file_name, 'wb')
                # TODO: make sure to encode correctly
                file.write(contents.encode('utf8', 'replace'))
                file.close()
