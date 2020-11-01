"""
Kubernetes related functonality. Mostly about to run KOPF, listen to configs and update API Manifests
"""
import kopf
import threading
import yaml

from api_manifests import api_registry


@kopf.on.event(
    '', 'v1', 'configmaps', annotations={'koap.tv/apimanifests': kopf.PRESENT}
)
def apimanifests_configmap(event, name, body, logger, **_):
    owner = f'k8s:{name}'

    api_registry.clean_by_owner(owner)

    if event['type'] == 'DELETED':
        return

    cm_data = body['data']
    for manifest_key in cm_data:
        manifest_raw = cm_data[manifest_key]
        manifest = yaml.safe_load(manifest_raw)
        api_registry.merge_manifest(manifest, owner)
        logger.info(f'Manifest merged: {manifest}')


def run_kopf(stop_flag: threading.Event):

    import asyncio

    def kopf_thread():
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        try:
            kopf.configure(verbose=True)

            loop.run_until_complete(kopf.operator(stop_flag=stop_flag))
        finally:
            loop.close()

    thread = threading.Thread(target=kopf_thread)
    thread.start()
