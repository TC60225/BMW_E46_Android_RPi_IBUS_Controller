import logging


# from controllers.bmw.e46 import E46Controller
from controllers.bmw.MINIR5x import MINIR5xController


LOGGER = logging.getLogger(__name__)


class ControllerFactory(object):
    """Factory class to instantiate controllers provided the type."""

    @staticmethod
    def create(controller_type):
        # if controller_type == 'bmw-e46':
        #     return E46Controller()
        # el
        if controller_type == 'R50' or controller_type == 'R52' or controller_type == 'R53':
            return MINIR5xController()

        LOGGER.error('controller not supported - %r', controller_type)
