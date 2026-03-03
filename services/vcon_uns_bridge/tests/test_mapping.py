from vcon_uns_bridge.mapping import AssetMap, resolve_asset_path

def test_resolve_asset_path_prefers_explicit():
    m = AssetMap(topic_root="acme/site1", assets={"pump07":"acme/site1/a/b/pump07"})
    v = {"extensions":{"okf":{"asset_path":"x/y/z"}}}
    assert resolve_asset_path(v, m) == "x/y/z"
