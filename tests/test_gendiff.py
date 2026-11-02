import os

from gendiff import generate_diff


def get_fixture_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'test_data', file_name)


def test_generate_diff():
    expected_path = get_fixture_path('expected_flat.txt')
    with open(expected_path, 'r') as f:
        expected = f.read().strip()

    json1 = get_fixture_path('file1.json')
    json2 = get_fixture_path('file2.json')
    assert generate_diff(json1, json2).strip() == expected

    yaml1 = get_fixture_path('file1.yaml')
    yaml2 = get_fixture_path('file2.yml')
    assert generate_diff(yaml1, yaml2).strip() == expected
