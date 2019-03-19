class NewClass:

    def __init__(self, class_name: str) -> None:
        self.class_name = class_name
        self.attribute = []
        self.method = []
        self.relationship = []

    def __str__(self) -> str:
        return self.class_name

    def add_method(self, methodName: str) -> None:
        self.method.append(methodName)

    def add_attribute(self, attribute: str) -> None:
        self.attribute.append(attribute)

    def add_relationship(self, relationship: str) -> None:
        self.relationship.append(relationship)




