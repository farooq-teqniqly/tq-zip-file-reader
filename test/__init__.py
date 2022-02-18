"""
Tests module.
"""
import os


def get_zip_file_root_folder():
    """
    Gets the root folder containing the ZIP files used in the tests.
    :return: The ZIP root folder.
    """
    if os.getenv("GITHUB_WORKSPACE"):
        return os.path.join(os.getcwd(), "zip_files")

    return os.path.join(os.getcwd(), "..", "zip_files")
