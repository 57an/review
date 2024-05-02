from .utils import TopologyBusbar

class TopologyBranchModel:
    """
    Виртуальная модель ветви

    Notes:
        Содержит набор линий от busbar1 до busbar2 в порядке их расположения в списке lines
        elements не содержит входного выключателя, т.к. строит путь уже от ячейки первой линии в пути,
        т.е. с ячейки после этого выключателя
    """

    def __init__(self, tb: TopologyBusbar = None, switches=None, is_tap=False, only_connected=True):
        """
        Args:
             tb: TopologyBusbar
             is_tap(bool): True, если это отпайка.
        """
        self._is_tap = is_tap
        self._elements = []
        self._lines = []
        self._uid = None
        if tb is not None:
            self._elements = tb.get_elements(only_connected=only_connected)
            self._lines = self.__find_inner_lines()
            self._uid = self._create_uid()

        self._switches = self.__find_inner_switches() if switches is None else switches
        self._internal_busbars = self._get_internal_busbars()
        self._name = ''
        self._busbars_name = ''
        self._deadlock = None

    def add_elements(self, elements):
        self._elements.extend(elements)
        # Обновление линий
        self._lines = self.__find_inner_lines()

    def add_switches(self, switches):
        self._switches.extend(switches)

    @classmethod
    def from_dict(cls, data: dict, read_only):
        tbm = cls()
        tbm._loads(data, read_only)

    def _loads(self, data: dict, read_only):
        self._uid = data['full_name']
        self._name = data['name']
        self._is_tap = data['is_tap']
        self._deadlock = data.get('deadlock')
        elements = []
        switches = []
        if read_only:
            elements = data.get('elements')
            switches = data.get('switches')
        else:
            for el in data.get('elements'):
                elements.append(el)
            for sw in data.get('switches', []):
                switches.append(sw)

        if elements:
            self.add_elements(elements)

        if switches:
            self.add_switches(switches)
        else:
            self._switches = self.__find_inner_switches()

    # методы ниже показаны без тела, чисто чтобы pycharm не подчеркивал код выше

    def __find_inner_switches(self):
        return []

    def __find_inner_lines(self):
        return []

    def _create_uid(self):
        return ''

    def _get_internal_busbars(self):
        return []
