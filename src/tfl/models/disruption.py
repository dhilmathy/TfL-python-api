from msrest.serialization import Model

class Disruption(Model):
    """Disruption.

    :param category:
    :type category: str
    :param type:
    :type type: str
    :param category_description:
    :type category_description: str
    :param description:
    :type description: str
    :param summary:
    :type summary: str
    :param additional_info:
    :type additional_info: str
    :param created:
    :type created: datetime
    :param last_update:
    :type last_update: datetime
    :param affected_routes:
    :type affected_routes: list of :class:`AffectedRoute <models.AffectedRoute>`
    :param affected_stops:
    :type affected_stops: list of :class:`StopPoint <models.StopPoint>`
    :param closure_text:
    :type closure_text: str
    """

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