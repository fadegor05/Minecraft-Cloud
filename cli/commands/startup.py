from argparse import Namespace
from pathlib import Path

from sync.client import sync_client
from sync.server import sync_server


def startup_command(args: Namespace):
    instance_path = Path(args.instance_directory)
    if args.force_upload:
        sync_server(args.instance_name, instance_path)
        return
    sync_client(args.instance_name, instance_path)
