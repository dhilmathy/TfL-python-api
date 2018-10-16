from msrest.serialization import Model

class LineGroup(Model):
    """LineGroup.

    :param naptan_id_reference:
    :type naptan_id_reference: str
    :param station_atco_code:
    :type station_atco_code: str
    :param line_identifier:
    :type line_identifier: list of str
    """

    _attribute_map = {
        'naptan_id_reference': {'key': 'naptanIdReference', 'type': 'str'},
        'station_atco_code': {'key': 'stationActoCode', 'type': 'str'},
        'line_identifier': {'key': 'lineIdentifier', 'type': '[str]'}
    }

    def __init__(self, naptan_id_reference=None, station_atco_code=None, line_identifier=None):
        super(LineGroup, self).__init__()
        self.naptan_id_reference = naptan_id_reference
        self.station_atco_code = station_atco_code
        self.line_identifier = line_identifier