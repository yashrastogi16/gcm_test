# import autocomplete_light
# from models import members

# autocomplete_light.register(members,search_fields=['^username', 'user_id'],)
# 2nd try
from tagging.models import Tag

import autocomplete_light


autocomplete_light.register(Tag)
