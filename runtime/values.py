class ValueType:
    null = "null"
    number = "number"

class RuntimeVal:
    def __init__(self, type:ValueType) -> None:
        self.type = type
    def __repr__(self) -> str:
        return f"RuntimeVal(type: {self.type})"

class NullVal(RuntimeVal):
    def __init__(self) -> None:
        super().__init__(ValueType.null)
        self.value = "null"
    def __repr__(self) -> str:
        return f"NullVal(type: {self.type}, value: {self.value})"

class NumberVal(RuntimeVal):
    def __init__(self, value:float) -> None:
        super().__init__(ValueType.number)
        self.value = value
    def __repr__(self) -> str:
        return f"NumberVal(type: {self.type}, value: {self.value})"