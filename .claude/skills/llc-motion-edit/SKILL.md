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
