from msrest.serialization import Model

class LineModeGroup(Model):
    """LineModeGroup.

    :param mode_name:
    :type mode_name: str
    :param line_identifier:
    :type line_identifier: list of str
    """

    _attribute_map = {
        'mode_name': {'key': 'modeName', 'type': 'str'},
        'line_identifier': {'key': 'lineIdentifier', 'type': '[str]'}
    }

    def __init__(self, mode_name=None, line_identifier=None):
        super(LineModeGroup, self).__init__()
        self.mode_name = mode_name
        self.line_identifier = line_identifier
