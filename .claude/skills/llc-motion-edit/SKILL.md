---
name: llc-motion-edit
description: Complete playbook for editing the LLC / Tailor Brands talking-head video (footage/raw_footage_1.mp4) into a finished Apple-keynote-style edit with HyperFrames - cuts, studio colour grade, light-leak transitions, motion graphics, owner-approved sound design, delivery. Contains the owner's approved style, every correction they have made, the exact pipeline, and every bug already hit. Read ALL of it before touching the edit; it exists so no time is wasted re-learning.
---

# LLC video edit: playbook

State at hand-off: the first 28.45 s (raw 11.7 s to 58.3 s) is finished and APPROVED in style (`renders/first30_apple_v14_final_60fps.mp4`, 1920x1080, 60 fps, plus a 30 fps copy). Remaining job: apply the SAME system to the rest of the footage (raw 58.3 s to about 143 s, the footage ends mid-sentence) and deliver one full video.

Read the references in this order, then work:
1. `references/owner-feedback.md` - every correction the owner made, newest rules win. Never repeat these mistakes.
2. `references/design-system.md` - the approved look: tokens, layouts, motion, component recipes (copy the code patterns).
3. `references/sound.md` - the approved sound design, exact files, offsets, loudness.
4. `references/pipeline.md` - fresh-session setup, file map, commands, timings, how to add a scene, how to scale gen.py to the full video.
5. `references/gotchas.md` - bugs already hit and their fixes (several cost hours).
6. `references/full-video-plan.md` - transcript, cut list and scene plan for the remaining footage.

## Non-negotiables (summary; details in owner-feedback.md)
- Style: Apple keynote. Black base, huge tight Inter Display type, soft colour glows, frosted-glass cards, ease-out motion with NO bounce. Not the reference's purple clay 3D. The reference only sets a quality floor.
- Three layouts: `full` (presenter full frame), `fs` (full-screen animation, voice continues), `split` (presenter rounded card right, graphic left). NO bottom captions. Everything centred (fs on x=960, split zone on x=565, y=540).
- Presenter and graphics are never faded in and out; layout switches are hard cuts hidden under a light leak (+ push-zoom). Never put graphics on her face/head. Presenter opens the video for >= 1 s.
- Every animation peaks ON the spoken word (start 0.17 s before). Per-word kinetic text, not whole-block fades. No bounce. 60 fps master + 30 fps motion-blurred copy.
- Sound: professional, NOT sfx-heavy. Owner's RH sounds + Apple UI folder only. ONE riser in the whole video (already used at the start), RH-CAMERA4 only on rare key cuts. About 1 cue per 1.7 s at most.
- Studio colour grade baked into the cut with ffmpeg (no realtime shader).
- Be honest: say exactly what you checked (stills, frames of the final file, earshot numbers) and what you did not (not watched at speed, not listened). Look at frames of the FINAL file before sending anything.

## Definition of done for each delivery
1. `check` passes; snapshots at lead-in/hit/settle of every beat looked at (presenter visible in full AND split layouts).
2. Render at 60 fps; frames of the rendered file inspected (12-frame contact sheet minimum).
3. `mixdown.sh` -> 60 fps final + 30 fps copy, loudness about -16 LUFS; earshot sync check.
4. Send both files (`SendUserFile`), state verified/unverified honestly, list anything open.
5. Commit and push to `claude/nifty-fermi-w9ften` (no PR unless asked). A stop hook demands a clean tree: commit everything or delete scratch files. Keep only the latest renders plus the newest picture master.
6. Append any new owner correction to `references/owner-feedback.md` BEFORE doing the next thing.
