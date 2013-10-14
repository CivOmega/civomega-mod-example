# Basically bind the `parsers` inside this module
# with the civomega.registry that makes the website tick.

from .parser import FooParser

def autoregister(registry):
    # for each parser in this module, call this basically:
    registry.add_parser('foo_search', FooParser)
