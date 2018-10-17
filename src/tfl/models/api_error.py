from msrest.serialization import Model

class ApiError(Model):
    """ApiError.

    :param timestamp_utc:
    :type timestamp_utc: datetime
    :param exception_type:
    :type exception_type: str
    :param http_status_code:
    :type http_status_code: int
    :param http_status:
    :type http_status: str
    :param relative_uri:
    :type relative_uri: str
    :param message:
    :type message: str
    """

    _attribute_map = {
        'timestamp_utc': {'key': 'timestampUtc', 'type': 'iso-8601'},
        'exception_type': {'key': 'exceptionType', 'type': 'str'},
        'http_status_code': {'key': 'httpStatusCode', 'type': 'int'},
        'http_status': {'key': 'httpStatus', 'type': 'str'},
        'relative_uri': {'key': 'relativeUri', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'}
    }

    def __init__(self, timestamp_utc=None, exception_type=None, http_status_code=None, http_status=None,
                 relative_uri=None, message=None):
        super(ApiError, self).__init__()
        self.timestamp_utc = timestamp_utc
        self.exception_type = exception_type
        self.http_status_code = http_status_code
        self.http_status = http_status
        self.relative_uri = relative_uri
        self.message = message