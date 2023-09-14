import typer
from psd_tools import PSDImage
from .layers import render_with_features
from .fileutils import find_psd_files, get_matching_png_name
from .features import (
    FEATURES as ALL_FEATURES,
    FEATURE_NAMES as ALL_FEATURE_NAMES,
    select_enabled_features,
)

app = typer.Typer()

BASE_FILES = [
    "pack.png",
    "pack.txt",
]


@app.command("build")
def render(features: list[str]):
    if features == ["all"]:
        features = ALL_FEATURE_NAMES

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

    for feature in select_enabled_features(features):
        if feature.additional_includes:
            print("\n".join(feature.additional_includes))


@app.command("list")
def list_features():
    for feature in ALL_FEATURES:
        print(f"{feature.name}: {feature.documentation}")


if __name__ == "__main__":
    app()
