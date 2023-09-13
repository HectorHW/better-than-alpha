import typer
from psd_tools import PSDImage
from .layers import render_with_features
from .fileutils import find_psd_files, get_matching_png_name

app = typer.Typer()

BASE_FILES = [
    "pack.png",
    "pack.txt",
]


@app.command("build")
def render(features: list[str]):
    for file in BASE_FILES:
        print(file)

    for file in find_psd_files():
        psd = PSDImage.open(file)
        rendered_image, applied_features = render_with_features(psd, set(features))
        if not applied_features:
            continue
        name = get_matching_png_name(file)
        rendered_image.save(name)
        print(name)

    if "seasons" in features:
        print("misc/colors.properties")


@app.command("list")
def list_features():
    raise NotImplementedError()


if __name__ == "__main__":
    app()
