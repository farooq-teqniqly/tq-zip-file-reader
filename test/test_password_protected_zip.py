import os

import pytest

from tq.zip_file_reader import ZipFileReader, ZipFileReaderError

PWD = "1234"
zip_filename = os.path.join(os.getcwd(), "../test", "zip_files", "valid_zip_with_password.zip")
zfr = ZipFileReader(zip_filename)


def test_can_list_filenames():
    with zfr:
        filenames = zfr.list_filenames()
        assert list(filenames) == ["folder01/file01.log", "folder02/file02.log", "folder03/file03.log"]


def test_can_read_archived_file():
    with zfr:
        filename = list(zfr.list_filenames())[0]
        file_bytes = zfr.read_archive_file(filename, PWD)
        assert len(file_bytes) == 5524


def test_can_read_archived_file_with_encoding():
    with zfr:
        filename = list(zfr.list_filenames())[0]
        file_str = zfr.read_archive_file_as_string(filename, "utf-8", PWD)
        assert "Realtek" in file_str


@pytest.mark.parametrize("password", [None, "", "  "])
def test_read_archive_file_raises_error_when_password_not_specified(password):
    with pytest.raises(ZipFileReaderError) as e:
        with zfr:
            filename = list(zfr.list_filenames())[0]
            zfr.read_archive_file(filename, password)

    assert str(e.value) == "The ZIP file is password protected. Pass the password into the read_archive_file method."
