"""
Functions to facilitate reading ZIP files.
"""
from typing import Generator
from zipfile import ZipFile


class ZipFileReaderError(Exception):
    """
    Raised by the ZipFileReader class to indicate a problem reading a ZIP file.
    """


class ZipFileReader:
    """
    Facilitates reading ZIP files.
    """
    def __init__(self, filename: str):
        """
        Creates a ZipFileReader instance.
        :param filename: The ZIP file name.
        """
        ZipFileReader._ensure_string_not_none_or_whitespace(
            filename,
            "File name must be specified.")

        self._zip_file = ZipFile(filename)

    def list_filenames(self) -> Generator[str, None, None]:
        """
        Returns a list of file names in the ZIP file.
        :return: A generator producing the file names.
        """
        return (info.filename for info in self._zip_file.infolist() if not info.is_dir())

    def list_directories(self) -> Generator[str, None, None]:
        """
        Returns a list of directory names in the ZIP file.
        :return: A generator producing the directory names.
        """
        return (info.filename for info in self._zip_file.infolist() if info.is_dir())

    def read_archive_file(self, filename: str) -> bytes:
        """
        Reads a file contained in the ZIP.
        :param filename: The name of the file to read.
        :return: The file's contents as a byte array.
        """
        ZipFileReader._ensure_string_not_none_or_whitespace(
            filename,
            "File name must be specified.")

        return self._zip_file.read(filename)

    def read_archive_file_as_string(self, filename: str, encoding: str):
        """
        Reads a file contained in the ZIP with the specified encoding.
        :param filename: The name of the file to read.
        :param encoding: The encoding to use to read the file.
        :return: The file's contents as a string.
        """

        ZipFileReader._ensure_string_not_none_or_whitespace(
            filename,
            "File name must be specified.")

        ZipFileReader._ensure_string_not_none_or_whitespace(
            encoding,
            "Encoding must be specified.")

        file_bytes = self.read_archive_file(filename)
        return file_bytes.decode(encoding)

    @staticmethod
    def _ensure_string_not_none_or_whitespace(value, message):
        if not value or len(value.strip()) == 0:
            raise ZipFileReaderError(message)
