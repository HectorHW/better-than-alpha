import typer
from psd_tools import PSDImage
from .layers import render_with_features
from .fileutils import find_all_images, get_matching_png_name

app = typer.Typer()


@app.command()
def render(features: list[str]):
    for file in find_all_images():
        psd = PSDImage.open(file)
        rendered_image = render_with_features(psd, set(features))
        name = get_matching_png_name(file)
        rendered_image.save(name)


if __name__ == "__main__":
    app()
