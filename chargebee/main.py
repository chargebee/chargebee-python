import os.path

from chargebee.environment import Environment


class ChargeBee(object):

    default_env = None

    verify_ca_certs = True
    ca_cert_path = os.path.join(os.path.dirname(__file__), 'ssl', 'ca-certs.crt')

    @classmethod
    def configure(cls, options):
        cls.default_env = Environment(options)

    @classmethod
    def update_connect_timeout_secs(cls,connect_timeout):
         cls.default_env.connect_timeout = connect_timeout

    @classmethod
    def update_read_timeout_secs(cls,read_timeout):
         cls.default_env.read_timeout = read_timeout
