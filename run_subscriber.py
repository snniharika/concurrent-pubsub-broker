from client.subscriber import Subscriber


sub = Subscriber()
sub.start()

while True:
    cmd = input("Enter (sub/unsub): ")
    topic = input("Topic: ")

    if cmd == "sub":
        sub.subscribe(topic)
    elif cmd == "unsub":
        sub.unsubscribe(topic) 
