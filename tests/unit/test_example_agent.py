from src.agent.example_agent import build_example_agent


def test_single_step_echo():
    agent = build_example_agent()
    result = agent.run("hello")
    assert result == "hello"


def test_single_step_upper():
    agent = build_example_agent()
    result = agent.run("make upper")
    assert result == "MAKE UPPER"


def test_multi_step():
    agent = build_example_agent()
    result = agent.run("run steps")
    assert result == "RUN STEPS"
