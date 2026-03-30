from client.publisher import Publisher

if __name__ == "__main__":
    pub = Publisher()
    while True:
        topic = input("Topic: ")
        msg = input("Message: ")
        pub.publish(topic, msg)
