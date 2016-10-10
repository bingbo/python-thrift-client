#!/usr/bin/python
# -*- coding: utf-8 -*- 

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

from hbase import Hbase
from hbase.ttypes import *

transport = TSocket.TSocket('140.205.176.165', 9090);
transport = TTransport.TBufferedTransport(transport)
protocol = TBinaryProtocol.TBinaryProtocol(transport);

client = Hbase.Client(protocol)
transport.open()

tables = client.getTableNames()
print tables

client.checkAndPut('spacc_merge','rowkey:xxxxx','columns:usid:log','value:data')
