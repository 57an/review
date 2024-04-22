from protected_types import ProtectedTR3Type, ProtectedGeneratorType


class ElmTr3GeneratorProperties:
    def __init__(self, topology_object):
        self.obj = topology_object

    def value(self):
        """На самом деле логика сложнее, и завязана на других полях этого класса"""
        return '1' if self.obj.object_type == ProtectedTR3Type.BLOCK else '2'


class ElmSymGeneratorProperties:
    def __init__(self, topology_object):
        self.obj = topology_object

    def value(self):
        """На самом деле логика сложнее, и завязана на других полях этого класса"""
        return '1' if self.obj.object_type == ProtectedGeneratorType.HYDRO else '2'


class ElmVacGeneratorProperties:
    def __init__(self, topology_object):
        self.obj = topology_object

    def value(self):
        """На самом деле логика сложнее, и завязана на других полях этого класса"""
        return '1' if self.obj.object_type == ProtectedGeneratorType.TURBO else '2'
