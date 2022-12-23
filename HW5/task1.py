class MinStack:

    def __init__(self):
        self.data = []
        self.minElem = []

    def push(self, val) -> None:
        self.data.append(val)
        if len(self.minElem) == 0 or val <= self.minElem[len(self.minElem) - 1]:
            self.minElem.append(val)

    def pop(self) -> None:
        if self.minElem[len(self.minElem) - 1] == self.data[len(self.data) - 1]:
            self.minElem.pop()
        self.data.pop()

    def top(self) -> int:
        return self.data[len(self.data) - 1]

    def getMin(self) -> int:
        return self.minElem[len(self.minElem) - 1]
