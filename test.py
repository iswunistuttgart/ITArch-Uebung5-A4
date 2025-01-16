import paho.mqtt.client as mqtt
import json
import requests

# Dieses Skript ist als Ersatz vorgesehen, falls keine Verbindung mit dem Raspberry Pi möglich ist.

############################################################
# Relevanter Teil fuer die Uebung
# Hier die Geschwindigkeit eintragen von 0 = 0% bis 1 = 100%
# z.B. 0.44 entspricht 44%
pSpeed = 0.1
Team = ""  # Hier den Teamnamen als String eintragen
BROKER = ""  # Hier die IP Adresse des Brokers eintragen
QRCode = ""  # Hier den Inhalt des QR Codes eintragen
PORT = 1883

#Ab hier muss nichts mehr angepassst werden
############################################################

# Create an MQTT client instance
client = mqtt.Client()
# Connect to the broker
client.connect(BROKER, PORT, 60)


TOPIC = f'isw/ITArch/'
MESSAGE = {"qrcode": QRCode, "speed": pSpeed, "team": Team}
client.publish(TOPIC, json.dumps(MESSAGE))
print(f"Published message '{str(MESSAGE)}' to topic '{TOPIC}'.")

