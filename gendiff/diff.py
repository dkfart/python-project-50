import os
import pathlib

from gendiff.parser import parse


def to_str(value):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return str(value)


def get_data(file_path):
    _, extension = os.path.splitext(file_path)
    format_name = extension.strip('.').lower()
    
    content = pathlib.Path(file_path).read_text()
        
    return parse(content, format_name)


def generate_diff(file_path1, file_path2):
    data1 = get_data(file_path1)
    data2 = get_data(file_path2)

    all_keys = sorted(list(data1.keys() | data2.keys()))
    
    lines = []
    for key in all_keys:
        if key in data1 and key not in data2:
            lines.append(f"  - {key}: {to_str(data1[key])}")
        elif key not in data1 and key in data2:
            lines.append(f"  + {key}: {to_str(data2[key])}")
        elif data1[key] == data2[key]:
            lines.append(f"    {key}: {to_str(data1[key])}")
        else:
            lines.extend((
                f"  - {key}: {to_str(data1[key])}",
                f"  + {key}: {to_str(data2[key])}"
            ))

    return '\n'.join(['{', *lines, '}'])
