from utils.timing import measure_time


class SimplePipeline:
    """
    Minimal pipeline for debugging or unit tests.
    """

    @measure_time
    async def run(self, text: str) -> str:
        return text.upper()
