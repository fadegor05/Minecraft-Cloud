from argparse import Namespace
from pathlib import Path

from sync.server import sync_server


def shutdown_command(args: Namespace):
    instance_path = Path(args.instance_directory)
    sync_server(args.instance_name, instance_path)
