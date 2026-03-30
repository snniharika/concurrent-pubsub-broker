# Concurrent Publish–Subscribe Broker with SSL/TLS

## Overview

This project implements a secure and concurrent Publish–Subscribe messaging system using TCP sockets in Python. The system enables multiple publishers and subscribers to communicate through a central broker, supporting **topic-based message routing**, **real-time delivery**, and **performance evaluation**.

---

## Features

* Topic-based publish–subscribe communication
* Support for multiple concurrent clients
* Secure communication using SSL/TLS
* Thread-based concurrency for handling clients
* Custom JSON-based message protocol
* Reliable data transmission using length-prefixed framing
* Performance metrics:

  * Throughput (publisher side)
  * Latency (subscriber side)

---

## System Architecture

The system follows a modular client–server architecture:

* **Publisher**: Sends messages to specific topics
* **Subscriber**: Subscribes to topics and receives messages
* **Broker (Server)**: Manages connections and routes messages
* **Topic Manager**: Maintains topic subscriptions
* **Client Handler**: Handles each client connection concurrently

---

## Project Structure

```
concurrent-pubsub-broker/
│
├── client/
│   ├── client_base.py
│   ├── publisher.py
│   ├── subscriber.py
│   └── ssl_client.py
│
├── common/
│   ├── protocol.py
│   └── utils.py
│
├── server/
│   ├── broker.py
│   ├── client_handler.py
│   ├── topic_manager.py
│   └── ssl_context.py
│
├── run_server.py
├── run_publisher.py
├── run_subscriber.py
└── .gitignore
```

---

## Working Principle

1. The publisher sends messages to the broker with a specified topic.
2. The broker receives the message and identifies all subscribers of that topic.
3. The message is forwarded to the relevant subscribers.
4. Subscribers receive messages in real time and compute latency.

---

## Communication Protocol

* Messages are structured using a custom **JSON-based format**
* Each message includes:

  * Type (PUBLISH, SUBSCRIBE, EVENT)
  * Topic
  * Data
  * Timestamp
* Messages are transmitted using a **length-prefixed framing mechanism** to ensure reliable delivery over TCP

---

## Security

* SSL/TLS is implemented using Python’s `ssl` module
* Server uses a certificate and private key
* Client connections are encrypted to ensure secure communication

---

## Setup Instructions

### 1. Generate SSL Certificates

Run the following command:

```
openssl req -new -x509 -days 365 -nodes -out server.crt -keyout server.key
```

Place the generated files in:

```
certs/server.crt  
certs/server.key
```

---

### 2. Run the Application

Start the server:

```
python run_server.py
```

Start a subscriber:

```
python run_subscriber.py
```

Start a publisher:

```
python run_publisher.py
```

---

## Performance Evaluation

* **Throughput**: Number of messages sent per second by the publisher
* **Latency**: Time difference between message publish and reception at subscriber

---

## Technologies Used

* Python (Socket Programming)
* TCP/IP Networking
* SSL/TLS Security
* Multithreading

---

## Conclusion

This project demonstrates the implementation of a secure, concurrent messaging system using fundamental networking concepts. It highlights the integration of socket programming, synchronization, protocol design, and performance evaluation in a real-world application.
