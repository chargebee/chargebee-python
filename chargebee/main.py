import os.path
from contextlib import contextmanager

from chargebee.environment import Environment, MockEnvironment


class ChargeBee(object):

    default_env = None

    verify_ca_certs = True
    ca_cert_path = os.path.join(os.path.dirname(__file__), 'ssl', 'ca-certs.crt')

    @classmethod
    def configure(cls, options):
        cls.default_env = Environment(options)

    @classmethod
    @contextmanager
    def mock(cls, **options):
        """
        Context manager for unit testing environments.
        This changes the default environment, so saves passing custom environments around.

        See MockEnvironment for more details & example usage.
        """
        prev_env = cls.default_env
        try:
            cls.default_env = MockEnvironment(**options)
            yield cls.default_env
        finally:
            cls.default_env = prev_env
