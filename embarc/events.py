from .app import app, socketio, redis
from flask_socketio import emit

@socketio.on('connect')
def on_connect():
    redis.set('music_server_online', 1)
    print("Connected")

@socketio.on('disconnect')
def on_disconnect():
    redis.set('music_server_online', 0)
    print("Disconnected")

@socketio.on('aaa')
def on_aaa():
    emit('aaa_response')

@socketio.on('playlist')
def on_playlist(playlist):
    redis.set('playlist', playlist)

@socketio.on('pos')
def on_pos(pos):
    redis.set('pos', pos)
