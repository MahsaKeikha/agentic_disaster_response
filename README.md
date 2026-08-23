# F143 | Agentic Disaster Response | L3 Gold Standard | v1.0

A governed five-agent reference architecture for disaster-response decision support across situational awareness, humanitarian logistics, sheltering, public communications, life safety, accessibility, equity, recovery, evidence provenance, and qualified incident-command approval.

F143 can organize disaster reports, needs, resources, shelters, logistics dependencies, public-information drafts, recovery requirements, and review packages. It cannot autonomously dispatch responders, allocate scarce lifesaving resources, issue official warnings, open or close shelters, authorize reentry, impersonate an emergency authority, or distribute binding command instructions externally.

## Disaster-response lifecycle

```text
Situation Verification
        -> Needs and Damage Assessment
        -> Logistics and Resource Coordination
        -> Shelter and Essential-Service Support
        -> Public Information and Community Support
        -> Stabilization and Recovery Transition
        -> Qualified Incident Command Approval
        -> Human-Controlled Emergency Actions
```

The workflow fails closed when required reviews are missing or when material situational-awareness, life-safety, scarce-resource, logistics, shelter, public-information, accessibility, equity, or provenance risks remain unresolved.

## Five-agent architecture

| Agent | Responsibility | Core question |
|---|---|---|
| Situation Agent | Structures hazard, location, timing, damage, casualties, access, infrastructure, forecasts, source confidence, and uncertainty | What is happening, where, and how reliable is the evidence? |
| Logistics Agent | Tracks supplies, transport, staging, fuel, communications, personnel, routes, dependencies, requests, assignments, and constraints | What is needed and what can actually reach affected people? |
| Shelter Agent | Organizes shelter capacity, accessibility, medical support, sanitation, staffing, security, transport, pets, and habitability | Can displaced people be safely and equitably supported? |
| Communications Agent | Prepares traceable public-information and stakeholder communication support with authority, geography, accessibility, language, timing, and channel controls | What information can be prepared responsibly for authorized release? |
| Recovery Agent | Organizes damage, continuity, reentry, infrastructure restoration, housing, assistance, community recovery, and after-action learning | What is required to move from immediate response toward safe recovery? |

Agents support disaster-response organizations, emergency operations centers, incident commanders, humanitarian teams, shelters, public-information officers, logistics teams, healthcare systems, utilities, transportation agencies, community organizations, and recovery programs. They do not replace emergency command, medical authority, law enforcement, fire command, public-health authorities, structural-safety officials, humanitarian leadership, or government authority.

## Repository structure

```text
AGENTS/
├── situation_agent.py
├── logistics_agent.py
├── shelter_agent.py
├── communications_agent.py
└── recovery_agent.py

SKILLS/
├── situation_reasoning.py
├── logistics_reasoning.py
├── shelter_reasoning.py
├── communications_reasoning.py
└── recovery_reasoning.py

TOOLS/
├── situation_board.py
├── needs_matrix.py
├── resource_tracker.py
├── risk_register.py
└── command_gate.py

orchestration/
memory/
observability/
evals/
benchmarks/
examples/
docs/
prompts/
config/
safety/
tests/
.github/workflows/ci.yml
run.py
pyproject.toml
README.md
```

## Situation verification

The policy requires `situation_verified`.

Disaster information should preserve source, time, location, hazard, observation versus inference, confidence, corroboration, geographic scope, and supersession state. Reports from field teams, official agencies, sensors, social media, satellites, drones, news, community organizations, and affected people can differ in reliability and freshness.

`situational_awareness_gap` blocks release when material hazard, location, timing, casualty, access, or source-confidence information remains unresolved.

## Common operating picture

`TOOLS/situation_board.py` can organize current hazards, affected areas, roads, hospitals, shelters, utilities, communications, staging locations, resource routes, weather, forecasts, and verified field reports.

A map layer or dashboard is not automatically authoritative. Every operationally important layer should preserve update time and source.

## Damage and needs assessment

