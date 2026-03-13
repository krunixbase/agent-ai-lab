class Memory:
    def __init__(self):
        self.buffer = []

    def store(self, role: str, content: str):
        self.buffer.append({"role": role, "content": content})

    def get(self):
        return self.buffer
