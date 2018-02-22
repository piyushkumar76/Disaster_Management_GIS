# installed
async_mode = None

import os

from django.http import HttpResponse
import socketio

basedir = os.path.dirname(os.path.realpath(__file__))
sio = socketio.Server(async_mode=async_mode)
thread = None


def index(request):
    global thread
    if thread is None:
        thread = sio.start_background_task(background_thread)
    return HttpResponse(open(os.path.join(basedir, 'static/index.html')))


def background_thread():
    """Example of how to send server generated events to clients."""
    count = 0
    while True:
        sio.sleep(10)
        count += 1
        sio.emit('my response', {'data': 'Server generated event'},
                 )


@sio.on('my event')
def test_message(sid, message):
    print(message)
    sio.enter_room(sid,sid)
    sio.emit('my response', {'data': message['data']}, room=sid)

@sio.on('my broadcast event')
def test_broadcast_message(sid, message):
    print('broadcasted ',sid)
    sio.emit('my response', {'data': message['data']})

@sio.on('join')
def join(sid, message):
    sio.enter_room(sid, message['room'])
    sio.emit('my response', {'data': 'Entered room: ' + message['room']},
             room=sid)


@sio.on('leave')
def leave(sid, message):
    sio.leave_room(sid, message['room'])
    sio.emit('my response', {'data': 'Left room: ' + message['room']},
             room=sid)


@sio.on('close room')
def close(sid, message):
    sio.emit('my response',
             {'data': 'Room ' + message['room'] + ' is closing.'},
             room=message['room'])
    sio.close_room(message['room'])


@sio.on('my room event')
def send_room_message(sid, message):
    sio.emit('my response', {'data': message['data']}, room=message['room'],
             )


@sio.on('disconnect request')
def disconnect_request(sid):
    sio.disconnect(sid)


@sio.on('connect')
def test_connect(sid, environ):
    print('Client Connected')
    sio.emit('my response', {'data': 'Connected', 'count': 0}, room=sid,
             )

@sio.on('disconnect')
def test_disconnect(sid):
    print('Client disconnected')
