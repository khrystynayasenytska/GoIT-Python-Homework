import sys
import shutil
from pathlib import Path


def parse_arguments():
    """
    Parse command line arguments.
    Returns tuple: (source_dir, destination_dir)
    """
    if len(sys.argv) < 2:
        print("Error: Source directory not provided.")
        print("Usage: python script.py <source_dir> [destination_dir]")
        sys.exit(1)

    source = Path(sys.argv[1])
    destination = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("dist")

    return source, destination


def copy_files_by_extension(source: Path, destination: Path):
    """
    Recursively copies files from source directory into destination directory.
    Files are sorted into subfolders based on their extension.
    Directory structure is preserved inside each extension folder.
    """
    if not source.exists():
        print(f"Error: Source directory does not exist: {source}")
        sys.exit(1)

    if not source.is_dir():
        print(f"Error: Not a directory: {source}")
        sys.exit(1)

    for path in source.rglob("*"):
        try:
            if path.is_file():
                ext = path.suffix[1:] or "no_extension"

                # Build destination folder for this file type
                ext_dir = destination / ext

                # Preserve relative path (excluding the source root)
                relative_path = path.relative_to(source)
                final_path = ext_dir / relative_path

                # Ensure parent directory exists
                final_path.parent.mkdir(parents=True, exist_ok=True)

                # Copy file
                shutil.copy2(path, final_path)

                print(f"Copied: {path} -> {final_path}")

        except PermissionError:
            print(f"Permission denied: Cannot access {path}")
        except Exception as e:
            print(f"Error processing {path}: {e}")


def main():
    source, destination = parse_arguments()

    print(f"Source directory: {source}")
    print(f"Destination directory: {destination}")
    print("-" * 60)

    copy_files_by_extension(source, destination)

    print("-" * 60)
    print("Copy completed successfully!")


if __name__ == "__main__":
    main()
