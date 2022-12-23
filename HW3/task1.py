class OneIndexedList:
    def __init__(self, items=None):
        self.values = items or []

    def __getitem__(self, index: int) -> any:
        return self.values[index - 1]

    def __setitem__(self, index: int, value: any) -> None:
        self.values[index - 1] = value
