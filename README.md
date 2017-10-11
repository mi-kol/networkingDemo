# INFO350 Networking Demonstration

This repository, at completion, should hold all the files necessary to hold a successful networking demonstration that demonstrates how packets work in a closed environment. My setup has 3 raspberry pi's essentially out of the box, in order to cut down on ambient packets that aren't being actively sent by these python scripts. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

To get this up and running, you're gonna need
* [ChatterBot](https://github.com/gunthercox/ChatterBot) - The chatterbot library used. Machine Learning.
* python-dev, python3-dev, python 2.7, python 3.5
* Some computers, and a wired router to set up an enclosed network.

### Installing

Designate one of your hosts as the "Host" for all the programs. At this point in the project (10/7/2017), you're gonna want to run whatever python server seems to meet your needs. Note, this host machine can also be a client if necessary, or if you just want to mess around and see what happens.

Launch client programs on the other devices. Run throughsniffer.py to observe the packets running back and forth, or just mess with the client programs. It's really up to you and what you want to see.

## Deployment

Deploying this? Questionable. Note that we're using Python 2.7 and 3.5, so when deploying make sure to use the right version of Python for each program. As the project progresses, I'll try to stick to Python 2.7 more.

## Goals 

At the end of this project, I hope to have a much better understanding about networking, specifically at the application layer with sockets. Here's the hopeful programs before testing it on Friday.

- [x] packet sniffer
- [x] simple server client communication
- [ ] markov chain inspired packet bouncer
- [ ] chatbot interaction
- [ ] fun packet injector
- [ ] packet fishtank
- [ ] packet around the world (tracking)
- [ ] battleship?
- [ ] chatroom with in-room messages about how packets are moving around the system

## Authors

* **Mikol Aspinwall** - *Initial work* - [mi-kol](https://github.com/mi-kol)

## Acknowledgments

* Packet Sniffer logic came from http://www.binarytides.com/python-packet-sniffer-code-linux/
