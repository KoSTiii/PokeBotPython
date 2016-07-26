"""
"""

import logging


class BaseData(object):
    """
    """

    def __init__(self, api):
        """
        """
        self.logger = logging.getLogger(__name__)
        self.api = api
