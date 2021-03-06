import os.path
import unittest

try:
    from unittest.mock import patch
except ImportError:
    from mock import patch
from streamlink import Streamlink
from streamlink.api import streams

PluginPath = os.path.join(os.path.dirname(__file__), "plugins")


def get_session():
    s = Streamlink()
    s.load_plugins(PluginPath)
    return s


class TestStreamlinkAPI(unittest.TestCase):
    @patch('streamlink.api.Streamlink', side_effect=get_session)
    def test_find_test_plugin(self, session):
        self.assertTrue(
            "rtmp" in streams("test.se")
        )

    @patch('streamlink.api.Streamlink', side_effect=get_session)
    def test_no_streams_exception(self, session):
        self.assertEqual({}, streams("test.se/NoStreamsError"))

    @patch('streamlink.api.Streamlink', side_effect=get_session)
    def test_no_streams(self, session):
        self.assertEqual({}, streams("test.se/empty"))
