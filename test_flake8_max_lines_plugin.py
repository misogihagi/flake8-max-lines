import pytest
from flake8_max_lines import MaxLinesPlugin

file_contains_newline_at_last = """first line
second line
third line
"""

file_not_contains_newline_at_last = """first line
first line
second line
third line"""

file_contains_extra_newline_at_last = """first line
second line
third line

"""

test_cases = [
    [4, file_contains_newline_at_last],
    [4, file_not_contains_newline_at_last],
    [5, file_contains_extra_newline_at_last],
]


@pytest.mark.parametrize("expected_length,file_content", test_cases)
def test_get_file_length(expected_length, file_content):
    lines = file_content.split("\n")
    plugin = MaxLinesPlugin(lines=lines, total_lines=len(lines), tree=None)
    assert plugin.get_file_length() == expected_length
