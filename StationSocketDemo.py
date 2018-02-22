from socketIO_client import SocketIO, LoggingNamespace

def on_connect():
    # suprisingly connect doesn't work but the rest of it works perfectly with django
    print('connect success')
def on_lel(*args):
    print('lel called',args)
sio = SocketIO('localhost', 8000, LoggingNamespace)
sio.emit('my event',{'data':'x'}, on_lel)
