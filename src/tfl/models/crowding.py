from msrest.serialization import Model

class Crowding(Model):
    """Crowding.

    :param passenger_flows:
    :type passenger_flows: list of :class:`PassengerFlow <models.PassengerFlow>`
    :param train_loadings:
    :type train_loadings: list of :class:`TrainLoading <models.TrainLoading>`
    """

    _attribute_map = {
        'passenger_flows': {'key': 'passengerFlow', 'type': '[PassengerFlow]'},
        'train_loadings': {'key': 'trainLoadings', 'type': '[TrainLoading]'}
    }

    def __init__(self, passenger_flows=None, train_loadings=None):
        super(Crowding, self).__init__()
        self.passenger_flows = passenger_flows
        self.train_loadings = train_loadings