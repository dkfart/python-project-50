import os

from gendiff import generate_diff


def get_fixture_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'test_data', file_name)


def test_generate_diff_nested():
    expected_path = get_fixture_path('expected_nested.txt')
    with open(expected_path, 'r') as f:
        expected = f.read().strip()

    json1 = get_fixture_path('file1.json')
    json2 = get_fixture_path('file2.json')
    assert generate_diff(json1, json2) == expected

    yaml1 = get_fixture_path('file1.yaml')
    yaml2 = get_fixture_path('file2.yml')
    assert generate_diff(yaml1, yaml2) == expected
    
    expected_plain_path = get_fixture_path('expected_plain.txt')
    with open(expected_plain_path, 'r') as f:
        expected_plain = f.read().strip()

    assert generate_diff(json1, json2, 'plain') == expected_plain
    assert generate_diff(yaml1, yaml2, 'plain') == expected_plain