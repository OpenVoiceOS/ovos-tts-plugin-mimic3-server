## Description

OVOS Streaming TTS plugin for [Mimic3](https://github.com/MycroftAI/mimic3)

## Install

`pip install ovos-tts-plugin-mimic3-streaming`

## Configuration

```json
  "tts": {
    "module": "ovos-tts-plugin-mimic3-streaming",
    "ovos-tts-plugin-mimic3-streaming": {
        "voice": "slt"
    }
  }
 
```

Available Voices (Limited Voices From):
- https://github.com/MycroftAI/mimic3-voices
  - Lang: en_US, dataset: "cmu-artic_low"
    - Voices: "awb", "slt", "rms", "ljm"
  - Lang: en_US, dataset: "hifi-tts_low"
    - Voices: "9017", "92"
  - Lang: en_US, dataset: "m-ailabs_low"
    - Voices: "elliot_miller"
  - Lang: en_US, dataset: "ljspeech_low"
    - Voices: "default"
  - Lang: en_US, dataset: "vctk_low"
    - Voices: "p239"

  - Lang: de_DE, dataset: "thorsten-emotion_low"
    - Voices: "neutral", "amused"
  - Lang: de_DE, dataset: "thorsten_low"
    - Voices: "default"

  - Lang: es_ES, dataset: "carlfm_low"
    - Voices: "default"
  - Lang: es_ES, dataset: "m-ailabs_low"
    - Voices: "karen_savage"

  - Lang: fr_FR, dataset: "tom_low"
    - Voices: "default"
  - Lang: fr_FR, dataset: "siwis_low"
    - Voices: "default"

  - Lang: it_IT, dataset: "riccardo-fasol_low"
    - Voices: "default"
  - Lang: it_IT, dataset: "mls_low"
    - Voices: "6807"
  
  - Lang: nl_NL, dataset: "bart-de-leeuw_low"
    - Voices: "default"
  - Lang: nl_NL, dataset: "nathalie_low"
    - Voices: "default"

### Self Hosting
- Follow docker instructions from https://github.com/MycroftAI/mimic3
