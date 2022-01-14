from collections import namedtuple

"""Declaring the same namedtuple syntax here avoids to be an idiot
 and redeclare it with a typo everytime I use it"""

Position = namedtuple("Position", ["y_axis", "x_axis"])
