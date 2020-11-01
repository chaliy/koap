"""
Entry point for KOAP CLI
"""

from typing import Optional

import click


@click.group(
    name="koap",
    context_settings=dict(
        auto_envvar_prefix="KOAP",
    ),
)
def main() -> None:
    """Main entry point"""

@main.command(
    context_settings=dict(
        auto_envvar_prefix="KOAP",
    )
)
@click.option(
    "--k8s", is_flag=True, default=False, help="Enable Kubernetes integration"
)
@click.option("--k8s-namespace", default=None, help="Kubernetes namespace to listen")
@click.option(
    "--api-manifest",
    default=None,
    help="Path to JSON or YAML representation of API Manifest",
    allow_from_autoenv=True,
    show_envvar=True,
)
def service(
    k8s: bool, k8s_namespace: Optional[str], api_manifest: Optional[str]
) -> None:
    """ Start Koap Service with Koap UI """
    
    from aiohttp import web
    from service import webservice
    from api_manifests import api_registry
    
    api_registry.load_from_file(api_manifest)

    if k8s:
        import threading
        from k8s import run_kopf

        stop_flag = threading.Event()

        # On webservice shutdown let's signal Kopf
        async def on_app_shutdown(app):
            stop_flag.set()

        webservice.on_shutdown.append(on_app_shutdown)

        run_kopf(stop_flag)

    # Run web service
    web.run_app(webservice)
