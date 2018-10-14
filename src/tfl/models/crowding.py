from msrest.serialization import Model

class Crowding(Model):
    _attribute_map = {
        'passenger_flows': {'key': 'passengerFlow', 'type': '[PassengerFlow]'},
        'train_loadings': {'key': 'trainLoadings', 'type': '[TrainLoading]'}
    }

    def __init__(self, passenger_flows=None, train_loadings=None):
        super(Crowding, self).__init__()
        self.passenger_flows = passenger_flows
        self.train_loadings = train_loadings