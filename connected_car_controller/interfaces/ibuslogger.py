"""
This module contains the implementation for IBusLoggerInterface.
"""
import json
import threading
import logging
import csv

from interfaces.base import BaseInterface


LOGGER = logging.getLogger(__name__)


class IBusLoggerInterface(BaseInterface):
    """The IBusLogger interface definition for communication with wireless client devices."""

    __interface_name__ = 'IBusLogger'

    def __init__(self, controller):
        """
        Initializes a IBusLogger service that may be consumed by a remote client.

        Arguments
        ---------
            controller : controllers.base.BaseController
                the parent controller that is instantiated this interface

        """
        super(IBusLoggerInterface, self).__init__()
        self.controller = controller
        self.logfile = self.get_setting('logfile')
        self.file = None
        self.CSV = None
        self.thread = None

    def connect(self):
        """Creates a new thread that listens for an incoming IBusLogger RFCOMM connection."""
        LOGGER.info('connect IBusLogger interface...')

        # line buffered file
        self.file = open(self.logfile, 'w', newline='', buffering=1)
        self.CSV = csv.DictWriter(self.file, fieldnames=['timestamp', 'source_id', 'destination_id', 'data', 'length'])
        self.CSV.writeheader()

        self.thread = threading.Thread(target=self.PollFolderForMessages)
        self.thread.daemon = True
        self.thread.start()

    def PollFolderForMessages(self):

        self.state = self.__states__.STATE_CONNECTED
        # start listening for data
        self.consume_bus()

    def disconnect(self):
        """
        Closes IBusLogger connection and resets handle
        """
        LOGGER.info('disconnect IBusLogger interface...')
        self.state = self.__states__.STATE_DISCONNECTING
        self.file.close()

        self.state = self.__states__.STATE_READY

    def send(self, data):
        """
        "Sends" data  to the log file

        Arguments
        ---------
            data : basestring
                the data to be sent via this interface

        """
        if self.state != self.__states__.STATE_CONNECTED:
            LOGGER.error('error: send() was called but state is not connected')
            return False

        try:
            LOGGER.info('logging IBUSPacket(s)...')
            for packet in data:
                self.CSV.writerow(packet.as_serializable_dict())

        except Exception:
            # socket was closed, graceful restart
            LOGGER.exception('IBusLogger send exception')
            self.reconnect()

    def receive(self, data):
        """
        "Receives" data from a file to be sent to the iBus

        Arguments
        ---------
            data : basestring
                the data received from the IBusLogger file

        """
        try:
            packet = json.loads(data.decode('utf-8'))
            LOGGER.info('received packet via IBusLogger: %r', packet['data'])

            # invoke bound method (if set)
            if self.receive_hook and hasattr(self.receive_hook, '__call__'):
                self.receive_hook(packet['data'])

        except Exception as exception:
            LOGGER.exception('error: %r', exception)

    def consume_bus(self):
        """
        # TODO could poll a folder to pickup messages to be sent and call receive
        """
        try:
            # self.receive()
            pass
        except Exception as exception:
            pass