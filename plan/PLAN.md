# Plan: motion graphics for raw_footage_1 (144 s)

## 1. Reference breakdown (sample_llc_1.mp4, 78 s)
The reference is a cut of the first ~78 s of the *same script* as the raw footage. It starts at raw 10.4 s (dead air before that).

| Element | What it does | Weakness to beat |
|---|---|---|
| Visual language | Lavender/purple 3D "clay" icons on a pedestal (price tile, browser+cursor, shield, checkout+cart, question mark+magnifier, bar chart+tag, toggle, scales, box, clipboard+piggy bank, bakery, shopify, logo orbit) | One flat purple palette, no accent colour; every scene is the same pedestal composition |
| Text | Left-aligned condensed caps, 3–4 lines, key word highlighted in lighter purple or a highlight box | Static, small, low contrast on light scenes (e.g. checkout copy is tiny), no per-word sync visible |
| Structure | ~13 full-screen graphic cutaways, each 2–6 s, alternating with talking head. Hook (0–28 s) is nearly all graphics; 28–38 s talking head; 38–78 s mixed | Talking head is never reframed (no punch-ins), so long stretches are visually flat |
| Screen recording | 4 s of the Tailor Brands site with logo pop-up, signup flow, service grid with yellow highlight boxes | Low-res, fully greyed/vignetted, no zoom or callout tracking |
| Chapter card | White bubble "What Tailor Brands Actually Is" (~35 s) | Off-palette, tracking too wide, bubbles cross the text |
| Transitions | Hard cuts, a few soft dissolves (scene changes at 13.8, 18.7, 28.1, 33.3, 38.5, 42.3, 56.5, 65.9, 74.6 s) | No whoosh/impact motion matching |
| Sound | Voice only measured: mean -20 dB, peak -0.4 dB. No silence gaps detected, so no audible music bed or SFX is evident | No sound design at all: our biggest easy win |

## 2. Raw footage beats (speech starts 10.5 s)
| Raw time | Beat | Content |
|---|---|---|
| 10.5–26 | HOOK | "$0 LLC" claim, big green button, "technically true", checkout ~$200/yr, "no idea how I got there" |
| 26–44 | Dead gap/stutter | Long pause plus "I've formed two, I've formed two": tighten, keep one take |
| 44–61 | PROMISE | Credibility; 3 things I'll show (where price climbs, the setting to switch off, is it worth it); fee on step four teaser |
| 61–107 | CONTEXT | All-in-one platform: formation, AI logo, website, cards, social; "launching a bakery / cleaning / Shopify" |
| 107–116 | Turn | "That's also where the price hides. Let me walk you through it." |
| 116–143 | KEY POINT 1 (new, not in reference) | Free plan = filing only; state fee always applies: CA $70, TX $300, KY $40; "the government, not Tailor Brands"; free plan breaks at checkout: EIN, registered agent, operating agreement |
| 143–144 | Footage ends mid-point | No CTA recorded; need an end card (see §4) |

Note: the transcript is from `small` Whisper (local). Re-check names/numbers before captions are final.

## 3. Graphic plan (every item needs a spec: duration, entrance, exit, SFX)
Design system: deep violet base, but add a **warm accent (amber/coral) for money and warnings** and a **mint green** only for "free/$0" and the Sign-up button. Real 3D lighting via rendered HTML/Three.js or Blender-style lighting, not flat PNGs. Caption font: condensed bold, minimum 64 px on 1080p, safe-area 90 px.

Rules to beat the reference:
1. Word-level kinetic text synced to speech (word-timestamp JSON), highlight key words as spoken.
2. Never hold a graphic longer than 4 s without secondary motion (parallax, number count-up, camera drift).
3. Talking head gets slow punch-in (100→108 %) and alternate 115 % cuts every 6–10 s so no stretch is static.
4. Graphics enter with a matched whoosh and land with a soft thud; low music bed ducked -18 dB under voice.
5. Persistent lower-third progress tracker ("Price → Setting → Worth it") that fills as the promised three points are covered.

| # | Raw time | Line | Graphic |
|---|---|---|---|
| 1 | 10.5 | "$0 LLC" | Price tile with $0 counting from "$" glyph; shard-in |
| 2 | 13.5 | "big green button, sign up right now" | Browser with cursor clicking the green button, button press + click SFX |
| 3 | 18.8 | "technically that's true" | Shield + check, then crack/flip to expose the catch (new beat) |
| 4 | 20.5 | "by the time you finish checkout… 200 bucks" | Receipt scrolling with line items; total ticks $0 → $216 in amber, cart + coins |
| 5 | 24.5 | "no idea how I got there" | Question mark + magnifier, brief |
| 6 | 44 | "formed two businesses" | Small credibility chip over head: "2 LLCs formed" (talking head stays) |
| 7 | 49 | "where that price climbs" | Bar chart $0→$200 stepping up in sync with words |
| 8 | 51 | "the one setting you switch off" | Add-ons Auto-Renewal toggle flipping ON→OFF with haptic SFX |
| 9 | 53 | "is it worth it" | Scale: check vs $ |
| 10 | 56 | "pile of features you'll never touch" | Box overflowing icons, clipboard + piggy bank |
| 11 | 59–61 | "fee on step four, I'll name it" | Stepper 1-2-3-**4** with step 4 pulsing amber "?" (open loop; pay off later) |
| 12 | 61.5 | chapter | "What Tailor Brands Actually Is" in brand palette, not white bubbles |
| 13 | 68–80 | platform list | Orbiting service icons; each appears as named (formation, AI logo, website, cards, social) |
| 14 | 76 | screen recording | Real site capture, 2× zoom and tracked highlight on the service grid, source-cropped at full res |
| 15 | 94–103 | bakery / cleaning / Shopify / logo | Three mini 3D scenes then logo orbit; same assets as the reference, rebuilt with better lighting |
| 16 | 104 | "saves you juggling five tools" | Five app icons collapse into one |
| 17 | 107 | "that's where the price hides" | Price tag peeking from behind the bundle, then cut |
| 18 | 116 | free plan filing only | Document stamp "LLC FILED" + "$0" |
| 19 | 121–131 | state fee | US map: CA $70, TX $300, KY $40 pins with number count-up; label "Set by the state, not Tailor Brands" |
| 20 | 135–143 | EIN, registered agent, operating agreement | Three checklist cards stack, each with price chip (amber, TBD from later footage) |
| 21 | 143+ | end | Placeholder end card, "Next: the step-4 fee" (replace once CTA footage exists) |

## 4. Gaps and risks
- Raw ends at 144 s mid-argument: no step-4 reveal, verdict or CTA. The edit cannot pay off the hook. Either request more footage or end on a deliberate cliffhanger card.
- Only a static camera: all variety comes from punch-ins and graphics (plan §3 rule 3).
- Reference has 3D assets we cannot copy; every graphic must be rebuilt (HTML/Three.js or Blender). Budget: ~21 scenes.
- Site screen recordings must be captured fresh (reference's are low-res).
- Music/SFX: need royalty-free sources or generated; none in the repo.

## 5. Proposed build path
1. Cut: trim 0–10.4 s, remove 26–44 s gap/stutter, mark jump cuts at pauses (ffmpeg + word timestamps).
2. Author graphics as HTML/GSAP compositions (HyperFrames skills or local Node/Playwright), render each to alpha-capable clips.
3. Compose in ffmpeg with punch-ins, captions and audio mix; render 1080p30 H.264 into `renders/`.
4. Review side by side against the reference frame by frame.
