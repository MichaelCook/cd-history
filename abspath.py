import os

class AbsPath:
    """
    Like os.path.abspath, but if there are symlinks in / then prefer the
    symlink name rather than the symlinked-to name
    """

    def __init__(self) -> None:

        symlinks = []
        for entry in os.listdir('/'):
            preferred = f'/{entry}'
            try:
                alternate = os.readlink(preferred)
                if not alternate.startswith('/'):
                    alternate = f'/{alternate}'
                symlinks.append((os.path.realpath(alternate), preferred))
            except OSError:
                pass

        # Sort the list so we try the longest alternate names first.  For
        # example, for path /cygdrive/c/projects/foo we want to try
        # /cygdrive/c/projects before trying /cygdrive/c
        symlinks.sort(key=lambda ap: len(ap[0]), reverse=True)

        self.symlinks = tuple(symlinks)

    def __call__(self, path: str) -> str:
        path = os.path.realpath(path)
        for alternate, preferred in self.symlinks:
            if path == alternate:
                path = preferred
                break
            if path.startswith(f'{alternate}/'):
                path = f'{preferred}{path[len(alternate):]}'
                break
        return path