Damage and needs assessment should distinguish rapid estimates from verified assessments. Useful categories include housing, healthcare, water, sanitation, power, communications, transportation, food, shelter, protection, accessibility, livelihoods, schools, critical facilities, and environmental hazards.

Remote imagery can support triage but does not establish structural safety or habitability by itself.

## Casualty information

Casualty counts can change rapidly and may be incomplete, duplicated, or unverified. F143 must never fabricate or prematurely stabilize casualty figures.

## Search and rescue boundary

Search-and-rescue operations require qualified command, trained personnel, hazard assessment, equipment, communications, medical support, accountability, and safety procedures. F143 can support information organization but cannot direct people into collapsed, burning, flooded, contaminated, unstable, or otherwise hazardous environments.

## Life safety

The policy requires `life_safety_reviewed`.

`life_safety_risk` blocks release when survivor, responder, medical, structural, environmental, or access safety risks remain unresolved.

Life safety takes priority over speed, cost, property recovery, political pressure, or optimization metrics.

## Scarce lifesaving resources

`scarce_resource_risk` blocks release whenever allocation of scarce lifesaving resources requires accountable human command judgment.

Examples can include rescue teams, critical-care transport, oxygen, blood, dialysis, ventilators, emergency shelter capacity, medical evacuation, specialized rescue assets, limited water, or other resources whose allocation can materially affect survival.

`allocate_scarce_lifesaving_resources` is permanently protected.

F143 can display constraints and decision criteria but must not autonomously decide who receives a scarce lifesaving resource.

## Logistics architecture

The policy requires `logistics_reviewed`.

`TOOLS/resource_tracker.py` can preserve resource type, quantity, capability, owner, location, status, request, assignment, route, ETA, constraints, qualification, and update time.

`logistics_gap` blocks release when critical supply, transportation, fuel, communications, access, staffing, or staging dependencies remain unresolved.

## Humanitarian supply chain

Disaster logistics can involve water, food, shelter materials, medicines, fuel, generators, sanitation, hygiene, communications, PPE, bedding, accessibility equipment, infant supplies, and other essentials.

Supply availability should not be confused with deliverability. Roads, bridges, ports, airports, fuel, security, weather, customs, warehousing, staffing, and communications can all constrain distribution.

## Staging and distribution

Staging sites should consider access, safety, capacity, security, communications, loading, fuel, traffic, weather, staffing, and onward distribution.

F143 can recommend questions and track options but does not authorize tactical staging decisions.

## Transportation

Disaster transportation can involve ambulances, buses, accessible vehicles, trucks, helicopters, boats, rail, aviation, and pedestrian access. Operational use requires qualified human authority and real-time verification.

## Road and route status

Roads can be blocked by flood, debris, fire, structural damage, landslides, law-enforcement closures, traffic, damaged bridges, or ongoing hazards. Route data must be time stamped.

## Fuel

Fuel shortages can affect generators, ambulances, evacuation, delivery fleets, hospitals, shelters, and utility restoration. Fuel should be treated as a critical dependency rather than a generic commodity.

## Communications

Response teams may depend on radio, cellular, satellite, internet, amateur radio, runners, and other redundant methods. Communications outages can disrupt dispatch, logistics, healthcare, sheltering, and public information.

## Mutual aid and humanitarian partners

Requests and commitments should preserve requesting authority, providing organization, resource, quantity, mission, reporting location, time, duration, status, and constraints.

F143 cannot commit another organization's people, funds, equipment, or inventory.

## Dispatch boundary

`dispatch_response_resources` is protected.

Resource recommendations, route options, priorities, and availability reports do not constitute dispatch authority.

## Shelter architecture

The policy requires `shelter_reviewed`.

Shelter planning should consider capacity, accessibility, medical support, power, water, sanitation, food, staffing, security, privacy, transportation, communications, pets, service animals, children, older adults, medication, infection risk, and duration.

`shelter_safety_gap` blocks release when material shelter safety or habitability questions remain unresolved.

