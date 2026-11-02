import os
import pathlib

from gendiff.formatters import get_formatter
from gendiff.parser import parse
from gendiff.tree import build_diff_tree


def get_data(file_path):
    _, extension = os.path.splitext(file_path)
    format_name = extension.strip('.').lower()
    content = pathlib.Path(file_path).read_text()
    return parse(content, format_name)


def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1 = get_data(file_path1)
    data2 = get_data(file_path2)
    
    diff_tree = build_diff_tree(data1, data2)
    
    formatter = get_formatter(format_name)
    return formatter(diff_tree)
