#!/usr/bin/python

# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import Adafruit_DHT

# Sensor should be set to Adafruit_DHT.DHT11,
# Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.
sensor = Adafruit_DHT.AM2302

# Example using a Beaglebone Black with DHT sensor
# connected to pin P8_11.
#pin = 'P8_11'

# Example using a Raspberry Pi with DHT sensor
# connected to pin 23.
pin = 4

# Keen.io variables
# KEEN_PROJECT_ID='5550ccdb96773d6aecb9a4c7'
# KEEN_WRITE_KEY='b346371fc85d4e635f41ac68bf8b2566e511896da7f7745cadffbc909d81e7a031c72f5f55dc9f22fb31d160f59c5cad24f002b539575ccc451383bcd17c512e30eab07838fa99a812e9c39cc3f94366a5c40d918b24cedb3eaf9b8bd416b79f3a7942a3dd1238481ef8e7575936371a'
# KEEN_READ_KEY='ababf08c6b830f0803a3aed45fadf6db0535c109851f167ca64e1929f39a23141d27fabd71eb6d97b597fbd47ef9c01cd6cd24efb880b27dcdab16224635074c38d3f74a6803005728e374e6703122035bd63dd933734a2584c724e0066be6637b3a6c057a2e32bfbba91c49e7faca3f'
# KEEN_MASTER_KEY='2494B44E02BF223732CC2B38062668D9'

import keen
keen.project_id = "5550ccdb96773d6aecb9a4c7"
keen.write_key = "b346371fc85d4e635f41ac68bf8b2566e511896da7f7745cadffbc909d81e7a031c72f5f55dc9f22fb31d160f59c5cad24f002b539575ccc451383bcd17c512e30eab07838fa99a812e9c39cc3f94366a5c40d918b24cedb3eaf9b8bd416b79f3a7942a3dd1238481ef8e7575936371a"
keen.read_key = "ababf08c6b830f0803a3aed45fadf6db0535c109851f167ca64e1929f39a23141d27fabd71eb6d97b597fbd47ef9c01cd6cd24efb880b27dcdab16224635074c38d3f74a6803005728e374e6703122035bd63dd933734a2584c724e0066be6637b3a6c057a2e32bfbba91c49e7faca3f"
keen.master_key = "2494B44E02BF223732CC2B38062668D9"


# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

# Note that sometimes you won't get a reading and
# the results will be null (because Linux can't
# guarantee the timing of calls to read the sensor).  
# If this happens try again!
if humidity is not None and temperature is not None:
	print 'Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity)
else:
	print 'Failed to get reading. Try again!'

#send to keen.io
keen.add_event("temps", {
	"temperature": temperature,
	"humidity": humidity
})
