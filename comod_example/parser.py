# This file can be as complicated or as simple as possible, as long as
# 1: It contains a Parser subclass
# 2: The Parser subclass contains a "search" method that returns a Match subclass.
#    (The Match subclass can live in another file.)
# 3: The Match subclass returns an "as_html" of the search result (for the search
#    happening in Parser.search

from civomega import Parser, Match
from random import Random
from django.template import loader, Context

import re
import json

SIMPLE_PATTERN = re.compile('^\s*is\s(?P<name>(\s?\w+)+)\s(?:a|the)\swerewolf',re.IGNORECASE)

class FooParser(Parser):
    def search(self, s):
        if SIMPLE_PATTERN.match(s):
            d = SIMPLE_PATTERN.match(s).groupdict()
            noun = d['name'].strip()
            if(noun[-1] == '?'):
                noun = noun[0:-1]
            return FooMatch(noun)
        return None

class FooMatch(Match):
    def __init__(self, noun):
        self.name = noun
        r = Random()
        #r.seed(request.remote_addr)
        self.is_werewolf = r.choice([True, False])
        self.data = {
          'is_werewolf': self.is_werewolf,
          'name': self.name
        }

    def as_json(self):
        return json.dumps(self.data)

    def as_html(self):
        template = loader.get_template('comod_example/werewolf_search.html')
        return template.render(Context(self.data))
