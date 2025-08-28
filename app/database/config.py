from pathlib import Path

MAIN_DB_PATH = Path('data/links.db').as_posix()

ROOT_DIR = Path(__file__).parent.parent.parent
DATA_DIR = ROOT_DIR / 'data'
DATA_DIR.mkdir(exist_ok=True, parents=True)

MAIN_DB_PATH = DATA_DIR / 'data.db'