"""
Must define three methods:

* answer_pattern(pattern, args)
* render_answer_html(answer_data)
* render_answer_json(answer_data)
"""
from .patterns import PATTERNS

import json
from django.template import loader, Context
from random import Random
import re

PATTERN_ARGS_RE = re.compile(r'{([A-Za-z0-9_]+)}')



############################################################
# Pattern-dependent behavior
def answer_pattern(pattern_str, args):
    """
    Returns a `dict` representing the answer to the given
    pattern & pattern args.
    """
    if pattern_str not in PATTERNS:
      return None
    if len(args) != 1:
      return None

    # dumb example of how to get key-value pairs back,
    # by matching the positional args with the original
    # positional item in the pattern. in this case,
    # we're always matching "person=foo".
    args_keys = PATTERN_ARGS_RE.findall(pattern_str)
    kwargs = dict(zip(args_keys,args))
    person = kwargs['person']

    # if you don't need this behavior this, you can literally
    # just use `person=args[0]`, since in this contrived case,
    # you know you only ever have one arg, and it is always
    # `person`.

    r = Random()
    is_werewolf = r.choice([True, False])
    return {
      'is_werewolf': is_werewolf,
      'person': person,
      'plaintxt': '%s is%s a werewolf' % (
          person,
          " not" if is_werewolf else ""
      )
    }

############################################################
# Applicable module-wide
def render_answer_html(answer_data):
    template = loader.get_template('comod_example/werewolf_search.html')
    return template.render(Context(answer_data))

def render_answer_json(answer_data):
    return json.dumps(answer_data)
