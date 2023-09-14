import glob
import pathlib


def find_psd_files() -> list[str]:
    return glob.glob("**/*.psd", recursive=True)


def get_matching_png_name(psd_name: str) -> pathlib.Path:
    return pathlib.Path(psd_name).with_suffix(".png")
