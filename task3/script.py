import sys
import colorama
from pathlib import Path

colorama.init(autoreset=True)

def print_tree(directory: Path, prefix: str = "") -> None:
    print(f"{prefix}{colorama.Fore.BLUE}{directory.name}/{colorama.Style.RESET_ALL}")

    entries = sorted(directory.iterdir(), key=lambda item: (not item.is_dir(), item.name.lower()))

    for entry in entries:
        if entry.is_dir():
            print_tree(entry, prefix + "    ")
        else:
            print(f"{prefix}    {colorama.Fore.GREEN}{entry.name}{colorama.Style.RESET_ALL}")


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_directory>")
        return
    
    passed_path = Path(sys.argv[1]).resolve()
    print(f"passed_path: {passed_path}")
    
    if not passed_path.exists():
        print(f"Error: path does not exist: {passed_path}")
        return
    if not passed_path.is_dir():
        print(f"Error: path is not a directory: {passed_path}")
        return

    print_tree(passed_path)


if __name__ == "__main__":
    main()
