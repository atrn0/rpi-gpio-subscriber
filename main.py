import datetime
import random
import ssl
import time

from iotcore.client import Client


def main():
    # constants
    project_id = "aratasato"
    device_id = "rpiz-garage"
    registry_id = "rpi-garage"
    region = "asia-east1"
    algorithm = "RS256"
    private_key_file = "/Users/ataran/workspace/rpi-gpio-subscriber/key/rsa_private.pem"
    mqtt_bridge_hostname = "mqtt.googleapis.com"
    mqtt_bridge_port = 8883
    ca_certs = "/Users/ataran/workspace/rpi-gpio-subscriber/iotcore/roots.pem"

    client = Client(project_id, region, registry_id, device_id, private_key_file, algorithm, ca_certs,
                    mqtt_bridge_hostname,
                    mqtt_bridge_port)
    # Connect to the Google MQTT bridge.
    client.connect()


if __name__ == '__main__':
    main()
