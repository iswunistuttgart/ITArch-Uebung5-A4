from lib import QRScanner
import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
import json

############################################################
# Relevanter Teil fuer die Uebung
# Hier die Geschwindigkeit eintragen von 0 = 0% bis 1 = 100%
# z.B. 0.44 entspricht 44%
pSpeed = 0
Team = 'TEAMNAME' # Hier den Teamnamen als String eintragen
BROKER = ""  # Hier die IP Adresse des Brokers eintragen
PORT = 1883

#Ab hier muss nichts mehr angepassst werden
############################################################

camera = PiCamera()
camera.resolution = (320, 240)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(320, 240))
time.sleep(0.1)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
pwm = GPIO.PWM(18, 100)
Speed = 0.50 + (0.5 * pSpeed)
if (Speed < 0.5) :
    Speed = 0.5
elif(Speed > 1) :
    Speed = 1
pwm.start(73 * Speed)

qr_last = None


# Create an MQTT client instance
client = mqtt.Client()
# Connect to the broker
client.connect(BROKER, PORT, 60)


for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image = frame.array

    qr = QRScanner.crop_qr_code(image)

    if qr is not None:
        print (QRScanner.read_qr_code(qr))

    if (qr is not None and qr_last is not None):
        if (QRScanner.qr_codes_equal(qr,qr_last)):
            print (QRScanner.read_qr_code(qr))
            QRCode = QRScanner.read_qr_code(qr)
            TOPIC = f'isw/ITArch/pi/'
            MESSAGE = {"QRCode": QRCode, "Speed": pSpeed, "Team": Team}
            client.publish(TOPIC, str(MESSAGE))
            print(f"Published message '{str(MESSAGE)}' to topic '{TOPIC}'.")

    qr_last = qr
    rawCapture.truncate(0)
