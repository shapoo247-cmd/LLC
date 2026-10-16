# Owner feedback log (newest rules win; superseded ones are marked)

The owner reviewed ~14 versions. Everything below was learned the hard way. Apply it from the first build.

## Style and structure
1. **Own style, not a copy.** Do not recreate the reference's purple clay 3D objects on pedestals. Direction chosen: Apple keynote (black base, big type, glass, soft glows). Procedural Three.js "3D" attempts were judged too flat; the ledger/lime style was dropped; Apple style approved.
2. **Mix three layouts**: full-frame presenter, full-screen animation, and both at once (presenter card + graphic). Alternate them; do not cover the presenter with full-screen takeovers for most of the runtime.
3. **No captions at the bottom** (owner removed them). SUPERSEDED: "keep captions running".
4. **Everything centred.** Full-screen graphics centred on the screen (x=960, y=540); in split layout centred in the left zone (x=565, y=540). Left-aligned graphics were rejected.
5. **Presenter head fully in frame.** The card must start at source y=0 (her hair touches the top of the source frame). Never crop the head.
6. **Never put graphics on her face or head.** Overlay pills/chips go in the free left lane (x 40-700, mid height), dark and high-contrast (owner: "pills same colour as the model background, put in the middle not below").
7. **Opening**: show her for a real beat (>= 1 s, slow push-in) then cut. The owner hated "she appears for 2-3 frames then suddenly fades". Never fade her out while she is talking. SUPERSEDED: shrink/dock layout morphs (owner: "not professional").
8. **Transitions between presenter and animation**: hard cut hidden under a LIGHT LEAK with sound (see design-system.md). Only this.
9. **Emotion / suspense**: not "emotionless and motionless". Build tension (dark, slow push-in, a rising riser), a beat of near-silence, impact on the big reveals ($0, $216) with a shockwave ring, relief chord when solved (switch off). Pacing and sound carry it.
10. **Better hooks on weak scenes.** 0:19 price scene was rebuilt as an accelerating line chart; 0:27 "pile of features" scene was rebuilt from the real services menu (owner screenshot) with all 27 features, dimming to "LLC formation". When the owner says an animation is weak, redesign it, do not tweak it.
11. **Use real brand assets/content when supplied**: the Tailor Brands logo (repo root `tailor-brands-logo-png_seeklogo-351921.png`) and the real site menu. Never redraw a brand logo by hand; ask for the file.

## Motion
12. **Sync = the visual peak lands ON the spoken word**: start 0.17 s early. Verified with earshot (median sound-to-cue 23-30 ms).
13. **No bounce / overshoot on enters**, no springs with oscillation (read as "jittering"). Use ease-out-quint/quart for enters, ease-in-out for on-screen moves, scale from ~.95, blur <= 10 px. SUPERSEDED: "springs with controlled overshoot".
14. **Smooth like butter**: render the master at 60 fps (30 fps looked steppy); deliver a 30 fps motion-blurred copy too. Remove ambient drifting backgrounds (peripheral motion).
15. **Real motion design**, not fades: per-word kinetic headlines (words rise through a mask), staggered reveals, count-ups, draw-on lines.

## Colour
16. **Studio colour grade on the presenter**: natural, polished (warm skin, richer contrast, soft highlights). Too orange and too milky were both rejected; no extra vignette (it stacked with the overlay vignette and was too dark).

## Sound (most revisions here)
17. Sound must feel like Apple UI sounds and be restrained: "professional, not sfx heavy". SUPERSEDED: synthetic tones, Kenney samples (kept only as fallback), iPhone "message sent" swish (rejected by owner).
18. Owner sources: folder `Apple ui/` (on repo `main`) and the three uploads RH-SWOOSH3 (swoosh on cuts), RH-CAMERA4 (camera click on rare cuts), RH-RISER (ONE riser, at the start; "1 time is enough"). Details in sound.md.
19. Fire sounds when the visual lands. Camera click: owner said "too much" at one per cut; now only two in 28 s.

## Process
20. Owner wants everything saved so no day is wasted: this skill. Owner reviews each version and gives feedback; fix ALL points in one pass, deliver 60 fps + 30 fps, tell them honestly what was and was not verified.
21. Owner prefers HyperFrames (not vidIQ). Use available skills (motion-design, apple-design, media-use, hyperframes) instead of improvising.
22. Owner's files arrive via the repo (`main` branch) or `/root/.claude/uploads/`. Images pasted in chat are NOT on disk; ask them to push the file.
23. Final render for download: 1920x1080, 60 fps, H.264 + AAC.
