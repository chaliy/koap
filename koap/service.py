from aiohttp import web
from aiofile import AIOFile
import json
import os

from api_manifests import api_registry

webservice = web.Application()

# Ping
async def ping(request):
    return web.Response(text="pong")


webservice.router.add_route("GET", "/ping", ping)

# Serve static site
STATIC_BASE = os.getenv("KOAP_STATIC_BASE", "../koap-ui/build")
webservice.router.add_static("/static", f"{STATIC_BASE}/static")


async def index_html(request):
    async with AIOFile(f"{STATIC_BASE}/index.html", "r") as f:
        template = await f.read()

    manifest = api_registry.get_manifest()
    html = template.replace('"__API_MANIFEST__"', json.dumps(manifest))

    return web.Response(text=html, content_type="text/html")


webservice.router.add_get("/{path:.*}", index_html)