## Shelter opening and closure

`open_or_close_shelter` is protected.

Opening a site requires verified facility status, staffing, accessibility, sanitation, utilities, logistics, security, and authority. Closure can create displacement and must account for transportation and safe alternatives.

## Accessible sheltering

The policy requires `accessibility_equity_reviewed`.

Shelters should support people with mobility, vision, hearing, cognitive, respiratory, medical, communication, dietary, and other access needs as appropriate to the jurisdiction and operation.

## Medical shelter needs

Some displaced people require oxygen, dialysis, medication refrigeration, wound care, mobility support, power-dependent equipment, behavioral-health support, or other clinical services.

F143 can surface needs but does not provide clinical triage or medical treatment decisions.

## Sanitation and public health

Shelters and displacement sites can face sanitation, waste, food safety, respiratory illness, vector, water, and infection-control risks. Public-health guidance should come from qualified authorities.

## Protection and safeguarding

Disasters can increase exploitation, trafficking, domestic violence, abuse, theft, discrimination, and risks to children or isolated people. Shelter and assistance planning should include safeguarding and privacy.

## Accessibility and equity

`accessibility_equity_gap` blocks release when disability, language, transportation, medical, housing, documentation, or vulnerable-population needs remain materially unresolved.

Response planning should not assume equal access to vehicles, phones, internet, money, insurance, identification, housing, mobility, English, or social support.

## Older adults

Older adults may require transportation, medication, mobility assistance, communication support, caregiver coordination, refrigeration, oxygen, or continuity of home and community services.

## People with disabilities

Disaster response should consider accessible evacuation, transportation, shelter, communication, durable medical equipment, service animals, personal assistance, and continuity of support.

## Children and families

Children may require reunification, safeguarding, age-appropriate communication, school coordination, pediatric support, and supervision.

## Unhoused and precariously housed people

Response plans should account for people without conventional addresses, phones, transportation, secure document storage, or formal tenancy records.

## Language access

Safety-critical messages may require professional or qualified review in languages used by affected communities. Machine translation can support drafting but should not be treated as automatically reliable for emergency instructions.

## Public information architecture

The policy requires `communications_reviewed`.

A public-information draft should preserve issuing authority, audience, geographic scope, incident, timestamp, requested action, source, uncertainty, language, accessibility, channel, update expectation, and approval state.

`public_information_risk` blocks release when official-message authority, geography, timing, language, accessibility, or accuracy risks remain unresolved.

## Official warning boundary

`issue_official_warning` is protected.

F143 must never impersonate emergency management, fire, police, weather services, public health, humanitarian authorities, or government agencies.

## Rumor and misinformation management

Disaster misinformation can redirect people into danger, overwhelm shelters, create panic, impede response, or undermine legitimate authorities.

The system should distinguish verified facts, rumors, forecasts, recycled imagery, manipulated media, opinion, and unconfirmed reports.

## Social media evidence

Social posts can be valuable indicators but may be stale, geolocated incorrectly, duplicated, manipulated, or taken from another disaster. Operational conclusions require corroboration.

## Synthetic media

AI-generated images, audio, or video can create false evidence of damage, casualties, official statements, or resource conditions. Provenance and verification should be emphasized.

## Disaster types

F143 can support planning across earthquakes, floods, hurricanes, storms, tornadoes, wildfire, extreme heat, winter weather, landslides, tsunamis, infrastructure failure, public-health emergencies, and other disasters while preserving hazard-specific authority and expertise.

## Earthquake response

Earthquakes can create collapse, fire, utility failure, landslides, liquefaction, road disruption, medical surge, and aftershocks. Entry into damaged buildings requires qualified structural and rescue assessment.

## Flood response

Floods can create drowning risk, swift water, contamination, electrical hazards, road washouts, dam or levee concerns, isolation, and changing access.

## Wildfire response

Wildfire conditions can change rapidly with wind, fuels, terrain, smoke, roads, and fire behavior. Tactical fire operations and evacuation authority remain with qualified officials.

