def to_str(value):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, str):
        return f"'{value}'"
    return str(value)


def format_plain(tree, path=''):
    lines = []

    for node in tree:
        node_type = node['type']
        key = node['key']
        current_path = f"{path}.{key}" if path else key

        if node_type == 'nested':
            lines.append(format_plain(node['children'], current_path))
        elif node_type == 'added':
            val = to_str(node['value'])
            lines.append(
                f"Property '{current_path}' was added with value: {val}"
            )
        elif node_type == 'deleted':
            lines.append(f"Property '{current_path}' was removed")
        elif node_type == 'changed':
            old_val = to_str(node['old_value'])
            new_val = to_str(node['new_value'])
            lines.append(
                f"Property '{current_path}' was updated. "
                f"From {old_val} to {new_val}"
            )

    return '\n'.join(filter(None, lines))
