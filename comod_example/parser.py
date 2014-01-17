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


############################################################
# Pattern-dependent behavior
def answer_pattern(pattern, args):
    """
    Returns a `dict` representing the answer to the given
    pattern & pattern args.
    """
    if pattern not in PATTERNS:
      return None
    if len(args) != 1:
      return None

    name = args[0]

    r = Random()
    is_werewolf = r.choice([True, False])
    return {
      'is_werewolf': is_werewolf,
      'name': name,
      'plaintxt': '%s is%s a werewolf' % (
          name,
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
