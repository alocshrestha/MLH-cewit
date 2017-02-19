import plotly.plotly as py
import plotly.tools as tools
import datetime
import time
from plotly.graph_objs import *
import PCF8591 as ADC
import RPi.GPIO as GPIO
from picamera import PiCamera
import send_email as se

GPIO.setmode(GPIO.BCM)
ADC.setup(0x48)

tools.set_credentials_file(username='', api_key='')

stream_token = ''

trace = Scatter(
    x = [],
    y = [],
    stream=dict(token=stream_token, maxpoints = 200)
)

layout = Layout(title = 'Streaming Voice Data')
fig = Figure(data=[trace])
print py.plot(fig, filename = 'RPI-VOICE-VALUES')

sensor_pin = 0

#initialize the ploty streaming object
stream = py.Stream(stream_token)
stream.open()
camera = PiCamera()
sent = False
while True:
    sensor_data = ADC.read(0)
    print sensor_data
    if sensor_data > 20 and not sent:        
        camera.rotation = 180
        camera.start_preview()
        time.sleep(2)
        camera.capture('baby.jpg')
        camera.stop_preview()
        se.sendmail()
        sent = True
        
    stream.write({'x': datetime.datetime.now(), 'y': sensor_data})
    time.sleep(0.1)

#data = Data([trace])
#py.iplot(data, filename = 'test1', sharing = 'public')
