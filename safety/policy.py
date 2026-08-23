"""Fail-closed governance for F143 Agentic Disaster Response."""

PROTECTED_ACTIONS = {
    "dispatch_response_resources",
    "allocate_scarce_lifesaving_resources",
    "issue_official_warning",
    "open_or_close_shelter",
    "authorize_reentry",
    "external_command_distribution",
}

REQUIRED_REVIEWS = (
    "situation_verified",
    "logistics_reviewed",
    "shelter_reviewed",
    "communications_reviewed",
    "life_safety_reviewed",
    "accessibility_equity_reviewed",
    "recovery_reviewed",
    "qualified_incident_command_approval",
)


def authorize(action: str, context: dict | None = None) -> dict:
    context = context or {}
    if action in PROTECTED_ACTIONS:
        return {"allowed": False, "reason": "binding disaster-response command, allocation, warning, shelter, reentry, or distribution action is outside reference-system scope"}

    missing = [key for key in REQUIRED_REVIEWS if not context.get(key)]
    if missing:
        return {"allowed": False, "reason": "missing required disaster-response review", "missing": missing}

    checks = {
        "situational_awareness_gap": "material hazard, location, timing, casualty, access, or source-confidence information unresolved",
        "life_safety_risk": "material survivor, responder, medical, structural, environmental, or access safety risk unresolved",
        "scarce_resource_risk": "scarce lifesaving resource allocation requires accountable human command decision",
        "logistics_gap": "critical supply, transport, fuel, communications, access, staffing, or staging dependency unresolved",
        "shelter_safety_gap": "shelter capacity, accessibility, medical, sanitation, security, staffing, or habitability issue unresolved",
        "public_information_risk": "official message authority, geography, timing, language, accessibility, or accuracy risk unresolved",
        "accessibility_equity_gap": "material disability, language, transportation, medical, housing, documentation, or vulnerable-population need unresolved",
        "provenance_documentation_gap": "map, report, imagery, sensor, forecast, resource, shelter, message, or decision provenance incomplete",
    }
    blockers = [message for key, message in checks.items() if context.get(key)]
    if blockers:
        return {"allowed": False, "reason": "disaster-response governance blocker", "blockers": blockers}
    return {"allowed": True, "reason": "disaster-response support package approved after qualified human command review"}


def review_required(action: str) -> bool:
    return action in PROTECTED_ACTIONS
