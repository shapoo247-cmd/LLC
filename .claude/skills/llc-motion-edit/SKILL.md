---
name: llc-motion-edit
description: Rules, workflow and past mistakes for editing the LLC talking-head video (footage/raw_footage_1.mp4) with Apple-style motion graphics in HyperFrames. Read before building, changing or reviewing any graphic, caption, cut or sound effect in this repo.
---

# LLC motion edit: rules and corrections

Owner feedback is recorded here so the same mistakes are not repeated. Add every new correction below before moving on.

## Project facts
- Style: Apple keynote. Black base, huge tightly tracked Inter Display type, soft ambient colour glows, frosted-glass cards, spring motion. NOT the reference's purple clay 3D, and not a copy of it. The reference is a quality floor only.
- Tooling: HyperFrames (`npx hyperframes@0.8.164 check | snapshot --at ... | render -o ...`). Do NOT use vidIQ tools. HyperFrames skills are installed per project under `.agents/skills/` (`npx -y skills add heygen-com/hyperframes -y`).
- Projects: `hf/style-demo` (look test), `hf/edit30` (first ~28 s edit). Generator: `hf/edit30/gen.py` builds `assets/aroll.mp4` (cuts), `assets/sfx.wav` and `index.html` from `plan/words_raw.json` (Whisper word times) and `hf/edit30/template.tpl`.
- Cut rules: speech starts at raw 11.77 s; remove dead air, the 29.7-41.4 s gap and the "I've formed two, I've" stutter; cut pauses longer than 0.4 s.
- Cloud sandbox: no `pkill -f` on a pattern that matches the running shell (it killed the shell once); copy fonts locally and use `@font-face`; no `Math.random` (use a seeded PRNG); an `<audio>` must have an `id` and sit inside the root; never put `data-start` on a wrapper around a `<video>`.

## Corrections from the owner (apply always)
1. **Sync means the hit lands on the word.** Start each animation about 0.15-0.2 s BEFORE the spoken word so its peak lands on the word. Never start the tween at the word (it lands late and feels out of sync). Use short snappy springs (0.35-0.5 s), not 0.9 s fades.
2. **Real motion design, not fades.** Use per-word kinetic text (words rise through a mask on their own onsets), springs with controlled overshoot, shared-element transitions (the A-roll shrinks into a rounded card), number count-ups, staggered reveals, depth/parallax. Whole-block fade + blur is not enough.
3. **Never put graphics on the speaker's face or head.** She sits right of centre (face about x 1000-1300, y 150-520 at full frame). Keep overlays in the free left zone, a lower-left lane, or beside her in a split layout.
4. **Keep the speaker on screen.** Do not cover the A-roll with full-screen takeovers for most of the runtime. Use a split layout (A-roll in a rounded card on the right, graphic on the left) and keep captions running.
5. **Sound effects must feel like Apple UI sounds.** Soft, glassy, tonal, short, quiet, with a touch of reverb: tink, soft tap, airy swish, gentle two-note confirm, soft click. No risers, no cash-register "ka-ching", no noisy thuds, no music-like drones. Fewer cues, each tied to a visible event.
6. **Review before sending.** Never send a render that has not been checked frame by frame around every graphic beat (snapshots at the word times, not just midpoints) and for overlap with the face. Do not describe things as verified when only stills were checked.
7. **Do not over-claim.** Say what was and was not verified (e.g. "checked stills, not watched at speed").

## Workflow
1. Update `plan/words_raw.json` timings only from Whisper word output; map raw time to edit time through the cut intervals in `gen.py`.
2. Run `python3 gen.py`, then `npx hyperframes check`, then `snapshot --at` the lead-in, hit and settle of each beat.
3. Render, then sample frames at 10 fps around beats and look for: face overlap, text cut off at the right edge (gradient text needs right padding), late hits, SFX that do not match a visible event.
4. Commit and push to `claude/nifty-fermi-w9ften` (no PR unless asked).

