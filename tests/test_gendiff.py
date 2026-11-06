import json
import os
from pathlib import Path

import pytest

from gendiff import generate_diff


def get_fixture_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'test_data', file_name)


def read_file(file_name):
    return Path(get_fixture_path(file_name)).read_text().strip()


@pytest.mark.parametrize(
    "file1, file2, format_name, expected_file",
    [
        ("flat_file1.json", "flat_file2.json", "stylish", "expected_flat.txt"),
        ("flat_file1.yaml", "flat_file2.yml", "stylish", "expected_flat.txt"),
        ("file1.json", "file2.json", "stylish", "expected_nested.txt"),
        ("file1.yaml", "file2.yml", "stylish", "expected_nested.txt"),
        ("file1.json", "file2.json", "plain", "expected_plain.txt"),
        ("file1.yaml", "file2.yml", "plain", "expected_plain.txt"),
    ]
)
def test_gendiff_formats(file1, file2, format_name, expected_file):
    path1 = get_fixture_path(file1)
    path2 = get_fixture_path(file2)
    expected = read_file(expected_file)
    
    assert generate_diff(path1, path2, format_name) == expected


def test_generate_diff_json_format():
    path1 = get_fixture_path("file1.json")
    path2 = get_fixture_path("file2.json")
    
    result = generate_diff(path1, path2, "json")
    assert isinstance(json.loads(result), (list, dict))
