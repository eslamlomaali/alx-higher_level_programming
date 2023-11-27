#!/usr/bin/python3
"""text_indentation method module"""


def text_indentation(text):
    """adding 2 new lines after '.?:' chars method.

    Args:
        text: The string text.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for d in ".?:":
        # print(d, text.split(d))
        text = (d + "\n\n").join(
            [line.strip(" ") for line in text.split(d)])

    print(text, end="")

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
