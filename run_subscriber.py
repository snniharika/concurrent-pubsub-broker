from client.subscriber import Subscriber

if __name__ == "__main__":
    sub = Subscriber()
    sub.start()

    while True:
        topic = input("Subscribe: ")
        sub.subscribe(topic)
