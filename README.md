## Description

OVOS Server TTS plugin for [Mimic3](https://github.com/MycroftAI/mimic3)

## Install

`pip install ovos-tts-plugin-mimic3-server`

## Configuration

```json
  "tts": {
    "module": "ovos-tts-plugin-mimic3-server",
    "ovos-tts-plugin-mimic3-server": {
        "voice": "en_UK/apope_low"
    }
  }
 
```

### Voices

You can find a list of valid voices [here](https://github.com/MycroftAI/mimic3-voices)

you can specify a speaker by adding `#speaker_name` at the end of the voice

NOTE: mimic3 uses the terminology "voice" and "speaker". A more accurate nomenclature would be "model" and "voice/speaker"


## Self Hosting
- Follow docker instructions from https://github.com/MycroftAI/mimic3


## Standalone usage

```python
from ovos_tts_plugin_mimic3_server import Mimic3ServerTTSPlugin

tt = Mimic3ServerTTSPlugin()
tt.get_tts("hello world", "test.wav", lang="en-gb")  # default voice
tt.get_tts("hello world", "test3.wav", voice="en_US/cmu-arctic_low", speaker="slt")  # specify speaker via optional args
tt.get_tts("hello world", "test4.wav", voice="en_US/cmu-arctic_low#awb") # specify speaker together with voice
tt.get_tts("hello world", "test5.wav", voice="cmu-arctic_low#rms", lang="en-us")  # lang separated from voice key also valid
```