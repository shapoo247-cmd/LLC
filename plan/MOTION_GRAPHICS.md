# Motion graphics spec (raw-footage timecodes)
Word-level timings: `plan/words_raw.json` (Whisper small; verify before final). Reference duration of this same script was 78 s; our cut targets ~100 s for 0–143 s of raw.

## Cut list (do first; graphics are timed to the cleaned timeline)
| Remove raw | Why |
|---|---|
| 0.0–11.5 | dead air before speech (keep 0.3 s breath) |
| 29.7–41.4 | 11.7 s dead gap/false start before "I've formed two" |
| 43.0–44.0 | repeated "I've formed two, I've" stutter, keep one take |
| 63.5–66.5, 84.1–86.7, 109.0–110.4, 112.5–114.5 | pauses >2 s; trim to 0.35 s |

## Global system
- Base: deep violet gradient + soft vignette. Accents: **mint #3DDC97** = free/$0/good, **amber #FFB547** = money climbing/warning, **lavender #B9A6FF** = highlighted caption word. White text, condensed bold, ≥64 px, 90 px safe margin, left third for captions, hero 3D object right two-thirds.
- Camera on every scene: slow 3% push + 2° parallax tilt; shadows on the pedestal; no static frame >1 s.
- Captions: word-timed, active word scales 1.0→1.08 and turns lavender; line-by-line mask reveal, 6-frame ease-out. Exit: 4-frame wipe toward the object.
- Entrances 10–14 frames (spring, 8% overshoot). Hard match-cuts between graphic and talking head on a downbeat, whoosh 3 frames before.
- Talking-head tiers: A 100 % slow push to 106 %; B 118 % crop on eyes/hands. Alternate every 5–9 s, never during a graphic.
- Persistent tracker top-left from 47.5 s: three pills **Price · Setting · Worth it**, fill as each is delivered.
- Audio: music bed -24 LUFS under voice, ducked 6 dB; SFX list per scene below.

## Scenes
| # | Raw in–out | Spoken | Visual | Motion detail | SFX |
|---|---|---|---|---|---|
| 1 | 11.8–14.5 | "Taylor Brands advertises a $0 LLC" | Price tile on pedestal, "$0" in mint with LLC FORMATION; brand wordmark text only (no logo recreation until a licensed asset is supplied) | tile drops in, "$0" counts up from "$", light sweep | thud |
| 2 | 14.9–17.5 | "Free formation, big green button, sign up right now" | Browser window, cursor glides to green button, click | cursor eases, button depresses, ripple | click, ping |
| 3 | 17.5–19.5 | "technically that's true" | Shield with check, rotates 180° to show a small crack/"*" on the back | flip on "true" | chime→glass tick |
| 4 | 22.9–27.0 | "finish checkout… number closer to 200 bucks a year" | Receipt scrolls; line items stack; total ticks $0→$216 in amber; cart and coins enter | count-up synced to "200", total shakes at landing | register ka-ching, rising riser |
| 5 | 27.0–29.7 | "no idea how I got there" | Question mark + magnifier circling the total | magnifier sweep | soft whoosh |
| 6 | 43.9–45.2 | "formed two businesses" | Over-head chip "2 LLCs formed" (talking head stays) | chip pops from lower third | pop |
| 7 | 47.5–50.0 | "where that price climbs" | Bar chart $0→$200, tag swings from rope | bars rise left-to-right with words; arrow draws | stepped risers |
| 8 | 50.0–52.9 | "the one setting you have to switch off before you pay" | Add-ons Auto-Renewal toggle; ON glows amber, then flips OFF mint | flip on "off"; lamp dims | switch click |
| 9 | 53.3–55.2 | "whether it's actually worth it" | Balance scale: check vs $ | scale tips back and forth, settles level | creak |
| 10 | 55.2–58.2 | "pile of features you'll never touch" | Box overflowing with icons; clipboard + piggy bank, unchecked boxes | icons pop out, fall back | whoosh, coin |
| 11 | 58.7–63.5 | "fee nobody warns you about shows up on step four, I'll name it" | Stepper 1-2-3-**4**; steps 1–3 tick, step 4 pulses amber "?" with redacted bar | redaction bar slides in on "name it" (payoff later) | ticks, low sting |
| 12 | 66.5–69.9 | "what makes Taylor Brands different" | Title card "What Tailor Brands Actually Is" on brand-violet, not white; 3D spheres behind but behind text | letters stagger 2 f | whoosh |
| 13 | 72.8–84.1 | "all-in-one platform… logo maker, website builder, cards, social tools" | Hub with orbiting icons; each icon docks in as named (formation, AI logo, website, cards, social) | orbit ring draws, icon labels slide | tick per icon |
| 14 | 76.0–80.0 (b-roll over voice) | alt of #13 or insert | Real screen capture of service grid, 2× zoom, highlighted card tracking | needs fresh high-res capture | UI blips |
| 15 | 86.7–93.0 | "one login, one dashboard… registered business and a brand" | Dashboard mock builds: login → dashboard → business card + logo | UI panels float in | whoosh |
| 16 | 96.7–101.7 | "bakery, cleaning service, Shopify store, logo matters" | Four mini-scenes: bakery, spray bottle, shop on laptop, logo orbit | 1.2 s each, swap on noun | per-noun pop |
| 17 | 102.2–105.5 | "juggling five different tools" | 5 app tiles collapse into one | tiles magnetise on "one place" | whoosh→click |
| 18 | 105.9–108.1 | "that's also where the price hides" | Bundle box; amber price tag peeks from behind | tag slides out | creak sting |
| 19 | 114.7–122.0 | "free plan gets you the LLC filing, that's it… state fee" | Document with "LLC FILED" stamp, "$0", then "+ STATE FEE" slides in amber | stamp slam | stamp |
| 20 | 122.5–132.5 | "That's the government… CA $70, TX $300, KY $40" | US map, pins at CA, TX, KY; numbers count up as each state is said; "Set by your state, not Tailor Brands" | pin drop on state name | drop ×3 |
| 21 | 133.4–143.1 | "EIN, registered agent, operating agreement" | Three checklist cards stack; each gets "NEEDED?" chip | card per phrase, last lands on 143 | card slap ×3 |
| 22 | 143.1–end | cliffhanger | Stepper #11 returns with step 4 blinking, "Next: the fee nobody warns you about" | | riser, cut |

## Open questions
1. Logo: use text wordmark or licensed Tailor Brands asset?
2. Do we get more footage (step 4, verdict, CTA)? Scene 22 is a placeholder.
3. Fresh screen captures of the signup flow for #2, #14 (needs the user to supply or to run a capture).
4. Music/SFX source.
