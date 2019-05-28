import os
import pytest
import shutil
import json

from click.testing import CliRunner

from json2dynamo import app
from json2dynamo.util import JsonTransfromer


RESOURCE_PATH = 'tests/resources'
OUTPUT_PATH = f'{RESOURCE_PATH}/output'
SAMPLE_FILE_NAME = 'test_sample_one.json'


@pytest.fixture
def sample_json():
    with open(f'{RESOURCE_PATH}/{SAMPLE_FILE_NAME}', 'r') as file:
        return json.loads(file.read())


@pytest.fixture
def sample_mapping():
    with open(f'{RESOURCE_PATH}/mapping/{SAMPLE_FILE_NAME}', 'r') as file:
        return file.read()


@pytest.fixture
def remove_output_folder():
    if os.path.exists(OUTPUT_PATH) and os.path.isdir(OUTPUT_PATH):
        shutil.rmtree(OUTPUT_PATH)


def test_get_json_files(remove_output_folder):
    assert set(['test_sample_two.json', 'test_sample_one.json']) == set(
            JsonTransfromer().get_json_files(RESOURCE_PATH))


def test_write_files_to_folder(remove_output_folder, sample_json, sample_mapping):
    JsonTransfromer().write_file_to_folder(
        str(sample_json), OUTPUT_PATH, SAMPLE_FILE_NAME)
    with open(f'{RESOURCE_PATH}/mapping/{SAMPLE_FILE_NAME}', 'r') as file:
        assert file.name.split('/')[3] == SAMPLE_FILE_NAME
        assert file.read() == sample_mapping


def test_transform_json_files(remove_output_folder):
    runner = CliRunner()
    result = runner.invoke(app.cli, [RESOURCE_PATH, OUTPUT_PATH])
    assert result.exit_code == 0
    _, _, files = next(os.walk(OUTPUT_PATH))
    assert len(files) == 2
