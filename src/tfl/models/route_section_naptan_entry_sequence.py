from msrest.serialization import Model

class RouteSectionNaptanEntrySequence(Model):
    """RouteSectionNaptanEntrySequence.

    :param ordinal:
    :type ordinal: int
    :param stop_point:
    :type stop_point: :class:`StopPoint <models.StopPoint>`
    """

    _attributes_map = {
        'ordinal': {'key': 'ordinal', 'type': 'int'},
        'stop_point': {'key': 'stopPoint', 'type': 'StopPoint'}
    }

    def __init__(self, ordinal=None, stop_point=None):
        super(RouteSectionNaptanEntrySequence, self).__init__()
        self.ordinal = ordinal
        self.stop_point = stop_point