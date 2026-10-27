import json


def to_str(value):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return str(value)


def generate_diff(file_path1, file_path2):
    with open(file_path1) as f1:
        data1 = json.load(f1)

    with open(file_path2) as f2:
        data2 = json.load(f2)

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

    result = ['{', *lines, '}']
    return '\n'.join(result)
