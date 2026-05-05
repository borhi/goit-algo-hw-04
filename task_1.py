from pathlib import Path


def organize_by_extension(path: Path, dest_root: Path) -> None:
    try:
        if path.is_dir():
            for child in path.iterdir():
                organize_by_extension(child, dest_root)
        elif path.is_file():
            suffix = path.suffix
            folder_name = suffix[1:].lower() if suffix else "no_ext"
            dest_dir = dest_root / folder_name
            dest_dir.mkdir(parents=True, exist_ok=True)
            dest_path = dest_dir / path.name
            dest_path.write_bytes(path.read_bytes())
    except (OSError, PermissionError) as e:
        print(f"{path}: {e}")


if __name__ == "__main__":
    source_raw = input("Шлях до вихідної директорії: ").strip()
    dest_raw = (
        input("Шлях до директорії призначення (Enter — dist): ").strip() or "dist"
    )

    if not source_raw:
        print("Потрібно вказати вихідну директорію.")
        raise SystemExit(1)

    source = Path(source_raw).expanduser().resolve()
    destination = Path(dest_raw).expanduser().resolve()

    if not source.is_dir():
        print(f"Не директорія: {source}")
        raise SystemExit(1)

    try:
        destination.mkdir(parents=True, exist_ok=True)
    except OSError as e:
        print(f"Не вдалося створити призначення: {destination}: {e}")
        raise SystemExit(1)

    organize_by_extension(source, destination)
