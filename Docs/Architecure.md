# Architecture
Presentation of the architectural design of the implemented messaging system. 

### Project description
The goal of this project is to build a python application with a messaging system based on the publish-subscribe messaging pattern, allowing multiple processes to exchange objects.

The main elements we have defined are: 
- **Publishers:** objects that publish messages (objects) to **one or many** certain topic.
- **Subscribers:** objects that subscribe to **one or many** topics, hence is able to get messages published on that specific topic.
- **PubSubs:** objects that are publishers and subscribers at the same time.
- **Topics:** objects allowing publishers to publish messages and appropriate subscribers to retrieve this messages.
- **Messages:** objects that can be published and retrieved in this messaging system.

### Constraints 
#### Publishers, Subscribers and PubSubs
###### Subscribers 
We settled that a subscriber is responsible for retrieving messages. It receives notification when a message is published on a subscribed topic, but it decides when to retrieve the message and process it.   
Subscriber can subscribe to one or many topics. \
Subscriber can subscribe to one or many types of messages of a topic. \
Subscriber can subscribe/unsubscribe on runtime.
###### Publishers 
Publisher can publish to one or many topics. \
Publisher MUST not be concerned by subscribers.
#### Topics at the core of communication
Publishers, Subscribers and PubSubs can run on different independent processes and on the same process as well. They MUST have the same behavior either way. 

As topics controls the communications between them, they are responsible for the management of the multiprocessing or non-multiprocessing behaviors.

#### Multiprocessing elements
First lets say that it seems best that our implementation of the Publisher-Subscriber pattern is not responsible for the multi-processes creation. 
Because the logic of processes depends on a global application needs which we SHOULDN'T depend on. 

Nevertheless, inter-processes communication (Ipc) requires data to be shared between processes. 

*WHO* : As topics are at the core of communication, they MUST be responsible for handling this shared data between processes.

*HOW* : Python offers three possible ways for shared data, **Pipes**, **Queues** and **Shared states**.
We identify two types of multiprocessing : 
1. Same task for multiple independent datasets. \
Ex: with object classification on a image, we can run multiple processes each one will classify one or many images independently.
2. Different independent tasks. \
Ex: motion detection and object classification are two independent tasks.

- *Queues* suits better the first use case. Because messages when retrieved are removed from a queue. Hence, many subscribers cannot get the same message without a duplication mechanism which needs to keep track of when the subscribers have processed the message. Moreover, queues are slower than Pipes.
- *Pipes* are fast, and allows the topic to push messages to each subscriber through its on connection end. Downside is we need to manage pipe connections for each subscriber.
- *Shared states* are depreciated, but allows sharing same objects through proxies. 

*WHAT* : Using pipes to allow communication between topics and subscribers, requires sharing pipe connection ends between them.

In conclusion, we use **Shared states** to allow topics to get and use subscribers **Pipes** connection ends.

For the implementation of this we define: 
- **SharedData:** objects representing the shared state across the processes.
- **PubSubManager:** child objects of multiprocessing.manager.SyncManager, which allow us to register the types (classes) that we can then share across our processes.

#### Processors
Finally, we define **Processors** objects which will process messages, and do something with them.  

## Class diagram
Here's a scheme of the architecture. 

![class_diagram](https://user-images.githubusercontent.com/26309004/169176159-39fe7472-f81f-4aca-bc41-8600e47be69e.png)
