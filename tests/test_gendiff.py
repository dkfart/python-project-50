import os
from gendiff import generate_diff


def get_fixture_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'test_data', file_name)


def test_generate_diff_flat_json():
    path1 = get_fixture_path('file1.json')
    path2 = get_fixture_path('file2.json')
    expected_path = get_fixture_path('expected_flat.txt')

    with open(expected_path, 'r') as f:
        expected = f.read()

    assert generate_diff(path1, path2) == expected
