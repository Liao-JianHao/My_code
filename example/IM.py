import socketio
import eventlet

# 猴子补丁
eventlet.monkey_patch()  # 携程切换

# 构建socketio服务器
sio = socketio.Server(async_mode="eventlet")

# 获取app对象，给携程调用
app = socketio.Middleware(sio)

SOCKET_ADDRESS = ('', 8000)
socket = eventlet.listen(SOCKET_ADDRESS)
eventlet.wsgi.server(socket, app)




















