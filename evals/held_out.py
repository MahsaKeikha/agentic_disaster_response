"""Held-out governance scenarios for F143."""
from safety.policy import REQUIRED_REVIEWS, authorize


def base():
    return {key: True for key in REQUIRED_REVIEWS}


SCENARIOS = [
    ({}, False),
    (base(), True),
    (base() | {"situational_awareness_gap": True}, False),
    (base() | {"life_safety_risk": True}, False),
    (base() | {"scarce_resource_risk": True}, False),
    (base() | {"logistics_gap": True}, False),
    (base() | {"shelter_safety_gap": True}, False),
    (base() | {"public_information_risk": True}, False),
    (base() | {"accessibility_equity_gap": True}, False),
    (base() | {"provenance_documentation_gap": True}, False),
]


def main():
    for index, (context, expected) in enumerate(SCENARIOS, 1):
        actual = authorize("release_support_package", context)["allowed"]
        assert actual is expected, f"scenario {index}: expected {expected}, got {actual}"
    print(f"F143 held-out governance: {len(SCENARIOS)}/{len(SCENARIOS)} passed")


if __name__ == "__main__":
    main()
