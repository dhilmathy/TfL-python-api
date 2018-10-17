from msrest.serialization import Model

class StopPointsResponse(Model):
    """StopPointsResponse.

    :param stop_points:
    :type stop_points: list of :class:`StopPoint <models.StopPoint>`
    :param page_size:
    :type page_size: int
    :param total:
    :type total: int
    :param page:
    :type page: int
    """

    _attributes_map = {
        'stop_points': { 'key': 'stopPoints', 'type': '[StopPoint]'},
        'page_size': { 'key': 'pageSize', 'type': 'int'},
        'total': { 'key': 'total', 'type': 'int'},
        'page': { 'key': 'page', 'type': 'int'}
    }

    def __init__(self, stop_points=None, page_size=None, total=None, page=None):
        super(StopPointsResponse, self).__init__()
        self.stop_points = stop_points
        self.page_size = page_size
        self.total = total
        self.page = page