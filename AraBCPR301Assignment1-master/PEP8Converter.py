class PEP8Converter:
    @staticmethod
    def convert_class(plant_class_name: str) -> str:
        class_name = plant_class_name.capitalize()
        class_name = "class {}:\n".format(class_name)
        return class_name

    @staticmethod
    def convert_method(plant_method: str) -> str:
        if ":" in plant_method:
            method_and_type = plant_method.split(":")
            return_type = method_and_type[1].strip()
            method = method_and_type[0][0].lower() + method_and_type[0][1:].rstrip()
            method_name = "\n    def {}:\n        return {}\n".format(method, return_type)
            return method_name
        else:
            plant_method = plant_method[0].lower() + plant_method[1:]
            method_name = "\n    def {}:\n        return\n".format(plant_method)
            return method_name

    @staticmethod
    def convert_attribute(plant_attribute: str) -> str:
        attribute_and_type = plant_attribute.split(":")
        return_type = attribute_and_type[1].strip()
        attribute = attribute_and_type[0][0].lower() + attribute_and_type[0][1:].strip()
        an_attribute = "    {} = {}\n".format(attribute, return_type)
        return an_attribute

    # def convert_constructor():
    #     pass
    @staticmethod
    def create_class(plant_class_name: str) -> str:
        methods = ""
        attributes = ""
        constructor = "\n    def __init__(self): \n        pass\n"

        class_name = PEP8Converter.convert_class(plant_class_name.class_name)
        for aMethod in plant_class_name.method:
            methods += PEP8Converter.convert_method(aMethod)
        for an_attribute in plant_class_name.attribute:
            attributes += PEP8Converter.convert_attribute(an_attribute)
        return class_name + attributes + constructor + methods



