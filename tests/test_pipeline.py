from src.pipelines.openai_pipeline import OpenAIPipeline

def test_pipeline_returns_dict():
    pipeline = OpenAIPipeline()
    result = pipeline.plan("hello")
    assert isinstance(result, dict)
    assert "action" in result
    assert "input" in result
