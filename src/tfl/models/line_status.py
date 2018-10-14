from msrest.serialization import Model

class LineStatus(Model):
    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'line_id': {'key': 'lineId', 'type': 'str'},
        'status_severity': {'key': 'statusSeverity', 'type': 'int'},
        'status_severity_description': {'key': 'statusSeverityDescription', 'type': 'str'},
        'reason': {'key': 'reason', 'type': 'str'},
        'created': {'key': 'created', 'type': 'iso-8601'},
        'modified': {'key': 'modified', 'type': 'iso-8601'},
        'validity_periods': {'key': 'validityPeriods', 'type': '[ValidityPeriod]'},
        'disruption': {'key': 'disruption', 'type': '[Disruption]'}
    }

    def __init__(self, id=None, line_id=None, status_severity=None, status_severity_description=None, 
                 reason=None, created=None, modified=None, validity_periods=None, disruption=None):
        super(LineStatus, self).__init__()
        self.id = id
        self.line_id = line_id
        self.status_severity = status_severity
        self.status_severity_description = status_severity_description
        self.reason = reason
        self.created = created
        self.modified = modified
        self.validity_periods = validity_periods
        self.disruption = disruption