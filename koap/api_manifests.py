"""
Represents internal registry for API Manifests
"""
import os
import threading
import yaml
from pathlib import Path


class APIRegistry:
    """
    Internal registry of API Manifests. `api_registry` is central entry point.
    """
    def __init__(self):
        self.lock = threading.RLock()
        self.registry = {}

    def merge_manifest(self, api_manifest: dict, owner: str = ''):
        """If manifest have groups, add them to the registry"""

        if 'apis' in api_manifest:
            for (key, api) in api_manifest['apis'].items():
                with self.lock:
                    self.registry[key] = {**api, ** {'owner': owner}}

    def clean_by_owner(self, owner: str):
        """Remove all items of specified owner"""
        with self.lock:
            to_delete = [key for key, api in self.registry.items() if api.get('owner', '') == owner]
            for key in to_delete:
                self.registry.pop(key, None)


    def get_manifest(self):
        """Generates manifest from internal representation"""

        # TODO: We should not return owner here. Could expose techincal details

        return {'apis': {** self.registry}}

    def load_from_file(self, path: str):
        """Loads and then merge manifest (YAML or JSON) from path if file exists"""

        if path:
            api_manifest_path = Path(path)
            if api_manifest_path.is_file(): 
                with api_manifest_path.open(mode='r') as stream:
                    api_manifest = yaml.safe_load(stream)
                    self.merge_manifest(api_manifest)

api_registry = APIRegistry()
