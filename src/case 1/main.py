import json
from typing import List
from task import MsgoPull, GridBuilder


class TasksTable:
    @classmethod
    def build(
        cls,
        tasks_list: List[str],
        pull: MsgoPull,
    ):
        rows = cls._get_table_rows(tasks_list, pull=pull)
        return GridBuilder().add_rows(rows).build()

    @classmethod
    def _get_table_rows(
        cls,
        tasks_list: List[str],
        pull: MsgoPull,
    ):
        """
        Notes:
            в userdata последней строки хранится суммарное время расчета всех задач таблицы
        """
        rows = []

        for task_dict_json in tasks_list:
            task_dict = json.loads(task_dict_json)
            task_data = get_all_task_details(task_dict, pull=pull)
            rza_names = task_data['rza_names']
            rza_functions = task_data['rza_functions']
            sgo_name = task_data['sgo_name']
            rza_location = task_data['rza_location']
            guarded_object = task_data['guarded_object']

            cells = cls._get_cells(
                rza_names=rza_names,
                rza_functions=rza_functions,
                rza_location=rza_location,
                sgo_name=sgo_name,
                guarded_object=guarded_object,
            )
            rows.append({'cells': cells})

        return rows

    @classmethod
    def _get_cells(cls, rza_names, rza_functions, rza_location, sgo_name, guarded_object):
        """
        Используется, в том числе для построения заголовков, чтобы задать последовательность столбцов, удалять нельзя
        """
        return [rza_names, rza_functions, rza_location, sgo_name, guarded_object]


def get_all_task_details(
    task_data: dict,
    pull: MsgoPull,
) -> dict:
    """
    Наполняет task_data данными для отображения в таблице msgo
    """
    rza_uids = task_data.get('rza_uids', [])
    rza_container = pull.rza_container
    rza_functions = (rza_container.get_by_rza_uid(rza_uid) for rza_uid in rza_uids)

    rza_names = ''
    rza_type = ''
    rza_location = ''
    guarded_object = ''

    for rza_function in rza_functions:
        rza_names += rza_function.name + '\n'
        rza_type += rza_function.rza_type + '\n'
        rza_location = rza_function.msgo_rm.relay_model.rza_location
        guarded_object = rza_function.msgo_rm.guarded_element.loc_name

    task_data['rza_names'] = rza_names
    task_data['rza_functions'] = rza_type

    if len(rza_uids) == 1:
        task_data['guarded_object'] = guarded_object
        task_data['rza_location'] = rza_location
    else:
        task_data['guarded_object'] = '-'
        task_data['rza_location'] = '-'

    return task_data
