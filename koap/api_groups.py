import os
import json

api_groups_registry = {
    'groups': []
}

api_groups_json = os.getenv('KOAP_API_GROUPS_JSON', None)
if api_groups_json:
    api_groups = json.loads(api_groups_json)
    if 'groups' in api_groups:
        api_groups_registry['groups'].extend(api_groups['groups'])