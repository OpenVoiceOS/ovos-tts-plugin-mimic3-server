# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import random
import requests
from ovos_plugin_manager.templates.tts import TTS, TTSValidator, RemoteTTSException


class Mimic3StreamingTTSPlugin(TTS):
    """Interface to Mimic3 Streaming TTS."""

    def __init__(self, lang="en-us", config=None):
        config = config or {}
        super(Mimic3StreamingTTSPlugin, self).__init__(lang, config,
                                              Mimic3StreamingTTSValidator(self), 'wav')
        if self.config.get("url"):  # self hosted
            self.url = self.config["url"]
            # TODO disable cache to avoid filename conflicts with other voices
            if not self.voice or self.voice == "default":
                self.voice = f"selfhosted{random.randint(0, 9999999)}"
                self.cache.persist = False
        else:
            self.voice = "p239"
            self.url = "http://mycroft.blue-systems.com:59125/api/tts"
            self.cache.persist = True

    def get_tts(self, sentence, wav_file, lang=None):
        """Fetch tts audio using tacotron endpoint.

        Arguments:
            sentence (str): Sentence to generate audio for
            wav_file (str): output file path
        Returns:
            Tuple ((str) written file, None)
        """
        selected_voice = self.get_configured_voice_path(lang)
        params = {"voice": selected_voice}
        r = requests.post(self.url, params=params, data=sentence)
        if not r.ok:
            raise RemoteTTSException(f"Mimic3 server error: {r.reason}")
        else:
            audio_data = r.content
        with open(wav_file, "wb") as f:
            f.write(audio_data)
        pho = [['HH', '0.0775'], ['AH', '0.1550']]
        return (wav_file, pho) # Pass fake pho or it fails at utterance2visemes g2p error

    @property
    def available_languages(self) -> set:
        """Return languages supported by this TTS implementation in this state
        This property should be overridden by the derived class to advertise
        what languages that engine supports.
        Returns:
            set: supported languages
        """
        return set(Mimic3StreamingTTSPluginConfig.keys())
    
    def get_configured_voice_path(self, language=None):
        if not language:
            language = "en-us"

        if language in Mimic3StreamingTTSPluginConfig:
            voices = Mimic3StreamingTTSPluginConfig[language]
            for voice in voices:
                if self.voice == voice["voice"]:
                    voice_path = voice["region"] + "/" + voice["dataset"] + "#" + voice["voice"]
                    return voice_path
        else:
            return "en_US/vctk_low#p239"

class Mimic3StreamingTTSValidator(TTSValidator):
    def __init__(self, tts):
        super(Mimic3StreamingTTSValidator, self).__init__(tts)

    def validate_lang(self):
        lang = self.tts.lang.lower()
        assert lang.startswith("en")

    def validate_connection(self):
        pass

    def get_tts_class(self):
        return Mimic3StreamingTTSValidator


Mimic3StreamingTTSPluginConfig = {
"en-us": [
    {"voice": "awb", "gender": "male", "display_name": "cmu-artic_low | awb", "offline": False, "priority": 45, "region": "en_US", "dataset": "cmu_artic_low"},
    {"voice": "slt", "gender": "female", "display_name": "cmu-artic_low | slt", "offline": False, "priority": 45, "region": "en_US", "dataset": "cmu_artic_low"},
    {"voice": "rms", "gender": "male", "display_name": "cmu-artic_low | rms", "offline": False, "priority": 45, "region": "en_US", "dataset": "cmu_artic_low"},
    {"voice": "ljm", "gender": "female", "display_name": "cmu-artic_low | ljm", "offline": False, "priority": 45, "region": "en_US", "dataset": "cmu_artic_low"},
    {"voice": "9017", "gender": "male", "display_name": "hifi-tts_low | 9017", "offline": False, "priority": 45, "region": "en_US", "dataset": "hifi_tts_low"},
    {"voice": "92", "gender": "female", "display_name": "hifi-tts_low | 92", "offline": False, "priority": 45, "region": "en_US", "dataset": "hifi_tts_low"},
    {"voice": "elliot_miller", "gender": "male", "display_name": "m-ailabs_low | elliot_miller", "offline": False, "priority": 45, "region": "en_US", "dataset": "m_ailabs_low"},
    {"voice": "default", "gender": "female", "display_name": "ljspeech_low | default", "offline": False, "priority": 45, "region": "en_US", "dataset": "ljspeech_low"},
    {"voice": "p239", "gender": "female", "display_name": "vctk_low | p239", "offline": False, "priority": 45, "region": "en_US", "dataset": "vctk_low"},
],

"de-de": [
    {"voice": "neutral", "gender": "male", "display_name": "thorsten-emotion_low | neutral", "offline": False, "priority": 45, "region": "de_DE", "dataset": "thorsten-emotion_low"},
    {"voice": "amused", "gender": "male", "display_name": "thorsten-emotion_low | amused", "offline": False, "priority": 45, "region": "de_DE", "dataset": "thorsten-emotion_low"},
    {"voice": "default", "gender": "male", "display_name": "thorsten_low | default", "offline": False, "priority": 45, "region": "de_DE", "dataset": "thorsten_low"},
],

"es-es": [
    {"voice": "default", "gender": "male", "display_name": "carlfm_low | default", "offline": False, "priority": 45, "region": "es_ES", "dataset": "carlfm_low"},
    {"voice": "karen_savage", "gender": "female", "display_name": "m-ailabs_low | karen_savage", "offline": False, "priority": 45, "region": "es_ES", "dataset": "m_ailabs_low"},
],

"fr-fr": [
    {"voice": "default", "gender": "male", "display_name": "tom_low | default", "offline": False, "priority": 45, "region": "fr_FR", "dataset": "tom_low"},
    {"voice": "default", "gender": "female", "display_name": "siwis_low | default", "offline": False, "priority": 45, "region": "fr_FR", "dataset": "siwis_low"},
],

"it-it": [
    {"voice": "default", "gender": "male", "display_name": "riccardo-fasol_low | default", "offline": False, "priority": 45, "region": "it_IT", "dataset": "riccardo-fasol_low"},
    {"voice": "6807", "gender": "female", "display_name": "mls_low | 6807", "offline": False, "priority": 45, "region": "it_IT", "dataset": "mls_low"},
],

"nl-nl": [
    {"voice": "default", "gender": "male", "display_name": "bart-de-leeuw_low | default", "offline": False, "priority": 45, "region": "nl_NL", "dataset": "bart-de-leeuw_low"},
    {"voice": "default", "gender": "male", "display_name": "nathalie_low | default", "offline": False, "priority": 45, "region": "nl_NL", "dataset": "nathalie_low"},
]

# Note: No pt-pt voices available yet
}
