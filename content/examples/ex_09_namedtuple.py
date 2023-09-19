
from collections import namedtuple

coords = namedtuple("Location", "name lat lon")

c = coords('London', 42.99, -81.243)
c

c.name

c.lat

c[0]

type(c)


