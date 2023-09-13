from psd_tools import PSDImage
from psd_tools.api.layers import PixelLayer, Group
from typing import Generator, Any
import re
from PIL.Image import Image


def iterate_up(
    item: PixelLayer | Group | None,
) -> Generator[PixelLayer | Group, None, None]:
    while item is not None:
        yield item
        item = item.parent


FEATURE_NAMING_PATTERN: re.Pattern[str] = re.compile(r"^\[(?P<feature_name>.*)\].*$")


def extract_feature_name(item: PixelLayer | Group) -> str | None:
    groups: re.Match[str] | None = FEATURE_NAMING_PATTERN.match(item.name)
    if groups is None:
        return None
    return groups.groupdict()["feature_name"]


def find_feature_group(layer: PixelLayer) -> str | None:
    for node in iterate_up(layer):
        feature_name: str | None = extract_feature_name(node)
        if feature_name is not None:
            return feature_name
    return None


def is_layer_enabled(layer: Any, enabled_features: set[str]) -> bool:
    if not isinstance(layer, PixelLayer):
        return True
    group: str | None = find_feature_group(layer)
    return group is None or group in enabled_features


def render_with_features(
    image: PSDImage, enabled_features: set[str]
) -> tuple[Image, set[str]]:
    enabled_features_in_file = set()

    def layer_filter(layer):
        group: str | None = find_feature_group(layer)

        if is_layer_enabled(layer, enabled_features):
            if group is not None:
                enabled_features_in_file.add(group)
            return True
        return False

    resulting_image = image.composite(layer_filter=layer_filter)
    assert isinstance(resulting_image, Image)
    return resulting_image, enabled_features_in_file
