from msrest.serialization import Model

class ValidityPeriod(Model):
    _attribute_map = {
        'from_date': {'key': 'fromDate', 'type': 'iso-8601'},
        'to_date': {'key': 'toDate', 'type': 'iso-8601'},
        'is_now': {'key': 'isNow', 'type': 'bool'}
    }

    def __init__(self, from_date=None, to_date=None, is_now=None):
        super(ValidityPeriod, self).__init__()
        self.from_date = from_date
        self.to_date = to_date
        self.is_now = is_now