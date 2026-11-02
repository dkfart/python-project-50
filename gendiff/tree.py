def build_diff_tree(data1, data2):
    all_keys = sorted(list(data1.keys() | data2.keys()))
    tree = []

    for key in all_keys:
        if key in data1 and key not in data2:
            tree.append({'key': key, 'type': 'deleted', 'value': data1[key]})
        elif key not in data1 and key in data2:
            tree.append({'key': key, 'type': 'added', 'value': data2[key]})
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            tree.append({
                'key': key,
                'type': 'nested',
                'children': build_diff_tree(data1[key], data2[key])
            })
        elif data1[key] == data2[key]:
            tree.append({'key': key, 'type': 'unchanged', 'value': data1[key]})
        else:
            tree.append({
                'key': key,
                'type': 'changed',
                'old_value': data1[key],
                'new_value': data2[key]
            })
    return tree
