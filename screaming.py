import os
from datetime import datetime

from assembla.api import API


api = API(
    key=os.getenv('ASSEMBLA_KEY'),
    secret=os.getenv('ASSEMBLA_SECRET')
)

aulasdovaca = api.spaces()[0]

space_tools = api.space_tools(space_id=aulasdovaca.id)

for tool in space_tools:
    if tool.type == 'GitTool':
        space_tool = tool
        break

merge_requests = api.merge_requests(space_id=aulasdovaca.id, space_tool_id=tool.id)

branch_names = []

for merge in merge_requests:
    delta = datetime.now() - merge.updated_at
    if delta.total_seconds() / 60 / 60 >= 6:
        branch_names.append(merge.source_symbol)

print(', '.join(branch_names))
