from msrest.serialization import Model

class Disruption(Model):
    _attribute_map = {
        'category': {'key': 'category', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'category_description': {'key': 'categoryDescription', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'summary': {'key': 'summary', 'type': 'str'},
        'additional_info': {'key': 'additionalInfo', 'type': 'str'},
        'created': {'key': 'created', 'type': 'iso-8601'},
        'last_update': {'key': 'lastUpdate', 'type': 'iso-8601'},
        'affected_routes': {'key': 'affectedRoutes', 'type': '[AffectedRoute]'},
        'affected_stops': {'key': 'affectedStops', 'type': '[StopPoint]'},
        'closure_text': {'key': 'closureText', 'type': 'str'}
    }

    def __init__(self, category=None, type=None, category_description=None, description=None,
                 summary=None, additional_info=None, created=None, last_update=None,
                 affected_routes=None, affected_stops=None, closure_text=None):
        super(Disruption, self).__init__()
        self.category = category
        self.type = type
        self.category_description = category_description
        self.description = description
        self.summary = summary
        self.additional_info = additional_info
        self.created = created
        self.last_update = last_update
        self.affected_routes = affected_routes
        self.affected_stops = affected_stops
        self.closure_text = closure_text