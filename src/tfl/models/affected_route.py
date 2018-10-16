from msrest.serialization import Model

class AffectedRoute(Model):
    """AffectedRoute.

    :param id:
    :type id: str
    :param line_id:
    :type line_id: str
    :param route_code:
    :type route_code: str
    :param name:
    :type name: str
    :param line_string:
    :type line_string: str
    :param direction:
    :type direction: str
    :param origination_name:
    :type origination_name: str
    :param destination_name:
    :type destination_name: str
    :param valid_to:
    :type valid_to: datetime
    :param valid_from:
    :type valid_from: datetime
    :param route_section_naptan_entry_sequence:
    :type route_section_naptan_entry_sequence: list of :class:`RouteSectionNaptanEntrySequence <models.RouteSectionNaptanEntrySequence>`
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'line_id': {'key': 'lineId', 'type': 'str'},
        'route_code': {'key': 'routeCode', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'line_string': {'key': 'lineString', 'type': 'str'},
        'direction': {'key': 'direction', 'type': 'str'},
        'origination_name': {'key': 'originationName', 'type': 'str'},
        'destination_name': {'key': 'destinationName', 'type': 'str'},
        'valid_to': {'key': 'validTo', 'type': 'iso-8601'},
        'valid_from': {'key': 'validFrom', 'type': 'iso-8601'},
        'route_section_naptan_entry_sequence': {'key': 'routeSectionNaptanEntrySequence', 'type': '[RouteSectionNaptanEntrySequence]'}
    }

    def __init__(self, id=None, line_id=None, route_code=None, name=None,
                 line_string=None, direction=None, origination_name=None, destination_name=None,
                 valid_to=None, valid_from=None, route_section_naptan_entry_sequence=None):
        super(AffectedRoute, self).__init__()
        self.id = id
        self.line_id = line_id
        self.route_code = route_code
        self.name = name
        self.line_string = line_string
        self.direction = direction
        self.origination_name = origination_name
        self.destination_name = destination_name
        self.valid_to = valid_to
        self.valid_from = valid_from
        self.route_section_naptan_entry_sequence = route_section_naptan_entry_sequence