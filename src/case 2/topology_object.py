class TopologyObject:
    def __init__(self):
        ...

    def get_setpoints(self, type_class, element):
        blank_properties = type_class.blank_properties(element)
        if blank_properties is not None:
            return blank_properties(self)
