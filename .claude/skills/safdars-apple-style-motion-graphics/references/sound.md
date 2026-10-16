# Sound design (approved)

Principle (owner): professional, restrained, Apple-like. NOT sfx heavy. The approved 28.45 s edit uses 17 cues in total. Budget for the full video: about the same density (<= 1 cue per ~1.7 s), mostly tied to cuts and 3-4 big reveals.

## Sources
- Owner uploads (copies in `hf/edit30/sfx_owner/`, processed 48 kHz stereo in `hf/edit30/sfx3/`): RH-SWOOSH3 (0.67 s, peak at 0.30 s), RH-CAMERA4 (0.17 s shutter click, peak at 0.05 s), RH-RISER (1.6 s, climax at its very end, first 0.35 s near silent).
- Owner folder `Apple ui/` (repo root, from `main`), 11 mp3s. Processed copies (peak -8 dBFS) in `sfx3/`: `click` (ui-click-43196, sign-up press), `deep` (ui-click-deep, hit on "$0" and "never"), `pop` (ui-pop, trimmed 0.5 s), `impact` (battle-pop first 0.8 s, "$216" landing), `applepay` (apple-pay chime, "Technically true"), `ding` (universfield ui-interface-03, trimmed 1.6 s, problem solved). NOT used: crickets "mid-nights", phone-typing, bubble-pop, dragon-studio notification (available if a role needs it).
- Synthetic layer (ffmpeg aevalsrc, in `sfx3/`): `boom` (under the big hits), `swell` (unused now), `relief` (warm chord when the problem is solved). Kenney CC0 files in `sfx2/` are fallback only.
- REJECTED by the owner: iPhone "message sent" swish (`swish_in/out`), sine-tone UI sounds, per-row tick spam, cash-register ka-ching, more than one riser, camera click on every cut.

## Role map / cue rules (`gen.py`, section after the `modes` list)
- Major cut at T: `swoosh3` starts at `T-0.30` (its peak lands on T), vol .6. Minor cuts: no sound (quiet is professional).
- `camera4` only on the opening cut and ONE later key cut (the cut into the checkout reveal), starts `T-0.05`, vol 1.0 / .8. Do not add more than ~1 per 12-15 s.
- `riser`: ONCE, ends on the opening "$0" reveal (`hero - .24 - 1.58`). The owner said one is enough for the whole video.
- Hits: `deep` + `boom` on the opening hero; `impact` + `boom` on the biggest number landing ("$216"). Use `relief` + `ding` + `click` when a problem is solved (switch off).
- Gestures: `click` on a button press, `applepay` on a confirmation check. Pills/chips/rows/bars/tiles: silent.
- Align by PEAK, not file start. Offsets: camera4 -0.05, swoosh3 -0.30, riser -1.58 (to end on the hit). Sounds with slow attack (applepay 88 ms) read late: start 50 ms earlier if needed.
- Silence is part of the design: one beat of near-silence right before an impact.

## Mix and loudness
- `hf/edit30/mixdown.sh <picture master mp4> <out prefix>`: voice (aroll audio, vol 1.0) + `assets/sfx.wav` (vol 0.6) -> two-pass loudnorm (I=-16, TP=-1.5, LRA=7, measured values, `linear=true`) -> mux onto the picture master (no re-render needed for audio-only changes) -> 30 fps copy (`tmix=frames=2` + `select='not(mod(n,2))'`). Single-pass loudnorm undershoots (-18.4 LUFS); two-pass gives about -16.5.
- Voice raw mix is very quiet (-29.6 LUFS before normalising).

## Verification (earshot, optional but valuable; I cannot listen, earshot can)
- Install is scratch-only (lost on restart): `git clone https://github.com/Leonxlnx/earshot`, `python3 -m venv .venv`, `.venv/bin/python -m pip install torch --index-url https://download.pytorch.org/whl/cpu`, `.venv/bin/python -m pip install -e ".[mcp,llm,dev]"`, `.venv/bin/python -m earshot doctor --load` (downloads ~1.4 GB, ~10 min).
- Check: `EARSHOT_THREADS=3 .venv/bin/python -m earshot timeline VIDEO --cues "t1,t2,..." --detail low` with the visual-landing times as cues (cut instants, big hits, clicks). Approved results: 26-30 ms median, 77-100% within 100 ms, -16.5 LUFS.
- `earshot describe FILE` classifies a sound (used to map the Apple UI folder to roles). Do not read "music/genre" labels as facts; they are CLAP guesses.
- The `sound-effects` skill (ElevenLabs generation) needs `ELEVENLABS_API_KEY` and the owner's approval before spending credits; not used so far.
