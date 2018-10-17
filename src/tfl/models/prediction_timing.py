from msrest.serialization import Model

class PredictionTiming(Model):
    """PredictionTiming.

    :param countdown_server_adjustment:
    :type countdown_server_adjustment: str
    :param source:
    :type source: datetime
    :param insert:
    :type insert: datetime
    :param read:
    :type read: datetime
    :param sent:
    :type sent: datetime
    :param received:
    :type received: datetime
    """

    _attribute_map = {
        'countdown_server_adjustment': {'key': 'countdownServerAdjustment', 'type': 'str'},
        'source': {'key': 'source', 'type': 'iso-8601'},
        'insert': {'key': 'insert', 'type': 'iso-8601'},
        'read': {'key': 'read', 'type': 'iso-8601'},
        'sent': {'key': 'sent', 'type': 'iso-8601'},
        'received': {'key': 'received', 'type': 'iso-8601'}
    }

    def __init__(self, countdown_server_adjustment=None, source=None, insert=None, read=None, sent=None, received=None):
        super(PredictionTiming, self).__init__()
        self.countdown_server_adjustment = countdown_server_adjustment
        self.source = source
        self.insert = insert
        self.read = read
        self.sent = sent
        self.received = received