# Plan for the REMAINING footage (raw 58.3 s -> 143.1 s)

Done and approved (raw 11.77 -> 58.18 s, edit 0 -> 28.45 s): hook ($0 claim, sign-up button, "technically true", checkout $216, "no idea how", credibility pills, price chart, auto-renewal toggle, "worth it?", pile-of-features menu). Do NOT redo those; extend the same system. Whole transcript: `plan/transcript_raw.txt`; word times: `plan/words_raw.json`; older broad plan: `plan/PLAN.md`, `plan/MOTION_GRAPHICS.md` (its look is superseded by design-system.md; its beats still useful).

## Script, raw timecodes (Whisper small; verify words before anchoring)
| raw | line |
|---|---|
| 58.7-63.5 | "Stick around because the fee nobody warns you about shows up on step four, and I'll name it." (OPEN LOOP: pay it off only if later footage names the fee; the footage ends before the reveal) |
| 66.5-69.9 | "Here's the thing that makes Taylor Brands different from a plain formation service." |
| 70.3-72.3 | "It's not just a company that files your paperwork." |
| 72.8-84.1 | "It's an all-in-one platform. You get LLC formation, sure, but you also get an AI logo maker, a website builder, business cards, social media tools, the whole branding kit bundled into one subscription." |
| 86.7-93.0 | "That's the pitch. One login, one dashboard, and you walk out with a registered business and a brand that looks like you spent real money on it." |
| 93.5-96.1 | "For a certain kind of person, that's genuinely appealing." |
| 96.7-101.7 | "If you're launching a bakery, a cleaning service, a Shopify store, anything where the logo actually matters," |
| 102.2-105.5 | "having it all in one place saves you juggling five different tools." |
| 105.9-112.2 | "But that bundle is also where the price hides. Let me walk you through it." |
| 114.7-122.0 | "The free plan gets you the LLC filing itself, and that's it. You still pay your state fee on top, always, no matter which service you use." |
| 122.5-132.5 | "That's not Tailor Brands. That's the government. In California, that's $70. In Texas, it's $300. In Kentucky, it's $40. Your state sets that number and nobody can make it disappear." |
| 133.4-143.1 | "Now, the free plan sounds great until you try to check out. To actually run a legal business, you need an EIN from the IRS. You probably want registered agent service, and you'll want an operating agreement." (footage ends here) |

## Cut notes
Pauses > 0.4 s are cut by the existing merge rule: gaps at ~63.5-66.5, 84.1-86.7, 109-110.4, 112.5-114.7 collapse automatically. Expect about 85 s of edit for raw 58-143 s => total about 113 s. Inspect the join at 58.18 -> 58.68 (the approved ending "...you'll never touch." must still land on a clean beat).

## Suggested scenes (same modes/rhythm; hold each layout >= 1.5 s; only ~4 big hits)
1. 58.7-63.5 Teaser (fs): 4-step stepper 1-2-3-**4**; steps 1-3 tick, step 4 pulses amber "?" with a redacted bar sliding in on "I'll name it". Open loop, no sound except one soft tick; NO new riser.
2. 66.5-72.3 Chapter (split or fs): logo + "What Tailor Brands actually is" as kinetic two-line headline in our palette (not white bubbles).
3. 72.8-84.1 Platform (fs): hub with five service tiles docking as named (formation, AI logo maker, website builder, business cards, social media tools); reuse the glass row/icon style from the menu scene; end with the tiles merging into one "subscription" card. Optional: real site capture if the owner supplies one.
4. 86.7-93.0 One login, one dashboard (split): dashboard mock (login field -> dashboard grid -> "registered business" check + logo tile).
5. 93.5-101.7 Who it suits (full presenter for 93.5-96.7, then fs on "bakery / cleaning service / Shopify store / logo"): four icon tiles swapping on each noun, ending on the logo.
6. 102.2-105.5 "five tools into one" (fs): five app tiles collapsing into one card.
7. 105.9-112.2 "that's where the price hides" (fs/split): price tag peeking out from behind the bundle card, then cut to presenter on "Let me walk you through it" (major cut with leak; presenter full frame >= 1.5 s).
8. 114.7-122.0 Free plan = filing only (fs): document stamped "LLC FILED $0", then "+ STATE FEE" slides in amber.
9. 122.5-132.5 State fees (fs, hero scene): US tile map; California $70, Texas $300, Kentucky $40 pin and count up on each state word; caption "Set by your state, not Tailor Brands". Big hit here (impact + ring), maybe the only camera4 in this half.
10. 133.4-143.1 Checkout reality (split): three glass cards stack (EIN, registered agent, operating agreement) with "needed?" chips, last card lands on the final word; hold the last frame.
11. End: footage stops mid-argument. ASK the owner: end on the step-4 cliffhanger card, or supply more footage / CTA. Do not invent claims or numbers (prices for EIN etc. are not in the footage).

## Rules for facts
- Only show numbers and names the presenter says or the owner supplied: $0, $200/yr, step four, state fees CA $70 / TX $300 / KY $40. The checkout rows ($149 add-ons, $67 renewal, $216) in the approved hook are illustrative of the "~$200" claim (owner accepted).
- Feature names in the menu scene come from the owner's site screenshot.

## Estimated effort (so the day is not wasted)
Scenes 1-10 are variations of components already built (mk headline, glass cards, rows cascade, count-up, ring, line chart, switch). Budget: build all scene HTML/JS in one pass, one snapshot review pass, fix, one 60 fps render (~25-30 min, background), frame check, mixdown, send. Avoid repeated full renders: use snapshots to iterate.
