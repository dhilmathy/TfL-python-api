from msrest.serialization import Model

class Prediction(Model):
    """Prediction.

    :param id:
    :type id: int
    :param operation_type:
    :type operation_type: int
    :param vehicle_id:
    :type vehicle_id: int
    :param naptan_id:
    :type naptan_id: str
    :param station_name:
    :type station_name: str
    :param line_id:
    :type line_id: str
    :param line_name:
    :type line_name: str
    :param platform_name:
    :type platform_name: str
    :param direction:
    :type direction: str
    :param bearing:
    :type bearing: str
    :param destination_naptan_id:
    :type destination_naptan_id: str
    :param destination_name:
    :type destination_name: str
    :param timestamp:
    :type timestamp: datetime
    :param time_to_station:
    :type time_to_station: datetime
    :param current_location:
    :type current_location: str
    :param towards:
    :type towards: str
    :param expected_arrival:
    :type expected_arrival: datetime
    :param time_to_live:
    :type time_to_live: datetime
    :param mode_name:
    :type mode_name: str
    :param timing:
    :type timing: :class:`PredictionTiming <models.PredictionTiming>`
    """

    _attribute_map = {
        'id': { 'key': 'id', 'type': 'int'},
        'operation_type': { 'key': 'operationType', 'type': 'int'},
        'vehicle_id': { 'key': 'vehicleId', 'type': 'int'},
        'naptan_id': { 'key': 'naptanId', 'type': 'str'},
        'station_name': { 'key': 'stationName', 'type': 'str'},
        'line_id': { 'key': 'lineId', 'type': 'str'},
        'line_name': { 'key': 'lineName', 'type': 'str'},
        'platform_name': { 'key': 'platformName', 'type': 'str'},
        'direction': { 'key': 'direction', 'type': 'str'},
        'bearing': { 'key': 'bearing', 'type': 'str'},
        'destination_naptan_id': { 'key': 'destinationNaptanId', 'type': 'str'},
        'destination_name': { 'key': 'destinationName', 'type': 'str'},
        'timestamp': { 'key': 'timestamp', 'type': 'iso-8601'},
        'time_to_station': { 'key': 'timeToStation', 'type': 'int'},
        'current_location': { 'key': 'currentLocation', 'type': 'str'},
        'towards': { 'key': 'towards', 'type': 'str'},
        'expected_arrival': { 'key': 'expectedArrival', 'type': 'iso-8601'},
        'time_to_live': { 'key': 'timeToLive', 'type': 'iso-8601'},
        'mode_name': { 'key': 'modeName', 'type': 'str'},
        'timing': { 'key': 'timing', 'type': 'PredictionTiming'}
    }

    def __init__(self, id=None, operation_type=None, vehicle_id=None, naptan_id=None, station_name=None, line_id=None,
                 line_name=None, platform_name=None, direction=None, bearing=None, destination_naptan_id=None,
                 destination_name=None, timestamp=None, time_to_station=None, current_location=None, towards=None,
                 expected_arrival=None, time_to_live=None, mode_name=None, timing=None):
        super(Prediction, self).__init__()
        self.id = id
        self.operation_type = operation_type
        self.vehicle_id = vehicle_id
        self.naptan_id = naptan_id
        self.station_name = station_name
        self.line_id = line_id
        self.line_name = line_name
        self.platform_name = platform_name
        self.direction = direction
        self.bearing = bearing
        self.destination_naptan_id = destination_naptan_id
        self.destination_name = destination_name
        self.timestamp = timestamp
        self.time_to_station = time_to_station
        self.current_location = current_location
        self.towards = towards
        self.expected_arrival = expected_arrival
        self.time_to_live = time_to_live
        self.mode_name = mode_name
        self.timing = timing