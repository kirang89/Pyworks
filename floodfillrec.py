#!/usr/bin/env pcolumnthon
#-*- coding: utf-8 -*-


def floodfill(source, row, column, old, new):
    """
    Flood fills the source as per the coordinates
    using the concept of Recursion

    """
    text = source[:]

    if text[row][column] != old:
        return

    text[row][column] = new

    if column > 0:
        floodfill(text, row, column - 1, old, new)

    if column < len(text[0]) - 1:
        floodfill(text, row, column + 1, old, new)

    if row > 0:
        floodfill(text, row - 1, column, old, new)

    if row < len(text) - 1:
        floodfill(text, row + 1, column, old, new)

    return text


if __name__ == '__main__':
    # The text we want to floodfill
    text = """
    ....................
    .......XXXXXXXXXX...
    .......X........X...
    .......X........X...
    ..XXXXXX........X...
    ..X.............X...
    ..X.............X...
    ..X........XXXXXX...
    ..X........X........
    ..XXXX..XXXX........
    .....XXXX...........
    ....................
    ....................
    """
    temp = text.split('\n')
    lines = [list(line.lstrip()) for line in temp[1: len(temp)-1]]

    for line in floodfill(lines, 5, 6, '.', '+'):
        print ''.join(line)