## Severe weather

Storm, tornado, hurricane, lightning, winter-weather, and extreme-heat response should use authoritative forecasting and local emergency guidance.

## Public-health disasters

Outbreaks and health emergencies require public-health, laboratory, healthcare, privacy, risk-communication, and clinical authority. F143 does not replace those functions.

## Hazardous-material incidents

Chemical, biological, radiological, nuclear, explosive, and industrial incidents require specialized responders and authoritative safety guidance. F143 should not provide instructions that enable harmful use or unsafe entry.

## Critical infrastructure

Power, water, wastewater, communications, healthcare, transportation, fuel, food distribution, and public safety can fail together. Disaster response should model dependencies and cascading effects.

## Utility restoration

Restoration priorities can affect hospitals, shelters, water systems, communications, transportation, refrigeration, fuel, and vulnerable populations. Actual utility switching and restoration decisions remain with authorized operators.

## Healthcare systems

Hospitals and clinics can experience surge, evacuation, power loss, water loss, staffing shortages, supply constraints, and communications failures.

F143 supports coordination and does not make patient-level clinical decisions.

## Recovery architecture

The policy requires `recovery_reviewed`.

Recovery planning can begin during response and include damage assessment, infrastructure restoration, debris, housing, assistance, schools, healthcare, businesses, environmental cleanup, public finance, cultural resources, and long-term resilience.

## Reentry

`authorize_reentry` is protected.

Reentry can depend on hazard stabilization, structural assessment, roads, utilities, contamination, fire conditions, public health, inspection, and jurisdictional authority.

## Housing recovery

Recovery should consider emergency shelter, temporary housing, rental supply, repairs, reconstruction, insurance, assistance, accessibility, displacement, and long-term community stability.

## Debris management

Debris can involve hazardous materials, damaged infrastructure, private property, environmental rules, transportation, staging, disposal, recycling, and worker safety.

## Economic recovery

Businesses, workers, agriculture, tourism, supply chains, and household finances can be heavily affected. Recovery analysis should include distributional consequences.

## Community recovery

Affected communities should participate in recovery priorities. F143 should not substitute model-generated preferences for real community engagement.

## Cultural and historic resources

Disasters can affect cultural sites, archives, museums, religious sites, indigenous resources, and historic structures. Recovery may require specialized consultation.

## Mental health and psychosocial support

Survivors, responders, caregivers, children, and communities can experience grief, trauma, exhaustion, and prolonged stress. F143 can support planning and referral, not mental-health diagnosis or treatment.

## Fatality and family assistance

Fatality management, identification, family notification, mortuary operations, and family assistance require specialized authorities, dignity, privacy, and established procedures.

## Privacy

Disaster-response data can expose health, disability, identity, household, location, immigration, shelter, and contact information. Operational urgency does not eliminate privacy obligations.

## Security

Responder locations, shelter vulnerabilities, critical-infrastructure conditions, access credentials, and tactical information can be sensitive. Access should follow legitimate operational need.

## Documentation and provenance

`provenance_documentation_gap` blocks release when map, report, imagery, sensor, forecast, resource, shelter, message, or decision provenance is incomplete.

F143 must never fabricate disaster boundaries, casualty counts, official orders, shelter status, resource availability, road status, hospital status, forecasts, authority, or reentry conditions.

## Memory and state

The `memory/` layer can preserve situation reports, hazards, needs, resources, shelter state, public-information drafts, logistics dependencies, recovery state, approvals, and unresolved issues.

It should distinguish current, stale, unverified, superseded, forecast, simulated, exercise, and real-disaster information.

## Observability

The `observability/` layer supports traceability across situation, logistics, shelter, communications, life safety, accessibility, equity, recovery, provenance, and governance.

Useful telemetry includes source freshness, open needs, logistics gaps, shelter capacity, shelter blockers, scarce-resource escalations, public-information blockers, accessibility findings, approvals, and protected-action attempts.

## Required reviews

The executable policy requires all eight conditions:

