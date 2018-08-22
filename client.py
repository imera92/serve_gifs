import sys
import glob
sys.path.append('gen-py')
sys.path.insert(0, glob.glob('../thrift-0.11.0/lib/py/build/lib*')[0])
from topgifs import TopGifsService
from src.Gif import Gif
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

def main():
    # Make socket
    transport = TSocket.TSocket('localhost', 9090)

    # Buffering is critical. Raw sockets are very slow
    transport = TTransport.TBufferedTransport(transport)

    # Wrap in a protocol
    protocol = TBinaryProtocol.TBinaryProtocol(transport)

    # Create a client to use the protocol encoder
    client = TopGifsService.Client(protocol)

    # Connect!
    transport.open()

    result = client.fetchAllGifs()
    print(result)

if __name__ == '__main__':
    try:
        main()
    except Thrift.TException as tx:
        print("There was an error")
        print('%s' % tx.message)
