from aiohttp import web
from aiofile import AIOFile
import json

from api_groups import api_groups_registry

app = web.Application()

# Ping
async def ping(request):
    return web.Response(text='pong')
app.router.add_route('GET', '/ping', ping)

# Serve static site
STATIC_BASE = '../koap-ui/build'
app.router.add_static('/static', f'{STATIC_BASE}/static')

async def index_html(request):
    async with AIOFile(f'{STATIC_BASE}/index.html', 'r') as f:
        template = await f.read()

    html = template.replace('"__API_GROUPS__"', json.dumps(api_groups_registry))

    return web.Response(text=html, content_type='text/html')

app.router.add_get('/{path:.*}', index_html)


web.run_app(app, host="127.0.0.1")