```text
situation_verified
logistics_reviewed
shelter_reviewed
communications_reviewed
life_safety_reviewed
accessibility_equity_reviewed
recovery_reviewed
qualified_incident_command_approval
```

Missing any condition fails closed.

## Fail-closed governance

The implemented policy blocks release when:

- material hazard, location, timing, casualty, access, or source-confidence information remains unresolved
- survivor, responder, medical, structural, environmental, or access safety risk remains unresolved
- scarce lifesaving resource allocation requires accountable human command judgment
- critical supply, transport, fuel, communications, access, staffing, or staging dependencies remain unresolved
- shelter capacity, accessibility, medical, sanitation, security, staffing, or habitability issues remain unresolved
- official-message authority, geography, timing, language, accessibility, or accuracy risks remain unresolved
- disability, language, transportation, medical, housing, documentation, or vulnerable-population needs remain unresolved
- map, report, imagery, sensor, forecast, resource, shelter, message, or decision provenance is incomplete
- any required review is missing
- qualified incident-command approval is missing

The system exposes blockers rather than manufacturing certainty, authority, shelter readiness, resource availability, warning status, or command approval.

## Protected actions

The safety policy permanently protects:

```text
dispatch_response_resources
allocate_scarce_lifesaving_resources
issue_official_warning
open_or_close_shelter
authorize_reentry
external_command_distribution
```

These remain outside autonomous authority even after all required reviews are satisfied.

## Human authority boundaries

F143 must not autonomously dispatch responders, allocate scarce lifesaving resources, open or close shelters, issue official warnings, make tactical rescue decisions, authorize reentry, commit external resources, impersonate authorities, or distribute binding command instructions.

Qualified humans retain control over incident command, rescue, dispatch, scarce-resource allocation, shelter operation, public warnings, healthcare, structural safety, reentry, and external command actions.

## Explicit failure states

```text
SITUATION VERIFICATION REQUIRED
LOGISTICS REVIEW REQUIRED
SHELTER REVIEW REQUIRED
COMMUNICATIONS REVIEW REQUIRED
LIFE SAFETY REVIEW REQUIRED
ACCESSIBILITY AND EQUITY REVIEW REQUIRED
RECOVERY REVIEW REQUIRED
QUALIFIED INCIDENT COMMAND APPROVAL REQUIRED
SITUATIONAL AWARENESS GAP
LIFE SAFETY RISK
SCARCE RESOURCE ESCALATION REQUIRED
LOGISTICS GAP
SHELTER SAFETY GAP
PUBLIC INFORMATION RISK
ACCESSIBILITY OR EQUITY GAP
PROVENANCE DOCUMENTATION GAP
AUTONOMOUS DISPATCH PROHIBITED
SCARCE LIFESAVING RESOURCE ALLOCATION PROHIBITED
OFFICIAL WARNING ISSUANCE PROHIBITED
AUTONOMOUS SHELTER OPEN OR CLOSE PROHIBITED
AUTONOMOUS REENTRY AUTHORIZATION PROHIBITED
EXTERNAL COMMAND DISTRIBUTION PROHIBITED
```

## End-to-end reference workflow

1. Register disaster reports with source, location, time, confidence, verification, and supersession state.
2. Build a common operating picture using verified field information, maps, imagery, forecasts, sensors, infrastructure status, access routes, and authoritative sources.
3. Identify immediate life-safety issues, affected populations, damage, access constraints, healthcare needs, and scarce-resource escalations.
4. Build a needs matrix and logistics plan covering food, water, shelter, medical, transport, fuel, communications, staffing, staging, and dependencies.
5. Track shelter capacity, accessibility, medical needs, sanitation, staffing, security, transportation, pets, and habitability.
6. Draft public-information support with issuing authority, geography, timing, action, accessibility, language, source, uncertainty, and approval controls.
7. Review disability, language, transportation, medical, housing, documentation, child, older-adult, and other vulnerable-population needs.
8. Track infrastructure dependencies, utility status, healthcare capacity, routes, humanitarian partners, and mutual-aid constraints.
9. Begin reentry, damage, debris, housing, infrastructure-restoration, assistance, community-recovery, and after-action planning during response.
10. Preserve provenance for maps, reports, imagery, sensors, forecasts, resources, shelters, messages, and decisions.
11. Apply fail-closed governance and require qualified incident-command approval.
12. Keep dispatch, scarce-resource allocation, official warnings, shelter opening or closure, reentry authorization, and binding external command distribution outside autonomous authority.

