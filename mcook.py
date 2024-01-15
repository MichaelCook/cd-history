import sys
import os
from typing import Final, NoReturn

THIS_SCRIPT: Final = os.path.basename(sys.argv[0])

def warn(msg: str) -> None:
    print(f'{THIS_SCRIPT}: {msg}', file=sys.stderr, flush=True)

def die(msg: str) -> NoReturn:
    sys.exit(f'{THIS_SCRIPT}: {msg}')
