# Pipeline: setup, files, commands, timings, scaling to the full video

## Fresh-session setup (the cloud container is ephemeral; only git survives)
1. `cd /home/user/LLC && git checkout claude/nifty-fermi-w9ften && git pull`. Then `bash setup.sh` (rebuilds `footage/raw_footage_1.mp4` + `reference/sample_llc_1.mp4` from parts, checks SHA256). Never commit the full videos.
2. Repo already contains: `plan/words_raw.json` (Whisper word times for the whole 144 s), `hf/edit30/*` (project), `Apple ui/` and `hf/edit30/sfx3|sfx_owner` (sounds), `hf/edit30/fonts`, logo files, previous renders.
3. Tools: ffmpeg is installed. HyperFrames via `npx -y hyperframes@0.8.164 ...` (pinned; first run downloads). Chrome: `npx hyperframes@0.8.164 browser ensure`. Python with Pillow/numpy is present. The `.agents/` and `.claude/skills/*` folders created by `npx skills add ...` are git-ignored; re-install if wanted: `npx -y skills add heygen-com/hyperframes -y` (inside `hf/edit30`). The `media-use`, `motion-design`, `apple-design` skills are available as session skills.
4. Optional: earshot (see sound.md). Whisper only if re-transcribing: `pip install faster-whisper` and pass a NumPy array, not an mp4 path (the `av` build in this container rejects mp4 paths).

## File map
- `hf/edit30/gen.py`: the generator. (a) cuts raw footage with ffmpeg into `assets/aroll.mp4` WITH the studio grade baked in (`CUT=1`, default; `CUT=0` skips the cut), (b) builds `assets/sfx.wav` from the cue list, (c) fills `template.tpl` with timing data -> `index.html`.
- `hf/edit30/template.tpl`: composition HTML/CSS/GSAP (NOT named .html: two root compositions in one project break the runtime). Placeholders: `@@CFG@@` (JSON config), `@@D@@` (duration), `@@<Scene>a@@` / `@@<Scene>d@@` (scene start/duration).
- `hf/edit30/index.html`: generated, committed. `hf/edit30/mixdown.sh`: audio finishing. `hf/edit30/compositions/organic-light-leak-overlay.html`: installed registry block (reference only; leak is re-implemented inline).
- `renders/`: keep latest `*_edit_vN_60fps.mp4` (picture master, needed for audio-only remixes) and `*_final_60fps/30fps.mp4`.
- Timing model in gen.py: speech words from `words_raw.json` -> keep-intervals (each word padded -0.06/+0.12 s, merged when the gap <= 0.40 s, so pauses > 0.4 s are cut) -> `mp(raw_time)` maps raw time to edit time. `find(word, after_raw)` / `T(word, after_raw)` return the mapped start of the first matching word after a raw time. `win` (scene windows), `kin` (per-word anchor times), `modes` (layout cuts: `[mode, cut_time, "major"|"minor"]`), `segs` (cut boundaries, used for alternating punch-ins), `cues` (sound).
- Known manual cut: the stutter "I've formed two, I've" (raw 41.4-43.7) is dropped; word at 42.59 is shifted to 43.65. Dead air at start removed (speech starts 11.77 s). Gap 29.7-41.4 s (dead air) is removed by the merge rule.

## Commands (run from `hf/edit30`)
```
CUT=1 python3 gen.py                       # re-cut + regenerate everything (~1-2 min); CUT=0 for template/sfx-only changes
npx -y hyperframes@0.8.164 check            # lint: errors block; a contrast warning at leak moments is expected
npx -y hyperframes@0.8.164 snapshot --at 1.5,5.5,7.0,14.0,16.0   # 1-2 min; look at the contact-sheet.jpg
nohup npx -y hyperframes@0.8.164 render --fps 60 -o /home/user/LLC/renders/NAME_60fps.mp4 > /tmp/render.log 2>&1 &
   # poll ONLY for the output file in a run_in_background loop:  until [ -f FILE ]; do sleep 10; done
./mixdown.sh ../../renders/NAME_60fps.mp4 ../../renders/NAME_final   # audio + 30 fps copy
```
- Timings measured here (software GL): snapshot of 6 times ~1.5 min; 60 fps render ~10 s of wall time per output second (28 s = 3-5 min). A 144 s video = about 25-30 min per render, so snapshot-review everything first and render only a few times. `--fps 30` roughly halves a draft render.
- Foreground tool calls die at 10 min: always background the render.
- `render --help` options: `--fps`, `--quality`, `--workers`, `--crf`.

## Adding a scene (recipe)
1. Pick the layout mode and the raw time window; add the window to `wd` and the word anchors to `kin` (use `T("word", raw_time_before_it)`; check the word actually exists at that time in `words_raw.json`).
2. Add a `<section class="scene clip" id="Lx" data-start="@@Lxa@@" data-duration="@@Lxd@@" data-track-index="2">` to the template (content inside `.lz` or `.lz.fs`, centred) and its JS block (use `mk`, `pop`, `ring`, count-up patterns).
3. Add the cut to `modes` (`[mode, T, "major"|"minor"]`) and, if warranted, cues. Keep each layout >= 1.5 s.
4. `CUT=0 python3 gen.py`, `check`, `snapshot` (presenter visible in full + split!), fix, render.
- `.clip` elements are shown only inside their data-start/duration window; the runtime hides them otherwise. Never tween `display`/`visibility`/`autoAlpha` on a `.clip`. Initial hidden state: let `fromTo` use default `immediateRender`.

## Scaling gen.py to the whole video (~144 s) - recommended refactor
- Today `W`, `wd`, `kin`, `modes`, `cues` are hardcoded for raw 11.7-58.3 s. For the full video: extend `W` to the whole speech range (11.7 -> 143.1 s) and keep the same interval/merge logic; replace the hardcoded dicts with a list of scene definitions (`id, raw_start, raw_end, mode, anchor words`) so adding scenes is data not code; template sections can be generated from the same list.
- Keep `D` computed; the template root `data-duration`, video, audio and timeline all use `@@D@@`.
- Long compositions: the number of `immediateRender` tweens grows; keep selectors specific. If a render gets slow, split the composition into sub-compositions (see hyperframes-core `sub-compositions.md`) per section.
- Re-check the presenter alternate punch-in and slow push logic works with many segments (`C.segs`).
- Footage ends at raw 143.1 s mid-sentence ("...operating agreement."): no CTA exists. Ask the owner whether to end on a deliberate cliffhanger card or if more footage is coming.