## Evaluation and held-out governance suite

The repository contains evaluation logic under `evals/` and benchmark cases under `benchmarks/`.

Evaluation should test source verification, situational awareness, humanitarian logistics, shelter reasoning, life-safety escalation, accessibility and equity awareness, communications safety, provenance, and governance behavior.

The behavioral verification layer includes direct governance tests and a 10-scenario held-out suite covering missing review, approved support release, situational-awareness gaps, life-safety risks, scarce-resource escalation, logistics gaps, shelter-safety gaps, public-information risks, accessibility or equity gaps, and provenance gaps.

## Verification gates

CI runs on Python 3.10, 3.11, and 3.12 and requires:

```bash
ruff check . --select E9,F63,F7,F82
python -m pytest -q
python evals/held_out.py
python run.py
```

These gates verify syntax-critical linting, fail-closed behavior, held-out governance scenarios, and execution of the governed reference workflow.

## Reproducibility

Reproducible disaster-response review requires preserving situation version, sources, maps, imagery, forecasts, needs, resource status, shelter state, public-information drafts, accessibility findings, approvals, and unresolved risks.

## Extension points

Organization-specific implementations can add governed integrations for GIS, satellite imagery, weather and hazard feeds, disaster-management platforms, resource systems, warehouse and logistics systems, shelter systems, hospital status, roads, utilities, damage assessment, public-information platforms, humanitarian case management, and recovery systems.

Any integration capable of dispatching responders, allocating scarce lifesaving resources, issuing official warnings, opening or closing shelters, changing official incident state, authorizing reentry, or distributing binding commands should remain behind explicit authorization, least privilege, audit logging, authenticated authority, and human-controlled execution.

## Example applications

Potential governed uses include disaster operations center support, situation reports, humanitarian logistics, needs assessment, shelter coordination, public-information drafting, earthquake response, flood response, wildfire support, hurricane response, infrastructure-outage coordination, damage assessment, reentry planning, housing recovery, and after-action review.

F143 is not an autonomous incident commander, dispatcher, rescue authority, scarce-resource allocation authority, shelter operator, warning authority, structural-safety official, medical director, humanitarian commander, or reentry authority.

## Design principles

1. Verify disaster information before turning it into operational support.
2. Preserve source, timestamp, location, confidence, uncertainty, and supersession state.
3. Never convert AI-generated recommendations into commands, dispatches, official warnings, or scarce-resource allocation decisions.
4. Never fabricate casualties, hazard boundaries, shelter status, resource availability, road status, forecasts, or authority.
5. Treat accessibility, language, transportation, medical needs, housing, and vulnerable populations as core response requirements.
6. Treat scarce lifesaving resources as accountable human-command decisions.
7. Preserve provenance and distinguish verified facts, forecasts, simulations, exercises, assumptions, rumors, and synthetic media.
8. Fail closed when situation, safety, logistics, shelter, communications, equity, provenance, or approval is incomplete.
9. Keep dispatch, lifesaving allocation, official warnings, shelter authority, reentry, and external command under qualified human control.

## Scope statement

F143 demonstrates a governed multi-agent architecture for disaster-response decision support. It combines specialized situation, logistics, shelter, communications, and recovery agents with deterministic situation, needs, resource, risk, and command tools, observability, held-out evaluation, and fail-closed governance while preserving strict human authority over response dispatch, scarce lifesaving resources, shelters, official warnings, reentry, and binding external actions.

Author: Mahsa Keikha
