from typing import Any


def artifact_sorter(artifacts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(
        artifacts,
        key=lambda a: a["power"],
        reverse=True
    )


def power_filter(
    mages: list[dict[str, Any]],
    min_power: int
) -> list[dict[str, Any]]:
    return list(filter(
        lambda m: m["power"] >= min_power,
        mages
    ))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(
        lambda s: "* " + s + " *",
        spells
    ))


def mage_stats(mages: list[dict[str, Any]]) -> dict[str, Any]:
    powers = list(map(lambda m: m["power"], mages))
    return {
        "max_power": max(powers),
        "min_power": min(powers),
        "avg_power": sum(powers) / len(powers)
    }


if __name__ == "__main__":
    test_artifacts = [
        {"name": "Crystal Orb", "power": 85, "type": "focus"},
        {"name": "Fire Staff", "power": 92, "type": "weapon"},
        {"name": "Moon Amulet", "power": 71, "type": "charm"},
    ]
    test_mages = [
        {"name": "Alex", "power": 88, "element": "fire"},
        {"name": "Riley", "power": 65, "element": "water"},
        {"name": "Jordan", "power": 95, "element": "lightning"},
    ]
    test_spells = ["fireball", "heal", "shield"]

    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(test_artifacts)
    print(
        f"{sorted_artifacts[0]['name']} ({sorted_artifacts[0]['power']} power)"
        f" comes before {sorted_artifacts[1]['name']}"
        f" ({sorted_artifacts[1]['power']} power)"
    )
    print("Testing power filter...")
    print(power_filter(test_mages, 80))
    print("Testing spell transformer...")
    print(" ".join(spell_transformer(test_spells)))
    print("Testing mage stats...")
    print(mage_stats(test_mages))
