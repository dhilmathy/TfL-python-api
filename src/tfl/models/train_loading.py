from msrest.serialization import Model

class TrainLoading(Model):
    """TrainLoading.

    :param line:
    :type line: str
    :param line_direction:
    :type line_direction: str
    :param platform_direction:
    :type platform_direction: str
    :param direction:
    :type direction: str
    :param naptan_to:
    :type naptan_to: str
    :param time_slice:
    :type time_slice: str
    :param value:
    :type value: int
    """

    _attribute_map = {
        'line': {'key': 'line', 'type': 'str'},
        'line_direction': {'key': 'lineDirection', 'type': 'str'},
        'platform_direction': {'key': 'platformDirection', 'type': 'str'},
        'direction': {'key': 'direction', 'type': 'str'},
        'naptan_to': {'key': 'naptanTo', 'type': 'str'},
        'time_slice': {'key': 'timeSlice', 'type': 'str'},
        'value': {'key': 'value', 'type': 'int'}
    }

    def __init__(self, line=None, line_direction=None, platform_direction=None,
                 direction=None, naptan_to=None, time_slice=None, value=None):
        super(TrainLoading, self).__init__()
        self.line = line
        self.line_direction = line_direction
        self.platform_direction = platform_direction
        self.direction = direction
        self.naptan_to = naptan_to
        self.time_slice = time_slice
        self.value = value