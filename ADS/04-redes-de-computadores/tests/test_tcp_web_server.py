import socket,sys,time
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]))
import pytest
from tcp_web_server import TCPWebServer,parse_request,ProtocolError
@pytest.fixture
def server():
 s=TCPWebServer(port=0).start(); yield s; s.stop()
def raw(server,request):
 with socket.create_connection((server.host,server.port),timeout=2) as c:
  c.sendall(request); return c.recv(8192)
def test_parse_http_request():
 r=parse_request(b'GET /healthz HTTP/1.1\r\nHost: localhost\r\n\r\n'); assert r.method=='GET' and r.target=='/healthz'
def test_parse_rejects_malformed():
 with pytest.raises(ProtocolError): parse_request(b'GET /healthz\r\n\r\n')
def test_health_route(server):
 out=raw(server,b'GET /healthz HTTP/1.1\r\nHost: localhost\r\n\r\n'); assert out.startswith(b'HTTP/1.1 200') and b'ok\n' in out
def test_info_route(server):
 out=raw(server,b'GET /info HTTP/1.1\r\nHost: localhost\r\n\r\n'); assert b'"transport": "TCP"' in out
def test_not_found_and_method_contract(server):
 assert raw(server,b'GET /missing HTTP/1.1\r\nHost: x\r\n\r\n').startswith(b'HTTP/1.1 404')
 assert raw(server,b'POST /healthz HTTP/1.1\r\nHost: x\r\n\r\n').startswith(b'HTTP/1.1 405')
def test_head_has_no_body(server):
 out=raw(server,b'HEAD /healthz HTTP/1.1\r\nHost: x\r\n\r\n'); assert out.startswith(b'HTTP/1.1 200') and out.endswith(b'\r\n\r\n')
def test_concurrent_connections(server):
 results=[]
 import concurrent.futures
 with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
  results=list(pool.map(lambda _: raw(server,b'GET /healthz HTTP/1.1\r\nHost: x\r\n\r\n'),range(20)))
 assert all(x.startswith(b'HTTP/1.1 200') for x in results); assert server.metrics['completed']>=20
