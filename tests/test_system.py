from orchestration.orchestrator import run
from safety.policy import PROTECTED_ACTIONS, REQUIRED_REVIEWS, authorize


def approved_context():
    return {key: True for key in REQUIRED_REVIEWS}


def test_orchestrator_runs_five_agents_and_fails_closed():
    result = run({})
    for key in ("situation", "logistics", "shelter", "communications", "recovery"):
        assert key in result
    assert result["released"] is False


def test_missing_reviews_fail_closed():
    result = authorize("release_support_package", {})
    assert result["allowed"] is False
    assert len(result["missing"]) == 8


def test_reviewed_package_can_release():
    assert authorize("release_support_package", approved_context())["allowed"] is True


def test_situation_gap_blocks():
    assert authorize("release_support_package", approved_context() | {"situational_awareness_gap": True})["allowed"] is False


def test_scarce_resource_risk_blocks():
    assert authorize("release_support_package", approved_context() | {"scarce_resource_risk": True})["allowed"] is False


def test_shelter_safety_gap_blocks():
    assert authorize("release_support_package", approved_context() | {"shelter_safety_gap": True})["allowed"] is False


def test_public_information_risk_blocks():
    assert authorize("release_support_package", approved_context() | {"public_information_risk": True})["allowed"] is False


def test_protected_actions_never_autonomously_release():
    for action in PROTECTED_ACTIONS:
        assert authorize(action, approved_context())["allowed"] is False
