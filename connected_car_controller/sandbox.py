import logging
import sys
import argparse

from interfaces.ibus import IBUSInterface
from interfaces.ibus import IBUSPacket
from interfaces.ibuslogger import IBusLoggerInterface

if __name__ == "__main__":
    # setup logging
    log_format = '%(asctime)s [%(levelname)s] [%(filename)s] [%(lineno)s] %(message)s'
    logging.basicConfig(level=logging.DEBUG, format=log_format)

    logging.info('Sandbox')

    log = IBusLoggerInterface(None)
    bus = IBUSInterface(None)
    log.connect()
    packets = bus.receive(bytes.fromhex('3b0580410601f8800aff24060031393420206b3b0580410301fd5b06808340009c82800aff24030031362e35206e3b0580410401fa800aff24040032322e30206b3b0580410501fb800aff24050032322e30206a8005bf180000223b0580410a01f4800aff24'))
    log.send(packets)
    # bus.receive(bytes.fromhex('0a0032372e3520653b0580410901f7800aff2409003020202020683b0580410701f9800aff2407003020202020665b04008b04d00004bf8c02353b0580410e01f0800aff240e0030202020206f'))
    # bus.receive(bytes.fromhex('d007bf5b00000000335b06808340009c828007bf5cff3fff005b8005bf18000022'))
    # bus.receive(bytes.fromhex('5b04008b04d00004bf8c0235'))
