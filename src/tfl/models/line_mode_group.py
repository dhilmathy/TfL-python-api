from msrest.serialization import Model

class LineModeGroup(Model):
    _attribute_map = {
        'mode_name': {'key': 'modeName', 'type': 'str'},
        'line_identifier': {'key': 'lineIdentifier', 'type': '[str]'}
    }

    def __init__(self, mode_name=None, line_identifier=None):
        super(LineModeGroup, self).__init__()
        self.mode_name = mode_name
        self.line_identifier = line_identifier
