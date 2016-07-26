"""
"""

import logging


class BaseData(object):
    """
    """

    def __init__(self, api, data):
        """
        """
        self.logger = logging.getLogger(__name__)
        self.api = api
        self.data = data
