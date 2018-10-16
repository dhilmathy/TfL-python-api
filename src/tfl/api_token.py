class ApiToken():
    """ApiToken.

    :param str app_id: Application ID from the API credentails
    :param str app_key: Application Key from the API credentails
    """

    def __init__(self, app_id, app_key):
        self.app_id = app_id
        self.app_key = app_key