from realtime_channel import bus


bus.targetClients = ["e5wgwetdUzs"]


def reply_handler(message):
    print(message)

bus.send("test", "ap", None, reply_handler)

