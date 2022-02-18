import os.path

import pytest

from tq.zip_file_reader import ZipFileReader, ZipFileReaderError

valid_zip_filename = os.path.join(os.getcwd(), "zip_files", "valid_zip_with_folders.zip")
zfr = ZipFileReader(valid_zip_filename)


def test_can_list_filenames():
    with zfr:
        filenames = zfr.list_filenames()
        assert list(filenames) == ["folder01/file01.log", "folder02/file02.log", "folder03/file03.log"]


def test_can_list_directories():
    dirnames = zfr.list_directories()
    assert list(dirnames) == ["folder01/", "folder02/", "folder03/"]


def test_can_read_archived_file():
    with zfr:
        filename = list(zfr.list_filenames())[0]
        file_bytes = zfr.read_archive_file(filename)
        assert len(file_bytes) == 5524


def test_can_read_archived_file_with_encoding():
    with zfr:
        filename = list(zfr.list_filenames())[0]
        file_str = zfr.read_archive_file_as_string(filename, "utf-8")
        assert "Realtek" in file_str


@pytest.mark.parametrize("filename", [None, "", "  "])
def test_init_raises_error_when_filename_not_specified(filename):
    with pytest.raises(ZipFileReaderError) as e:
        ZipFileReader(filename)

    assert str(e.value) == "File name must be specified."


@pytest.mark.parametrize("filename", [None, "", "  "])
def test_read_archive_file_raises_error_when_filename_not_specified(filename):
    with pytest.raises(ZipFileReaderError) as e:
        zfr.read_archive_file(filename)

    assert str(e.value) == "File name must be specified."


@pytest.mark.parametrize("filename", [None, "", "  "])
def test_read_archive_file_as_string_raises_error_when_filename_not_specified(filename):
    with pytest.raises(ZipFileReaderError) as e:
        zfr.read_archive_file_as_string(filename, "utf-8")

    assert str(e.value) == "File name must be specified."


@pytest.mark.parametrize("encoding", [None, "", "  "])
def test_read_archive_file_as_string_raises_error_when_encoding_not_specified(encoding):
    filename = list(zfr.list_filenames())[0]

    with pytest.raises(ZipFileReaderError) as e:
        zfr.read_archive_file_as_string(filename, encoding)

    assert str(e.value) == "Encoding must be specified."
