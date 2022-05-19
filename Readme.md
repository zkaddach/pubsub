# PUBLISH-SUBSCRIBE MESSAGING PATTERN

The goal of this project is to design and implement a messaging system following the Publish-Subscribe pattern.


### PREREQUISITES

You must have the following software installed on your development machine:

* [Python](https://www.python.org/downloads/) - version 3 or above


### SET UP THE APP FROM CODE:

1. In a terminal, navigate to this sample's root directory.

2. Run the following commands:

   - Install libraries:

       `pip3 install requirements.txt`

   - Run application : 

       `python3 main.py`


### SET UP THE APP WITH DOCKER:

1. In a terminal, navigate to this sample's root directory.

2. Run the following commands:

   - Build image:

       `docker build --tag my-tag .`

   - Run container : 

       `docker run -it my-tag`


### RUN SAMPLES

1. Now that the program has started it awaits for your input.

2. Write anything other than 'q' then press enter:

   Dummy messages that have been published to a topic and then retrieved by a subscriber are displayed.

3. Enter 'q' to end program.


### RUN TESTS 

1. In a terminal, navigate to this sample's root directory.

2. Run the following command:

    `mypy .` #python static type check

    `black .` #python code formatter

    `flake8 .` #python code linter

   `python3 -m pytest` #python tests

Enjoy ! 

Check [Architecture](https://github.com/zkaddach/pubsub/blob/master/Docs/Architecture.md) for more details.
