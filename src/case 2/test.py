from topology_object import TopologyObject
from protected_types import ProtectedTR3Type

if __name__ == '__main__':
    topology_object = TopologyObject()
    print(topology_object.get_setpoints(ProtectedTR3Type, 'object'))
