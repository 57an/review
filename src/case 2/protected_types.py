from properties import ElmTr3GeneratorProperties, ElmSymGeneratorProperties, ElmVacGeneratorProperties


class ProtectedTR3Type:
    BLOCK = 'BLOCK'  # Трансформатор блока
    CONNECTION = 'CONNECTION'  # Трансформатор связи

    @classmethod
    def blank_properties(cls, pf_object):
        return ElmTr3GeneratorProperties


class ProtectedGeneratorType:
    HYDRO = 'HYDRO'  # Гидрогенератор
    TURBO = 'TURBO'  # Турбогенератор

    @classmethod
    def blank_properties(cls, pf_object):
        if pf_object.cls_type == 'ElmSym':
            return ElmSymGeneratorProperties
        elif pf_object.cls_type == 'ElmVac':
            return ElmVacGeneratorProperties
