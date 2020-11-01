# pylint: disable=C0116,C0114

import os
dirname = os.path.dirname(__file__)

from api_manifests import APIRegistry


def test_empty_manifest():
    registry = APIRegistry()
    manifest = registry.get_manifest()
    assert manifest is not None
    assert 'apis' in manifest


def test_merge_manifest_1():
    registry = APIRegistry()
    registry.merge_manifest({'apis': {}})
    registry.merge_manifest(
        {'apis': {'1':  { 'title': '1', 'apiSpec': '1', 'foo': '1'} }}
    )
    manifest = registry.get_manifest()
    assert len(manifest['apis']) == 1
    assert manifest['apis']['1']['title'] == '1'
    assert manifest['apis']['1']['foo'] == '1', 'custom properties should pass'


def test_merge_manifest_2():
    registry = APIRegistry()
    registry.merge_manifest({'apis': {'1': {'title': '1'}}})
    registry.merge_manifest({'apis': {'1': {'title': '1'}}})
    registry.merge_manifest({'apis': {'2': {'title': '2'}}})
    manifest = registry.get_manifest()
    assert len(manifest['apis']) == 2
    assert manifest['apis']['1']['title'] == '1'
    assert manifest['apis']['2']['title'] == '2'


def test_load_from_file():
    registry = APIRegistry()
    example_manifest_path = os.path.join(dirname, '../examples/manifest.yaml')

    registry.load_from_file(example_manifest_path)
    
    manifest = registry.get_manifest()
    assert len(manifest['apis']) == 2
    assert manifest['apis']['weatherbit']['title'] == 'Weatherbit.io'
    assert manifest['apis']['petstore']['title'] == 'PET Store'
