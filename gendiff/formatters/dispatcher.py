from gendiff.formatters.stylish import format_stylish


def get_formatter(format_name):
    if format_name == 'stylish':
        return format_stylish
    raise ValueError(f"Unknown format: {format_name}")
