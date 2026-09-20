# Copyright © 2026 Chelsea Megan Woods
from src.agent import ApexAgent


def test_apex_allow_autonomous():
    agent = ApexAgent()
    rec = agent.recommend("increase MRR")
    assert rec.policy == "ALLOW"
    assert agent.default_policy == "ALLOW"
