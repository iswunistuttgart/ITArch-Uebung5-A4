import paho.mqtt.client as mqtt
import json
import requests

# Dieses Skript ist als Ersatz vorgesehen, falls keine Verbindung mit dem Raspberry Pi möglich ist.

# Hier die Geschwindigkeit eintragen von 0 = 0% bis 1 = 100%
# z.B. 0.44 entspricht 44%
pSpeed = 0.1

# Team Information
Team = ""  # Hier den Teamnamen als String eintragen
QRCode = ""  # Hier den Inhalt des QR Codes eintragen

# MQTT Information
BROKER = ""  # Hier die IP Adresse des Brokers eintragen
PORT = 1883

# MQTT Client 
client = mqtt.Client()
client.connect(BROKER, PORT, 60)

# MQTT Message
TOPIC = f'isw/ITArch/'
MESSAGE = {"qrcode": QRCode, "speed": pSpeed, "team": Team}

# MQTT Publish
client.publish(TOPIC, json.dumps(MESSAGE))
print(f"Published message '{str(MESSAGE)}' to topic '{TOPIC}'.")

