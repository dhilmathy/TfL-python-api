from msrest.serialization import Model

class AdditionalProperties(Model):
    _attribute_map = {
        'category': {'key': 'category', 'type': 'str'},
        'key': {'key': 'key', 'type': 'str'},
        'source_system_key': {'key': 'sourceSystemKey', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'},
        'modified': {'key': 'modified', 'type': 'str'}
    }
    
    def __init__(self, category=None, key=None, source_system_key=None, value=None, modified=None):
        super(AdditionalProperties, self).__init__()
        self.category = category
        self.key = key
        self.source_system_key = source_system_key
        self.value = value
        self.modified = modified