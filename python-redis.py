# coding=utf-8
# import redis
# r=redis.StrictRedis(host='127.0.0.1',port=6379)
# r.set('foo','bar')
# print r.get('foo')

from bottle import request, Bottle, abort
from gevent.pywsgi import WSGIServer
from geventwebsocket.handler import WebSocketHandler
from geventwebsocket import WebSocketError
app = Bottle()
@app.route('/websocket')
def handle_websocket():
    wsock = request.environ.get('wsgi.websocket')
    if not wsock:
        abort(400, 'Expected WebSocket request.')
    while True:
        try:
            message = wsock.receive()
            print "已连接上"
            wsock.send('{"geometry":{"y":39.452906000,"x":-77.423663000,"z":115.3,"spatialReference":{"wkid":4326}},"attributes":{"trackId":1,"time":"2011-09-25T18:18:41Z"}}')
        except WebSocketError:
            break

server = WSGIServer(("localhost", 8888), app,handler_class=WebSocketHandler)
server.serve_forever()
