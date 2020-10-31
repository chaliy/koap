"""Kubernetes listener"""

import kopf

@kopf.on.event('', 'v1', 'configmaps')
def configmap(event, **_):
    print(event)
