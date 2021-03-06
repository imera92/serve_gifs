import logging
import glob
import sys
sys.path.append("gen-py")
sys.path.insert(0, glob.glob('../thrift-0.11.0/lib/py/build/lib*')[0])
from topgifs import TopGifsService
from src.DbInterface import DbInterface
from src.Gif import Gif
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
import pickle as cPickle

class FetchGifHandler:
    def __init__(self):
        self.log = {}

    def fetchRedisGifs(self):
        dbi = DbInterface()
        print("[Server] Handling client request")
        print("[Server] Creating Gif set")
        result_set = dbi.getRedisGifs().decode('utf-8', 'ignore')
        return result_set

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    handler = FetchGifHandler()
    proc = TopGifsService.Processor(handler)
    trans_svr = TSocket.TServerSocket(port=9090)
    trans_fac = TTransport.TBufferedTransportFactory()
    proto_fac = TBinaryProtocol.TBinaryProtocolFactory()
    server = TServer.TSimpleServer(proc, trans_svr, trans_fac, proto_fac)
    print('Starting the server...')
    server.serve()
