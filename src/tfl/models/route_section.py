from msrest.serialization import Model

class RouteSection(Model):
    _attribute_map = {
        'route_code': {'key': 'routeCode', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'direction': {'key': 'direction', 'type': 'str'},
        'origination_name': {'key': 'originationName', 'type': 'str'},
        'destination_name': {'key': 'destinationName', 'type': 'str'},
        'originator': {'key': 'originator', 'type': 'str'},
        'destination': {'key': 'destination', 'type': 'str'},
        'service_type': {'key': 'serviceType', 'type': 'str'},
        'valid_to': {'key': 'validTo', 'type': 'iso-8601'},
        'valid_from': {'key': 'validFrom', 'type': 'iso-8601'}
    }

    def __init__(self, route_code=None, name=None, direction=None, origination_name=None, 
                 destination_name=None, originator=None, destination=None, 
                 service_type=None, valid_to=None, valid_from=None):
        super(RouteSection, self).__init__()
        self.route_code = route_code
        self.name = name
        self.direction = direction
        self.origination_name = origination_name
        self.destination_name = destination_name
        self.originator = originator
        self.destination = destination
        self.service_type = service_type
        self.valid_to = valid_to
        self.valid_from = valid_from