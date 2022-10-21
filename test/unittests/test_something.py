# write your first unittest!
import unittest

from ovos_tts_plugin_mimic3_streaming import Mimic3StreamingTTSPlugin


class TestTTS(unittest.TestCase):
    def test_p239(self):
        path = "/tmp/hello_p239.wav"
        mimic = Mimic3StreamingTTSPlugin(config={"voice": "p239"})
        audio = mimic.get_tts("hello world", path)
        self.assertEqual(audio, path)
    
    def test_awb(self):
        path = "/tmp/hello_awb.wav"
        mimic = Mimic3StreamingTTSPlugin(config={"voice": "awb"})
        audio = mimic.get_tts("hello world", path)
        self.assertEqual(audio, path)
        
    def test_slt(self):
        path = "/tmp/hello_slt.wav"
        mimic = Mimic3StreamingTTSPlugin(config={"voice": "slt"})
        audio = mimic.get_tts("hello world", path)
        self.assertEqual(audio, path)