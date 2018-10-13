from channels.routing import route
import sys
from django.conf import settings
sys.path.append(settings.BASE_DIR + "/example")
from example.consumers import ws_connect, ws_disconnect

channel_routing = [
    route('websocket.connect', ws_connect),
    route('websocket.disconnect', ws_disconnect),
]
