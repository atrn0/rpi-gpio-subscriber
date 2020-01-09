import json

import paho.mqtt.client as mqtt

from gpio.cmd_handler import handle_cmd
from iotcore import client


def on_connect(unused_client, unused_userdata, unused_flags, rc):
    """Callback for when a device connects."""
    print('on_connect', mqtt.connack_string(rc))

    # After a successful connect, reset backoff time and stop backing off.
    client.should_backoff = False
    client.minimum_backoff_time = 1


def on_disconnect(unused_client, unused_userdata, rc):
    """Paho callback for when a device disconnects."""
    print('on_disconnect', __error_str(rc))

    # Since a disconnect occurred, the next loop iteration will wait with
    # exponential backoff.
    client.should_backoff = True


def on_publish(unused_client, unused_userdata, unused_mid):
    """Paho callback when a message is sent to the broker."""
    print('on_publish')


def on_message(unused_client, unused_userdata, message):
    """Callback when the device receives a message on a subscription."""
    payload = str(message.payload.decode('utf-8'))
    print('Received message \'{}\' on topic \'{}\' with Qos {}'.format(
        payload, message.topic, str(message.qos)))
    data = json.loads(payload)
    handle_cmd(data['cmd'], data['pin'])


def __error_str(rc):
    """Convert a Paho error to a human readable string."""
    return '{}: {}'.format(rc, mqtt.error_string(rc))
