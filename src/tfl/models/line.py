from msrest.serialization import Model

class Line(Model):
    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'mode_name': {'key': 'modeName', 'type': 'str'},
        'disruptions': {'key': 'disruptions', 'type': '[Disruption]'},
        'created': {'key': 'created', 'type': 'iso-8601'},
        'modified': {'key': 'modified', 'type': 'iso-8601'},
        'line_statuses': {'key': 'lineStatuses', 'type': '[LineStatus]'},
        'route_sections': {'key': 'routeSections', 'type': '[RouteSection]'},
        'service_types': {'key': 'serviceTypes', 'type': '[ServiceType]'},
        'crowding': {'key': 'crowding', 'type': 'Crowding'}
    }

    def __init__(self, id=None, name=None, mode_name=None, disruptions=None, created=None, modified=None, 
                 line_statuses=None, route_sections=None, service_types=None, crowding=None):
        super(Line, self).__init__()
        self.id = id
        self.name = name
        self.mode_name = mode_name
        self.disruptions = disruptions
        self.created = created
        self.modified = modified
        self.line_statuses = line_statuses
        self.route_sections = route_sections
        self.service_types = service_types
        self.crowding = crowding