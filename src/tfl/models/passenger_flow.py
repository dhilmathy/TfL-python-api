from msrest.serialization import Model

class PassengerFlow(Model):
    """PassengerFlow.

    :param time_slice:
    :type time_slice: str
    :param value:
    :type value: int
    """

    _attribute_map = {
        'time_slice': {'key': 'timeSlice', 'type': 'str'},
        'value': {'key': 'value', 'type': 'int'}
    }

    def __init__(self, time_slice=None, value=None):
        super(PassengerFlow, self).__init__()
        self.time_slice = passenger_flows
        self.value = value