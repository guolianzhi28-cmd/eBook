from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent


def main() -> None:
    print(f"Project root: {PROJECT_ROOT}")
    print("eBook audiobook project scaffold is ready.")


if __name__ == "__main__":
    main()