## Build gotchas learned (HyperFrames + GSAP)
- `fromTo(..., immediateRender:false)` leaves the element VISIBLE before its tween starts. Use it only to chain a second tween on a property whose CSS default already matches. Single-use reveals must keep the default so they start hidden.
- Gradient text (`background-clip:text`): put the class on each inline-block word span (not on the line container) and give it right padding, otherwise the last glyph (e.g. the 0 in "$0") is clipped.
- Never tween `fontSize`/`width` (lint `gsap_non_transform_motion`); use `scale` + `x`.
- Do not keep a template `.html` next to `index.html` (two roots). Template is `template.tpl`; `gen.py` writes `index.html`.
- After `gen.py`, run `npx hyperframes@0.8.164 check`; fix lint `content_overlap`, `text_occluded` and contrast before rendering.

## Motion principles (from the installed `apple-design` HIG skill: `.agents/skills/apple-design/references/hig/motion.md`)
- Motion is purposeful and supports the story; no decorative or peripheral motion. Background glows stay static and only crossfade between beats (continuous drift removed).
- Feedback animations are brief and precise, tied to the exact event they explain.
- Keep realistic, reversible directions: what enters from the right leaves to the right; the A-roll card grows back the way it shrank.
- Smoothness: motion looks steppy at 30 fps; render the master at 60 fps (`render --fps 60`) and derive a 30 fps motion-blurred copy (ffmpeg `tmix` + `select`) for the 30 fps spec in CLAUDE.md.
- Presenter framing: keep her head fully in frame (top of head touches the source frame edge, so the card must start at source y=0), and zoom with `transform-origin: 58% 0%`.

## Mode mix (owner request)
Alternate three layouts: `full` (presenter full frame), `fs` (full-screen animation, presenter hidden, voice continues), `split` (presenter card on the right, graphic on the left). No bottom captions.

## Sound rules (installed skills: `design/game-feel/sound-design.md`, `sound-effects`)
- Small palette (about 4-6 sounds: soft transition, tap, click, tink, toggle, confirm). One sound per completed gesture. No tick spam per row/bar/tile; routine = quiet, rare = bigger.
- Fire the sound when the visual change lands (its peak), never before it and never for something that fails.
- Sources: Kenney "Interface Sounds" (CC0, `hf/edit30/sfx2/`, normalised to -8 dB peak). `sound-effects` skill can generate sounds via ElevenLabs but needs `ELEVENLABS_API_KEY` and the owner's approval before spending credits.
- Sound never carries meaning alone; the picture must make sense muted.

## Delivery checks (earshot installed at scratchpad `earshot_src/repo`; `python -m earshot timeline VIDEO --cues "t1,t2,..."`)
- Run earshot `timeline` with the visual-landing times as `--cues`. v4 result: median sound-to-cue offset 23 ms, 100% within 100 ms.
- Normalise the final audio to about -16 LUFS, true peak <= -1.5 dBTP (`loudnorm=I=-16:TP=-1.5:LRA=7`). The raw mix was -29.6 LUFS, far too quiet.
- Deliver a 60 fps master (`render --fps 60`) and a 30 fps copy made with `tmix=frames=2` + `select='not(mod(n,2))'` for the 30 fps spec.
- All graphics are CENTRED: full-screen on x=960, side-by-side zone on x=565, both on y=540. Pills over the presenter are dark, high-contrast and sit mid-height in the free left lane (x 40-700), never in the same colour as the footage.
- Easing (from the motion-design skill): ease-out-quint/quart for enters, ease-in-out for on-screen moves, no bounce/overshoot on enters, scale from about .95 (never ~0), blur at most 10px.

## Round 3 corrections (owner)
- NEVER flash the presenter for a few frames and then fade her out. Open on her for a real beat (>= 1 s) with a slow push-in. Never fade her while she is talking; layout changes move her (shrink into the card, dock into the right edge via `DOCK` clip), they do not fade her. Hold the presenter full-frame or in the card for >= 1.5 s at a time.
- The owner's "Apple UI" sound-effect folder is the preferred SFX source. As of this round it was NOT in the repo, uploads or Drive; ask for it to be pushed to the branch. Map sounds by ROLE (in/out, tap, click, tink, toggle, confirm) in `gen.py` so the folder can be dropped in.
- The edit must carry emotion and suspense, not just clean UI: build tension (dark, slow push-in, low swell), a beat of silence, then an impact on the big reveals ($0, $216), a shockwave ring on each hit, and a relief chord when the problem is solved (switch off). Pacing and sound carry the feeling.
- Rings/overlays that start invisible must use `immediateRender:false` with CSS opacity 0, or they show as outlines before they fire.

