import argparse

from commands.shutdown import shutdown_command
from commands.startup import startup_command


def main():
    parser = argparse.ArgumentParser(description="Minecraft-Cloud-CLI")

    subparsers = parser.add_subparsers(dest="command", required=True, help="Commands")

    startup_parser = subparsers.add_parser("startup", help="On Minecraft instancce startup")
    startup_parser.add_argument("instance_name", type=str, help="Instance name")
    startup_parser.add_argument("instance_directory", type=str, help="Instance .minecraft directory")
    startup_parser.add_argument("--force-upload", action="store_true", help="Force upload minecraft instance to cloud")

    shutdown_parser = subparsers.add_parser("shutdown", help="On Minecraft instance shutdown")
    shutdown_parser.add_argument("instance_name", type=str, help="Instance name")
    shutdown_parser.add_argument("instance_directory", type=str, help="Instance directory")

    args = parser.parse_args()

    if args.command == "startup":
        startup_command(args)
    elif args.command == "shutdown":
        shutdown_command(args)


if __name__ == "__main__":
    main()
