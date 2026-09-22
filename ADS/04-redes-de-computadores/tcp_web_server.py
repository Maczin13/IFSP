"""Servidor HTTP/1.1 didático construído diretamente sobre sockets TCP."""
from __future__ import annotations
import argparse, json, logging, socket, threading, time
from dataclasses import dataclass
from typing import Dict, Tuple

MAX_REQUEST=8192
@dataclass
class Request:
    method:str; target:str; version:str; headers:dict[str,str]; body:bytes=b''
class ProtocolError(ValueError): pass

def parse_request(raw:bytes)->Request:
    if b'\r\n\r\n' not in raw: raise ProtocolError('cabeçalho incompleto')
    head,body=raw.split(b'\r\n\r\n',1); lines=head.decode('iso-8859-1').split('\r\n')
    if not lines or len(lines[0].split())!=3: raise ProtocolError('linha inicial inválida')
    method,target,version=lines[0].split(); headers={}
    for line in lines[1:]:
        if ':' not in line: raise ProtocolError('cabeçalho inválido')
        k,v=line.split(':',1); headers[k.strip().lower()]=v.strip()
    if 'content-length' in headers:
        try: length=int(headers['content-length'])
        except ValueError: raise ProtocolError('content-length inválido')
        if length<0 or length>MAX_REQUEST: raise ProtocolError('corpo excede limite')
        if len(body)<length: raise ProtocolError('corpo incompleto')
        body=body[:length]
    return Request(method,target,version,headers,body)

def response(status:int, body:bytes, headers:dict[str,str]|None=None)->bytes:
    reasons={200:'OK',404:'Not Found',405:'Method Not Allowed',400:'Bad Request',413:'Payload Too Large'}
    h={'Content-Length':str(len(body)),'Content-Type':'text/plain; charset=utf-8','Connection':'close'}; h.update(headers or {})
    start=f'HTTP/1.1 {status} {reasons.get(status,"Error")}\r\n'
    return (start+''.join(f'{k}: {v}\r\n' for k,v in h.items())+'\r\n').encode()+body

class TCPWebServer:
    def __init__(self,host='127.0.0.1',port=0,backlog=16):
        self.host,self.port,self.backlog=host,port,backlog; self.sock=None; self._stop=threading.Event(); self._thread=None; self.log=logging.getLogger('tcp-web')
        self.metrics={'accepted':0,'completed':0,'errors':0,'bytes_in':0,'bytes_out':0}
    def start(self):
        self.sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM); self.sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1); self.sock.bind((self.host,self.port)); self.sock.listen(self.backlog); self.port=self.sock.getsockname()[1]
        self._thread=threading.Thread(target=self._accept_loop,daemon=True); self._thread.start(); return self
    def _accept_loop(self):
        self.sock.settimeout(.2)
        while not self._stop.is_set():
            try: conn,addr=self.sock.accept()
            except socket.timeout: continue
            except OSError: break
            self.metrics['accepted']+=1; threading.Thread(target=self._handle,args=(conn,addr),daemon=True).start()
    def _handle(self,conn,addr):
        began=time.perf_counter()
        try:
            conn.settimeout(2); raw=conn.recv(MAX_REQUEST+1); self.metrics['bytes_in']+=len(raw)
            if len(raw)>MAX_REQUEST: out=response(413,b'payload too large\n')
            else:
                try: req=parse_request(raw); out=self.route(req)
                except ProtocolError as exc: self.metrics['errors']+=1; out=response(400,(str(exc)+'\n').encode())
            conn.sendall(out); self.metrics['bytes_out']+=len(out); self.metrics['completed']+=1
            self.log.info('client=%s method=%s status=%s bytes_in=%d bytes_out=%d duration_ms=%.2f',addr,locals().get('req',Request('?','?','?',{})).method if 'req' in locals() else '?',out.split(b' ',2)[1].decode(),len(raw),len(out),(time.perf_counter()-began)*1000)
        except (OSError,TimeoutError): self.metrics['errors']+=1
        finally: conn.close()
    def route(self,req:Request)->bytes:
        if req.method not in {'GET','HEAD'}: return response(405,b'method not allowed\n',{'Allow':'GET, HEAD'})
        if req.target=='/healthz': body=b'ok\n'
        elif req.target=='/info': body=json.dumps({'service':'tcp-web-lab','transport':'TCP','protocol':'HTTP/1.1'},ensure_ascii=False).encode()+b'\n'
        else: return response(404,b'not found\n')
        if req.method=='HEAD': body=b''
        return response(200,body)
    def stop(self):
        self._stop.set()
        if self.sock:
            try:self.sock.close()
            except OSError:pass
        if self._thread:self._thread.join(timeout=1)

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--host',default='127.0.0.1'); ap.add_argument('--port',type=int,default=8080); ap.add_argument('--backlog',type=int,default=16); a=ap.parse_args()
 logging.basicConfig(level=logging.INFO,format='%(asctime)s %(levelname)s %(message)s')
 server=TCPWebServer(a.host,a.port,a.backlog).start(); print(f'listening={server.host}:{server.port}',flush=True)
 try:
  while True: time.sleep(1)
 except KeyboardInterrupt: server.stop()
if __name__=='__main__': main()
