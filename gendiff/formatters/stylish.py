def to_str(value, depth=1):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    if not isinstance(value, dict):
        return str(value)

    indent = ' ' * (depth * 4)
    out_indent = ' ' * ((depth - 1) * 4)
    lines = []
    for k, v in value.items():
        lines.append(f"{indent}{k}: {to_str(v, depth + 1)}")
    return '\n'.join(['{', *lines, f"{out_indent}}}"])


def format_stylish(tree, depth=1):
    space = ' ' * (depth * 4 - 2)
    end_space = ' ' * ((depth - 1) * 4)
    lines = []

    for node in tree:
        node_type = node['type']
        key = node['key']

        if node_type == 'nested':
            children_str = format_stylish(node['children'], depth + 1)
            lines.append(f"{space}  {key}: {children_str}")
        elif node_type == 'unchanged':
            lines.append(f"{space}  {key}: {to_str(node['value'], depth + 1)}")
        elif node_type == 'added':
            lines.append(f"{space}+ {key}: {to_str(node['value'], depth + 1)}")
        elif node_type == 'deleted':
            lines.append(f"{space}- {key}: {to_str(node['value'], depth + 1)}")
        elif node_type == 'changed':
            lines.extend((
                f"{space}- {key}: {to_str(node['old_value'], depth + 1)}",
                f"{space}+ {key}: {to_str(node['new_value'], depth + 1)}"
            ))
    return '\n'.join(['{', *lines, f"{end_space}}}"])
