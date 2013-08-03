import os
from datetime import datetime

from assembla.api import API


api = API(
    key=os.getenv('ASSEMBLA_KEY'),
    secret=os.getenv('ASSEMBLA_SECRET')
)

aulasdovaca = api.spaces()[0]

space_tool = api.space_tools(aulasdovaca.id)[0]

merge_requests = api.merge_requests(space_id=aulasdovaca.id, space_tool_id=space_tool.id)

for merge_request in merge_requests:
    delta = datetime.now() - merge_request.updated_at
    if delta / 60 / 60 >= 6:
        exit(1)
