import io
import shutil
import tempfile
import zipfile
from pathlib import Path
from urllib.request import Request, urlopen

GITHUB_OWNER = "PyPrig"
GITHUB_REPO = "pyprig-help"
BRANCH = "main"

URL = (
    f"https://github.com/{GITHUB_OWNER}/"
    f"{GITHUB_REPO}/archive/refs/heads/{BRANCH}.zip"
)

PACKAGE_DIR = Path(__file__).resolve().parent
HELP_DIR = PACKAGE_DIR / "help"

def get_help():
    request = Request(URL, headers={"User-Agent": "pyprig/1.0"})
    max_download = 50 * 1024 * 1024

    with urlopen(request, timeout=30) as response:
        content = response.read(max_download + 1)

    if len(content) > max_download:
        raise RuntimeError("GitHub archive exceeds 50 MB")

    with tempfile.TemporaryDirectory() as temp:
        temp_path = Path(temp)
        extract_dir = temp_path / "extracted"
        extract_dir.mkdir()

        with zipfile.ZipFile(io.BytesIO(content)) as archive:
            members = archive.infolist()

            if len(members) > 10000:
                raise RuntimeError("Too many archive entries")

            if sum(m.file_size for m in members) > 250 * 1024 * 1024:
                raise RuntimeError("Archive too large")

            for member in members:
                entry = Path(member.filename)
                mode = (member.external_attr >> 16) & 0o170000

                if (
                    entry.is_absolute()
                    or ".." in entry.parts
                    or "\\" in member.filename
                    or mode not in (0, 0o040000, 0o100000)
                ):
                    raise RuntimeError("Unsafe archive entry")

            archive.extractall(extract_dir)

        folders = list(extract_dir.iterdir())

        if len(folders) != 1 or not folders[0].is_dir():
            raise RuntimeError("Invalid GitHub archive structure")

        if HELP_DIR.exists():
            shutil.rmtree(HELP_DIR)

        shutil.copytree(folders[0], HELP_DIR)

    return HELP_DIR
