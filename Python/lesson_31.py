class TrainingResource:
    def __enter__(self):
        print("Resource acquired")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Resource released")
        # Do not suppress exceptions

with TrainingResource() as resource:
    print("Training model....")

