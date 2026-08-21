from orchestration.orchestrator import run
def test_run(): assert run({'event':'x'})['system']=='F143'
