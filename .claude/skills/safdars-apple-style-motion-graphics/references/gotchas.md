# Gotchas: bugs already hit (each cost real time)

## Render / environment
- **Realtime colour grade is unusable here**: HyperFrames `data-color-grading` (media-treatment shader) rendered ~15 s per frame on software GL (56/1707 frames in 14 min) and made `hyperframes check` time out ("Check did not finish within its deadline"). Bake the grade with ffmpeg in `gen.py` (done).
- **Killed render leaves a corrupt frame cache** `/tmp/hyperframes-extract-cache-*` (1.2 GB). Next render shows `extract 0.0s` and BLACK presenter after the first ~1 s. After any killed/aborted render: `rm -rf /tmp/hyperframes-extract-cache-*`. Kill render processes with `pkill -x node; pkill -x chrome-headless; pkill -x ffmpeg` (exact names; `pkill -f` with a pattern that also matches your own command kills your own shell, and process names > 15 chars never match with `-x`).
- **Wait loops**: `until ... ! pgrep -f "<pattern>"` matches itself and never ends. Poll for the output FILE only (`until [ -f FILE ]; do sleep 10; done`) inside a `run_in_background` call; the loop's time limit is 30 min.
- **Foreground limit 10 min**; run renders with `nohup ... &` and a background poller. When you change the template mid-render, kill the render first (then clear the cache).
- The hyperframes check "contrast" warning near light-leak moments (e.g. 20.5 s) is a transient from the overlay; ignore. 0 errors is the bar.
- `hyperframes add <block>` has no `--yes` flag. `media-treatment ... --apply` edits `index.html` directly, which `gen.py` overwrites; put attributes in `template.tpl`.

## Template / GSAP
- **Never slice `template.tpl` by string index across CSS blocks** (`t[a:b]`). A slice from "/* L9 ..." to the first `#vig{` silently deleted the `#world`, `#leak`, `.lk*`, `#lkflash` rules: `#world` collapsed to 0x0 and, once the first push-zoom transformed it (a transformed element is the containing block for absolute children), the presenter (`#vframe{inset:0}`) vanished from 1.5 s on. Renders v10-v13 were wrong. After every template edit assert the neighbouring rules still exist (`assert "#world{" in t`) and snapshot the presenter in full AND split layouts BEFORE rendering.
- `fromTo(..., {immediateRender:false})` leaves an element VISIBLE before its tween (shows text before it animates in). Use it only to chain a second tween on a property whose CSS default already matches; single-use reveals keep the default. Rings/overlays that start invisible need CSS opacity 0 + `immediateRender:false`.
- Gradient text: class on each word span, right padding (else the last glyph, the "0" of "$0", is clipped).
- Never tween `fontSize`/`width`/layout props (lint `gsap_non_transform_motion`, steppy): use `scale`/`x`/`y`/`opacity`.
- Two root compositions (template `.html` next to `index.html`) break the runtime: keep the template as `.tpl`.
- `Math.random` is banned (lint, non-determinism): use a seeded PRNG (none needed currently).
- An `<audio>` needs an `id` and must sit INSIDE the root composition element. Never put `data-start` on a wrapper around a `<video>`. Audio shorter than its data-duration only logs a warning.
- Do not use `backdrop-filter` blur > 20 px in product UI; our video uses 50 px for the glass look (render cost is acceptable); blur filters in tweens <= 10 px.
- Text transforms: `transform-origin` for the presenter zoom is `58% 0%` (top edge fixed so the head is never cropped further).
- ffmpeg `vignette` `mode=forward` darkens edges, `backward` brightens them. Do not add a vignette to the footage (overlay `#vig` already exists).
- SVG chart label: measure `offsetWidth` and clamp so "$200 / yr" stays inside the panel (it was clipped at the panel edge).

## Audio
- Single-pass loudnorm undershoots (-18.4 LUFS); use the two-pass in `mixdown.sh`.
- Align samples by their PEAK (camera4 -0.05 s, swoosh3 -0.30 s, riser -1.58 s). Negative start times are clamped to 0 (harmless for the riser's silent first 0.35 s).
- `volumedetect` prints with `-hide_banner -nostats` and without `-v error`.

## Footage / transcript
- Whisper small timings are reliable per word except the FIRST word after a long silence (can be early by ~0.3 s); check by listening/silencedetect. Re-transcribing the cut audio and comparing to caption times gave 0.01 s median error.
- The raw footage: 144 s, 30 fps, speech 11.77-143.1 s, large dead gap 29.7-41.4 s, stutter at 41.4-43.7 s. The presenter's hair touches the top of the frame.

## Process
- Images pasted into chat are not on disk. Files from the owner come via `main` (repo) or `/root/.claude/uploads/<session>/`. Check `git fetch origin && git ls-tree -r origin/main --name-only`.
- Stop hook: the repo must be clean at the end of every turn. Commit + push; delete throwaway files (old renders) rather than leaving them untracked.
- When the owner reports "I see X", first ask which of the plausible things they mean if unclear (black backdrop by design vs missing footage vs viewer showing transparent PNGs as black).

## Portrait 1080x1920 edits (WhatsApp one-offer video, hf/oneoffer)
- Template: `hf/oneoffer/template.tpl`. Presenter card sits at the TOP (clip `inset(90px 60px 990px 60px round 48px)`, vclip y=90, card-mode `#vz` scale .9 so chin/mouth stay inside); split graphics zone is the lower half (`.lz` left 40 top 960 w1000 h880); fs uses the full 1080x1920 box; pills in full mode go over the shirt (top ~1250).
- `.ln` mask lines clip descenders ("money." rendered "monev."): padding-bottom .22em and margin-bottom -.1em.
- Low-res phone source (464x832) is upscaled 2.3x in gen.py GRADE (lanczos + unsharp); tell the user it is soft.
- `mixdown.sh <picture> <out prefix> <duration>` takes the duration as 3rd arg (hf/oneoffer/mixdown.sh); intermediate wavs use /tmp/oo_ prefix.
- 61 s portrait render at 60 fps took ~11 min (software GL).
