from msrest.serialization import Model

class RouteSectionNaptanEntrySequence(Model):
    _attributes_map = {
        'ordinal': {'key': 'ordinal', 'type': 'int'},
        'stop_point': {'key': 'stopPoint', 'type': 'StopPoint'}
    }

    def __init__(self, ordinal=None, stop_point=None):
        super(RouteSectionNaptanEntrySequence, self).__init__()
        self.ordinal = ordinal
        self.stop_point = stop_point