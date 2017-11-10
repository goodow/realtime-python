import pyrebase

_config = {
    "apiKey": "AIzaSyBvasV2WNLiFR6CR_m-_PbIDFEArYDtWpA",
    "authDomain": "tencent-live.firebaseapp.com",
    "databaseURL": "https://tencent-live.firebaseio.com",
    "storageBucket": ""
}

_db = pyrebase.initialize_app(_config).database()

targetClients = []


def send(topic, payload, options, callback):
    client_id = targetClients[0]
    msg = {
        "topic": topic,
        "payload": payload,
        "options": options,
    }
    busRef = _db.child("bus")
    queueRef = busRef.child("queue").child(client_id)
    json = queueRef.push(msg)
    if callback is None:
        return

    def stream_handler(message):
        if message["data"] is None:
            return

        # my_stream.close()
        replyMsg = message["data"]
        callback(replyMsg)

    path = "bus/queue/" + client_id + "/" + json["name"] + "/reply"
    my_stream = _db.child(path).stream(stream_handler)
    return None
