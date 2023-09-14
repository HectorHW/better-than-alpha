import dataclasses
from typing import Iterable


@dataclasses.dataclass
class Feature:
    name: str
    documentation: str
    additional_includes: list[str] = dataclasses.field(default_factory=list)

    def is_enabled(self, match_against: Iterable[str]) -> bool:
        return self.name in match_against


FEATURES: list[Feature] = [
    Feature("trees", "alpha 1.1.2_01 tree colors"),
    Feature("grass", "alpha grass & plants color"),
    Feature("stone", "old cobblestone & mossy cobblestone texture"),
    Feature(
        "seasons",
        "disable BTA seasons feature and keep same colors whole year",
        additional_includes=["misc/colors.properties"],
    ),
]

FEATURE_NAMES: list[str] = [f.name for f in FEATURES]


def select_enabled_features(feature_names: list[str]) -> list[Feature]:
    return [f for f in FEATURES if f.is_enabled(feature_names)]
