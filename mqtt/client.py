import datetime
import ssl

import jwt
import paho.mqtt.client as mqtt

from mqtt import handler


def create_jwt(project_id, private_key_file, algorithm):
    """Creates a JWT (https://jwt.io) to establish an MQTT connection.
        Args:
         project_id: The cloud project ID this device belongs to
         private_key_file: A path to a file containing either an RSA256 or
                 ES256 private key.
         algorithm: The encryption algorithm to use. Either 'RS256' or 'ES256'
        Returns:
            A JWT generated from the given project_id and private key, which
            expires in 20 minutes. After 20 minutes, your client will be
            disconnected, and a new JWT will have to be generated.
        Raises:
            ValueError: If the private_key_file does not contain a known key.
        """

    token = {
        # The time that the token was issued at
        'iat': datetime.datetime.utcnow(),
        # The time the token expires.
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
        # The audience field should always be set to the GCP project id.
        'aud': project_id
    }

    # Read the private key file.
    with open(private_key_file, 'r') as f:
        private_key = f.read()

    print('Creating JWT using {} from private key file {}'.format(
        algorithm, private_key_file))

    return jwt.encode(token, private_key, algorithm=algorithm)


class Client:
    def __init__(self, project_id, cloud_region, registry_id, device_id, private_key_file,
                 algorithm, ca_certs, mqtt_bridge_hostname, mqtt_bridge_port):
        self.MAXIMUM_BACKOFF_TIME = 32
        self.PROJECT_ID = project_id
        self.CLOUD_REGION = cloud_region
        self.REGISTRY_ID = registry_id
        self.DEVICE_ID = device_id

        self.should_backoff = False
        self.minimum_backoff_time = 1

        """Create our MQTT client. The client_id is a unique string that identifies
        this device. For Google Cloud IoT Core, it must be in the format below."""
        self.client = mqtt.Client(client_id=self.__get_client_id())

        # With Google Cloud IoT Core, the username field is ignored, and the
        # password field is used to transmit a JWT to authorize the device.
        self.client.username_pw_set(username='unused',
                                    password=create_jwt(
                                        project_id, private_key_file, algorithm))
        # Enable SSL/TLS support.
        self.client.tls_set(ca_certs=ca_certs, tls_version=ssl.PROTOCOL_TLSv1_2)

        # Register message callbacks. https://eclipse.org/paho/clients/python/docs/
        # describes additional callbacks that Paho supports. In this example, the
        # callbacks just print to standard out.
        self.__register_handler()

    def __get_client_id(self):
        return 'projects/{}/locations/{}/registries/{}/devices/{}'.format(
            self.PROJECT_ID, self.CLOUD_REGION, self.REGISTRY_ID, self.DEVICE_ID)

    def __register_handler(self):
        self.client.on_connect = handler.on_connect
        self.client.on_publish = handler.on_publish
        self.client.on_disconnect = handler.on_disconnect
        self.client.on_message = handler.on_message
