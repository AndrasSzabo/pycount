from importlib import resources

def get_einstein():
    """Get path to example text file, quoting Einstein.

    Returns
    -------
    pathlib.PosixPath
        Path to file.

    """
    with resources.path("pycounts.data", "einstein.txt") as f:
        data_file_path = f
    return data_file_path


def get_zen():
    """Get path to example text file, the zen of python.

    Returns
    -------
    pathlib.PosixPath
        Path to file.

    """
    with resources.path("pycounts.data", "zen.txt") as f:
        data_file_path = f
    return data_file_path
