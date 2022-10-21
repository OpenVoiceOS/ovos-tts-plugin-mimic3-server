import unittest

from ovos_tts_plugin_mimic3_server import Mimic3ServerTTSPlugin

mimic = Mimic3ServerTTSPlugin()


class TestTTS(unittest.TestCase):
    def test_default_voice(self):
        path = "/tmp/hello_ap.wav"
        # also testing that en-gb resolves to the internally used (wrong) en-uk
        audio, phonemes = mimic.get_tts("hello world", path, lang="en-gb")
        self.assertEqual(audio, path)
    
    def test_speaker_in_voice(self):
        path = "/tmp/hello_awb.wav"
        # specify speaker together with voice
        audio, phonemes = mimic.get_tts("hello world", "test4.wav",
                              voice="en_US/cmu-arctic_low#awb")
        self.assertEqual(audio, path)
        
    def test_voice_plus_speaker(self):
        path = "/tmp/hello_slt.wav"
        # specify speaker via optional args
        audio, phonemes = mimic.get_tts("hello world", path,
                              voice="en_US/cmu-arctic_low", speaker="slt")
        self.assertEqual(audio, path)

    def test_voice_plus_lang(self):
        path = "/tmp/hello_rms.wav"
        # lang separated from voice key also valid
        audio, phonemes = mimic.get_tts("hello world", path,
                              voice="cmu-arctic_low#rms", lang="en-us")
        self.assertEqual(audio, path)
