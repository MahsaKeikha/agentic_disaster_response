from AGENTS import communications_agent, logistics_agent, recovery_agent, shelter_agent, situation_agent
from safety.policy import authorize


def run(case: dict) -> dict:
    result = {
        "situation": situation_agent.run(case),
        "logistics": logistics_agent.run(case),
        "shelter": shelter_agent.run(case),
        "communications": communications_agent.run(case),
        "recovery": recovery_agent.run(case),
    }
    governance = authorize("release_support_package", case.get("governance", {}))
    result["governance"] = governance
    result["released"] = governance["allowed"]
    return result
