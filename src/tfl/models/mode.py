from msrest.serialization import Model

class Mode(Model):
    """Mode.

    :param is_tfl_service:
    :type is_tfl_service: bool
    :param is_fare_paying:
    :type is_fare_paying: bool
    :param is_scheduled_service:
    :type is_scheduled_service: bool
    :param mode_name:
    :type mode_name: str
    """

    _attribute_map = {
        'is_tfl_service': {'key': 'isTflService', 'type': 'bool'},
        'is_fare_paying': {'key': 'isFarePaying', 'type': 'bool'},
        'is_scheduled_service': {'key': 'isScheduledService', 'type': 'bool'},
        'mode_name': {'key': 'modeName', 'type': 'str'}
    }

    def __init__(self, is_tfl_service=None, is_fare_paying=None, is_scheduled_service=None, mode_name=None):
        super(Mode, self).__init__()
        self.is_tfs_service = is_tfl_service
        self.is_fare_paying = is_fare_paying
        self.is_scheduled_service = is_scheduled_service
        self.mode_name = mode_name