## Apple UI sound folder (`Apple ui/` on `main`, copied into the branch)
Role map from earshot readings: message-sent swish = panel transition in (reversed = out); ui-click-deep = deep hit on "$0" and "never"; ui-click-43196 = button click; ui-pop = chip/tag pops; battle-pop (first 0.8 s) = impact on "$216"; apple-pay chime = "Technically true" check; universfield ding = problem solved (switch off). Skipped: crickets "mid-nights", phone typing, bubble-pop. Processed copies are in `hf/edit30/sfx3/` (peak -8 dB). Synthetic suspense layer (swell/boom/relief) sits under them.
- Slow-attack sounds (apple-pay 88 ms, message-sent 92 ms) measured about 54 ms median off the visual peak in earshot; if it matters, start those cues 50 ms earlier.
- Remux audio without re-rendering: render video once, then `ffmpeg -i video -i aroll.mp4 -i sfx.wav -filter_complex "[1:a]volume=1[v];[2:a]volume=.6[s];[v][s]amix=inputs=2:normalize=0,loudnorm=I=-16:TP=-1.5:LRA=7" -c:v copy`.
## Shell gotcha
- Never write a wait loop like `until ... ! pgrep -f "<pattern>"` where the pattern also appears in the loop's own command line: it matches itself and never ends. Poll for the output file only, or check `ps` once.

## Round 4 correction (owner): presenter <-> animation transitions
- Shrink/dock/fade layout morphs were rejected as unprofessional. Cut between layouts instantly UNDER a light leak (layered amber/red/gold screen-blended glow, style of registry block `organic-light-leak-overlay`; installed in `hf/edit30/compositions/`, timing re-implemented inline in `template.tpl` because the block peaks ~1 s in), with a push-zoom through the cut, a reverse swish building into the cut, a soft hit on it, and an airy tail after. Major leak (peak .82) for any cut that brings the presenter in or out of full frame; minor (.55) for split <-> full-screen animation. Alternate the sweep direction.
- Cut times in `gen.py` `modes` are the cut instants (first graphic appears there), not transition starts.

