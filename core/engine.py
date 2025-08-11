class Engine:
    def __init__(self, engine_type):
        self.engine_type = engine_type

    def start(self):
        return f"{self.engine_type} engine started."
