#!/usr/bin/python2

# written by sqall
# twitter: https://twitter.com/sqall01
# blog: http://blog.h4des.org
# github: https://github.com/sqall01
#
# Licensed under the GNU Public License, version 2.

import os


# this class is a global configuration class that holds 
# values that are needed all over the client
class GlobalData:

	def __init__(self):

		# version of the used client (and protocol)
		self.version = 0.500

		# revision of the used client
		self.rev = 1

		# name of this client
		self.name = "alertR Sensor Client Raspberry Pi"

		# the instance of this client
		self.instance = "sensorClientRaspberryPi"

		# interval in which a ping should be send when 
		# no data was received/send
		self.pingInterval = 20

		# type of this node/client
		self.nodeType = "sensor"

		# path to the configuration file of the client
		self.configFile = os.path.dirname(os.path.abspath(__file__)) \
			+ "/../config/config.xml"

		# instance of the email alerting object
		self.smtpAlert = None

		# this variable holds the object of the server communication
		self.serverComm = None

		# list of all sensors that are managed by this client
		self.sensors = list()

		# Flag that indicates if this node is registered as persistent
		# (0 or 1).
		self.persistent = None