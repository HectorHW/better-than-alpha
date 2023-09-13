import typer
from psd_tools import PSDImage
from .layers import render_with_features

app = typer.Typer()


@app.command()
def render(features: list[str]):
    psd = PSDImage.open("terrain.psd")
    rendered_image = render_with_features(psd, set(features))
    rendered_image.save("terrain.png")


if __name__ == "__main__":
    app()
