from msrest.serialization import Model

class StopPoint(Model):
    """StopPoint.

    :param naptan_id:
    :type naptan_id: str
    :param platform_name:
    :type platform_name: str
    :param indicator:
    :type indicator: str
    :param stop_letter:
    :type stop_letter: str
    :param modes:
    :type modes: list of str
    :param ics_code:
    :type ics_code: str
    :param sms_code:
    :type sms_code: str
    :param stop_type:
    :type stop_type: str
    :param station_naptan:
    :type station_naptan: str
    :param accessibility_summary:
    :type accessibility_summary: str
    :param hub_naptan_code:
    :type hub_naptan_code: str
    :param lines:
    :types lines: list of :class:`Line <models.Line>`
    :param line_group:
    :type line_group: list of :class:`LineGroup <models.LineGroup>`
    :param line_mode_group:
    :type line_mode_group: list of :class:`LineModeGroup <models.LineModeGroup>`
    :param full_name:
    :type full_name: str
    :param naptan_mode:
    :type naptan_mode: str
    :param status:
    :type status: str
    :param id:
    :type id: str
    :param url:
    :type url: str
    :param common_name:
    :type common_name: str
    :param distance:
    :type distance: int
    :param place_type:
    :type place_type: str
    :param additional_properties:
    :type additional_properties: list of :class:`AdditionalProperties <models.AdditionalProperties>`
    :param children:
    :type children: list of :class:`StopPoint <models.StopPoint>`
    :param children_urls:
    :type children_urls: list of str
    :param lat:
    :type lat: int
    :param lon:
    :type lon: int
    """

    _attribute_map = {
        'naptan_id': {'key': 'naptanId', 'type': 'str'},
        'platform_name': {'key': 'platformName', 'type': 'str'},
        'indicator': {'key': 'indicator', 'type': 'str'},
        'stop_letter': {'key': 'stopLetter', 'type': 'str'},
        'modes': {'key': 'modes', 'type': '[str]'},
        'ics_code': {'key': 'icsCode', 'type': 'str'},
        'sms_code': {'key': 'smsCode', 'type': 'str'},
        'stop_type': {'key': 'stopType', 'type': 'str'},
        'station_naptan': {'key': 'stationNaptan', 'type': 'str'},
        'accessibility_summary': {'key': 'accessibilitySummary', 'type': 'str'},
        'hub_naptan_code': {'key': 'hubNaptanCode', 'type': 'str'},
        'lines': {'key': 'lines', 'type': '[Line]'},
        'line_group': {'key': 'lineGroup', 'type': '[LineGroup]'},
        'line_mode_groups': {'key': 'lineModeGroups', 'type': '[LineModeGroup]'},
        'full_name': {'key': 'fullName', 'type': 'str'},
        'naptan_mode': {'key': 'naptanMode', 'type': 'str'},
        'status': {'key': 'status', 'type': 'bool'},
        'id': {'key': 'id', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'common_name': {'key': 'commonName', 'type': 'str'},
        'distance': {'key': 'distance', 'type': 'int'},
        'place_type': {'key': 'placeType', 'type': 'str'},
        'additional_properties': {'key': 'additionalProperties', 'type': '[AdditionalProperties]'},
        'children': {'key': 'children', 'type': '[StopPoint]'},
        'children_urls': {'key': 'childrenUrls', 'type': '[str]'},
        'lat': {'key': 'lat', 'type': 'int'},
        'lon': {'key': 'lon', 'type': 'int'}
    }

    def __init__(self, naptan_id=None, platform_name=None, indicator=None, stop_letter=None,
                 modes=None, ics_code=None, sms_code=None, stop_type=None, station_naptan=None, 
                 accessibility_summary=None, hub_naptan_code=None, lines=None, line_group=None,
                 line_mode_groups=None, full_name=None, naptan_mode=None, status=None,
                 id=None, url=None, common_name=None, distance=None, place_type=None,
                 additional_properties=None, children=None, children_urls=None,
                 lat=None, lon=None):
        super(StopPoint, self).__init__()
        self.naptan_id = naptan_id
        self.platform_name = platform_name
        self.indicator = indicator
        self.stop_letter = stop_letter
        self.modes = modes
        self.ics_code = ics_code
        self.sms_code = sms_code
        self.stop_type = stop_type
        self.station_naptan = station_naptan
        self.accessibility_summary = accessibility_summary
        self.hub_naptan_code = hub_naptan_code
        self.lines = lines
        self.line_group = line_group
        self.line_mode_groups = line_mode_groups
        self.full_name = full_name
        self.naptan_mode = naptan_mode
        self.status = status
        self.id = id
        self.url = url
        self.common_name = common_name
        self.distance = distance
        self.place_type = place_type
        self.additional_properties = additional_properties
        self.children = children
        self.children_urls = children_urls
        self.lat = lat
        self.lon = lon