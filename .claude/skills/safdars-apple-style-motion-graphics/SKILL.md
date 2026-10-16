---
name: safdars-apple-style-motion-graphics
description: Safdar's Apple style Motion graphics animation. A complete, reusable system for turning a talking-head video into a premium Apple-keynote-style edit with HyperFrames - black base, huge tight Inter Display type, frosted-glass cards, per-word kinetic text that lands on the spoken word, presenter/animation layout modes joined by light-leak transitions, studio colour grade, restrained Apple-UI sound design, 60 fps delivery. Use whenever Safdar asks for an Apple-style / keynote-style / premium motion-graphics edit, "do it in my style", or continues the LLC / Tailor Brands video. Contains the approved look, working code, sound rules, every correction already made, and every bug already hit.
---

# Safdar's Apple style Motion graphics animation

A battle-tested house style, refined over ~14 review rounds with Safdar on a real video (the LLC / Tailor Brands review). It is for talking-head footage with word-synced graphics, but the look, motion rules, sound approach and pipeline apply to any video. For the specific LLC project (file paths, transcript, remaining scenes) also read the `llc-motion-edit` skill.

## How to use this skill
1. Read `references/style-corrections.md` first. These are Safdar's rules; they override defaults and your taste.
2. Read `references/design-system.md` (tokens, layouts, transitions, motion) and `references/sound.md`.
3. Copy working code from `references/engine.md` (kinetic headline helper, layout engine + light leak, chart, menu cascade, count-up, ring, switch). Do not re-invent them.
4. Follow `references/pipeline.md` for setup, commands, timings and delivery. Check `references/gotchas.md` before debugging: most bugs are already listed with causes.
5. The full reference implementation lives in the repo at `hf/edit30/template.tpl` and `hf/edit30/gen.py`.

## The style in one screen
- Black base `#000`, Inter Display (600 headlines, 700 numerals), letter-spacing -.035em, hero numerals 470-620 px, two-line headlines (grey line + big white/orange/green gradient line).
- Frosted-glass cards, soft static colour glows, no drifting backgrounds, no bottom captions, everything centred.
- Three layouts: `full` presenter, `fs` full-screen animation (voice continues), `split` (presenter in a rounded card on the right, graphic on the left, her head fully in frame). Switches are hard cuts hidden under a light leak with a push-zoom, never fades or morphs.
- Every reveal starts 0.17 s before the spoken word so its peak lands on the word; per-word kinetic text; ease-out-quint, no bounce, no overshoot.
- Emotion: slow push-in, one riser, a beat of silence, an impact + shockwave ring on the big reveal, a relief chord when the problem is solved.
- Sound is restrained (about one cue per 1.7 s, Apple UI sounds + the owner's RH swoosh/camera/riser), loudness -16 LUFS.
- Studio colour grade on the presenter baked with ffmpeg; 60 fps master + 30 fps motion-blurred copy; 1920x1080 H.264 + AAC.

## Honesty and process rules
- Look at frames from the FINAL rendered file before sending (presenter visible in full AND split layouts). Say plainly what was verified (stills, frames, earshot numbers) and what was not (not watched at speed, not heard).
- Fix ALL feedback points in one pass. When an animation is called weak, redesign it. Ask for missing brand assets (logo, screenshots) as files; never redraw a brand logo.
- Save every new correction to `references/style-corrections.md` immediately.
- End of turn: commit + push to the working branch (a stop hook requires a clean tree), keep only the latest renders.
