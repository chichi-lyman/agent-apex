# Copyright © 2026 Chelsea Megan Woods
from src.agent import ApexAgent


def test_apex_never_auto_spends():
    agent = ApexAgent()
    rec = agent.recommend("increase MRR")
    assert rec.policy == "REQUIRE_APPROVAL"
