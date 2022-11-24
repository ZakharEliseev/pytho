from pathlib import Path

BASE_DIR = Path(__file__).parent


def demo_cwd():
    print("Base dir", BASE_DIR)

    cwd = Path.cwd()
    print(cwd)

    print(list(cwd.iterdir()))

    for path in cwd.iterdir():
        print('path', path.name, path.is_dir(), path.is_file())


def demo_home():
    home = Path.home()
    print('home:', home)


def demo_dirs():
    users = Path('/Users')
    print('users:', users.expanduser())

    cats = Path('/Cats')
    print('cats:', cats.exists())

    BASE_DIR.mkdir(exist_ok=True)


def demo_files():
    filepath = BASE_DIR / 'file.txt'
    # print(filepath)
    # filepath = 'dir_name' / Path('pictures')
    print(filepath)

    filepath.unlink(missing_ok=True)
    filepath.write_text('Hello!')

    text = filepath.read_text()
    print('text:', text)

    print(filepath)
    print(filepath.suffixes)
    print(Path('cat.py.jpg').suffixes)
    print(Path('archive.tar.gz').suffixes)
    print(Path('archive.tar.gz').stem)
    print(filepath.name)
    print(filepath.suffixes)
    print(filepath.stem)
    print(list(filepath.parents))
    print(filepath.stat())
    filepath.chmod(0o777)
    print(filepath.stat())


if __name__ == '__main__':
    # demo_home()
    # demo_cwd()
    # demo_dirs()
    demo_files()