## Colour grade (owner request: professional studio grade on the presenter)
- Done through HyperFrames media-treatment (skill `media-use`, recipe "Natural Portrait"), NOT hand-rolled filters. Source measured clean (mid exposure, no clipping, low saturation) so it is a polish grade. Payload on `<video id="av">` (`data-color-grading`, stored in `template.tpl` so `gen.py` keeps it): preset skin-soft, intensity .72, exposure +.08, contrast +.08, highlights -.18, shadows +.12, whites -.08, blacks -.04, temperature +.04, tint +.015, vibrance +.06, saturation +.04, vignette .05 (all inside the recipe's safe ranges).
- Workflow: before sheet -> `hyperframes media-treatment --selector '#av' --grading '<json>' --apply --json` -> after sheet + face close-up check -> copy the attribute into the template (re-applying via CLI after every `gen.py` run is the failure mode that lost it once).

### Colour grade: baked with ffmpeg, not the realtime shader
- The `data-color-grading` shader path rendered at ~15 s/frame on this software-GL machine (56 of 1707 frames in 14 min) and made `hyperframes check` time out. Do NOT use it for the full render here.
- The approved Natural Portrait look is reproduced in `gen.py` as `GRADE` (applied after the cut concat): gentle S-curve with shadow detail and highlight roll-off, tiny warm mids / cool shadows via `colorbalance`, `vibrance` .08; NO ffmpeg vignette (it stacked with the `#vig` overlay and darkened the edges too much). Verified against the media-treatment result on face close-ups.
- Always compare original / graded / reference crops before rendering; first two tries were too orange then too milky.

## Owner's RH sounds (round 5), now the primary transition / build-up sounds (`hf/edit30/sfx_owner/`, processed copies in `sfx3/`)
- Do NOT use the iPhone "message sent" swish (rejected). Every cut: RH-SWOOSH3 (peak at 0.30 s into the file, so start it at T-0.30) + RH-CAMERA4 (shutter click, peak at 0.05 s, start at T-0.05). Major cuts louder (.8 / 1.0), minor (.55 / .6).
- Build-ups: RH-RISER (1.6 s, climax at its very end) ends exactly on the hit: starts at hit-1.58. Used before "$0", before the "$216" landing and under the price chart. A slightly negative start time is harmless (the first 0.35 s is near-silent).
- Align every sample by its measured PEAK, not its file start: earshot sound-to-cue sync went from median 54 ms to 26 ms after doing this.
- Loudness: single-pass loudnorm landed at -18.4 LUFS; two-pass (measure, then `linear=true`) gives -16.7 LUFS.
- Video-only edits need no re-render: keep the picture master (`first30_apple_edit_v8_60fps.mp4`) and remux new audio onto it.

## Round 6 corrections (owner): sound restraint + better 0:19 hook
- "Professional, not SFX heavy." RH-RISER: exactly ONE, at the start (into the opening $0 reveal). RH-CAMERA4: only twice (the opening cut and the cut into the checkout), never on every transition. RH-SWOOSH3: major cuts only (5), none on minor cuts. Removed: chip/tag pops, "never" thump, extra risers. Target about 17 cues in 28 s, each tied to a key gesture.
- 0:19 price scene (L6) rebuilt: a line chart draws on with an accelerating climb, a dot leads it, a counter rides the dot from $0 to $200 (green -> amber -> red), area fill follows, one small ring at the top. Replaces the plain bars + "$200 / yr" tag. Keep the end label inside the panel (measure `offsetWidth`).
- `hf/edit30/mixdown.sh <picture master> <out prefix>` does the audio remux + two-pass loudnorm + 30 fps copy.

## Round 7 (owner): real site content + logo
- 0:27 scene (L9) rebuilt from the owner's screenshot of the real services menu: three glass columns (Start your business / Compliance & operations / Branding & marketing) with all 27 features and stroke icons, cascading in on "pile", then everything dims on "never" except "LLC formation", which glows green. Text is the site's own; styling is ours (no site branding).
- The owner approved using the Tailor Brands logo. Images pasted in chat are NOT saved to disk unless they arrive as uploads; the logo was not on disk (only `images/1.png`, the site screenshot). Ask for the logo file (push to the branch/main like `Apple ui/`) before using it, and never redraw a brand logo by hand. Planned placement: above "$0" in the opening scene and on the L9 menu header.

- Logo delivered by the owner at repo root on `main`: `tailor-brands-logo-png_seeklogo-351921.png` (320x320 palette PNG, transparent, artwork only 288x87 px). Processed copy: crop to bbox + 4x Lanczos + light unsharp -> `hf/edit30/assets/logo.png` (1216x412). Keep it small on screen (130 px tall in the opening above "$0", 64 px above the L9 headline) so it stays sharp; brand red reads well on the black base.

## Render gotcha: corrupt frame cache after killing a render
- Killing a HyperFrames render mid-run leaves a partial video-frame cache in `/tmp/hyperframes-extract-cache-*`. The next render reports `extract 0.0s` and silently shows BLACK where the presenter video should be (only the first ~1 s was fine). After any killed/aborted render run `rm -rf /tmp/hyperframes-extract-cache-*` before rendering again, and ALWAYS look at frames from the final file (presenter visible in full AND split layouts) before mixing/sending.

## Root cause of the "presenter vanishes after 1 s" bug (v10-v13)
- `#world` (the push-zoom wrapper) had no CSS because a later CSS-block replacement in `template.tpl` (`t[a:b]` from "/* L9 ..." to the first "#vig{") silently deleted the `#world/#leak/.lk*/#lkflash` rules. A transformed element becomes the containing block for absolute children, so a zero-size `#world` collapsed `#vframe` (inset:0) to nothing the moment the first push-zoom fired.
- Rules: (1) never slice template CSS by index across blocks without asserting every neighbouring rule still exists afterwards (`assert "#world{" in t`); (2) after any template change take a `snapshot --at` with the presenter in full AND split layouts (e.g. 1.5, 5.5, 7.0, 14.0, 16.0) BEFORE rendering; (3) verify frames of the final render, then mix audio.
