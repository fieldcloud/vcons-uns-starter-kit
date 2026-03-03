# Sample SIPREC session (simulated)

This folder simulates a single recorded SIP session.

Files:
- `session.json` — metadata (call_id, parties, timestamps, asset hint)
- `audio.wav` — recorded media (not included in repo)

To create a placeholder WAV for demos, you can generate a short silent audio file, e.g.:

```bash
# requires ffmpeg
ffmpeg -f lavfi -i anullsrc=r=16000:cl=mono -t 5 -q:a 9 -acodec pcm_s16le audio.wav
```
