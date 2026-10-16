# Design system (approved). Source of truth: `hf/edit30/template.tpl` (324 lines of HTML/CSS/GSAP). Copy patterns from it.

## Canvas, fonts, colours
- 1920x1080. Fonts: Inter Display 500/600/700 (OTF files in `hf/edit30/fonts/`, loaded with `@font-face`; also Inter for canvas text if needed).
- Base `#000`. Text `#f5f5f7`, secondary `#a1a1a6` (`--g`). Accents: green `#30d158` (gradient `#8dffb0`->`#30d158`, = free/good), orange gradient `#ffd60a`->`#ff453a` (= price/warning), amber `#ffb340`/`#ff9f0a`, blue `#0a84ff`/`#64d2ff`, purple `#bf5af2`, red `#ff453a`, switch-off grey `#39393d`. Brand red from the logo.
- Gradient text: class on EACH inline-block word span (`.grn .org .wht`), with right padding. Never on the line container (the "$0" glyph got clipped / broken).
- Type: headlines weight 600, letter-spacing -.035em, line-height 1.02. Hero numerals 700, -.06em, 470-620 px. Two-line headline pattern: line 1 grey 58-62 px, line 2 white-gradient or orange 108-132 px.
- Glass: `background rgba(255,255,255,.08); backdrop-filter blur(50px) saturate(180%); border 1px rgba(255,255,255,.14); border-top-color rgba(255,255,255,.3); box-shadow 0 40px 120px rgba(0,0,0,.5), inset 0 1px 0 rgba(255,255,255,.15)`. Radii 36-64 px.
- Pills over footage (`.pillD`): `rgba(12,12,16,.86)` + 1px `rgba(255,255,255,.22)` border, white 42 px text, 18/34/18/22 padding, in lane `#lane*` (left 40, width 660, vertically centred ~y 420-540).
- Background glows: 6 blurred radial orbs (`.o1-.o6`), pair per scene (blue/purple, orange/red, green/teal), static, crossfade 0.5 s between beats. No drifting.
- Soft vignette overlay `#vig` radial 62% -> rgba(0,0,0,.35). Do not add another vignette to the footage.

## Layout modes (JS `ST` table in template)
| mode | presenter | background | notes |
|---|---|---|---|
| `full` | `#vframe` clip FULL, x0 y0, `#shade` top/bottom gradient on | none | slow push-in (scale 1 -> 1.05 over the interval, `#vp`), alternate punch-in 1.0/1.12 per jump cut (`#vz`, origin 58% 0%) |
| `split` | CARD `inset(90px 70px 90px 1130px round 48px)`, vclip x=330,y=90 (source y=0 at card top, head in frame), `#cring` shadow | `#sbg` black + orbs | graphic zone `.lz` left 60 width 1010 height 900 (centre x=565) |
| `fs` | opacity 0 (voice continues) | `#sbg` | graphics `.lz.fs` full width (centre x=960) |
- Presenter face at full frame: x 1000-1300, y 150-520 (she sits right of centre). Free lane left of x=700.
- Hold a layout >= 1.5 s. Typical rhythm in the approved 28 s: full 0-1.55, fs 1.55-2.93, split 2.93-5.62, full 5.62-7.37, fs 7.37-12.35, split 12.35-14.3, full 14.3-18.4, fs 18.4-20.49, split 20.49-26.05, fs 26.05-end.

## Transition = light leak (the owner's chosen transition)
Code: `C.modes.forEach(([m,T,kind]) => ...)` in the template.
- At the cut instant `T` everything switches with `tl.set` (instant). Cut time = first frame of the incoming graphic (or last of the outgoing).
- Leak `#leak` (screen blend, layers `.lk-a` amber, `.lk-r` red, `.lk-g` gold, from registry block `organic-light-leak-overlay`, re-timed): opacity 0 -> peak over `up` (major 0.28 s, minor 0.20 s) ending ON `T`, then burns off (0.62 / 0.45 s). Peak major .82, minor .55. Layers sweep 0.95 s, direction alternates (`d=+-1`).
- Push-zoom `#world`: scale 1 -> 1.07 (major) / 1.035 (minor) before `T`, back to 1 after (0.55 s, power3.out). `#world` MUST have CSS (position absolute, inset 0).
- Major = any cut that brings the presenter in/out of full frame; minor = split <-> fs. White flash `#lkflash` (.32, 0.07 s) on major only.

## Motion tokens
- `LEAD = .17` s: start every reveal this much before the word. Enters 0.55-0.6 s `power4.out`; moves `power3.inOut`; exits 0.25-0.3 s `power2/3`. Nothing bounces.
- `mk(sel, lines, t0)`: builds mask-line headline; each word span `yPercent 118 -> 0, opacity 0 -> 1` at its own word time minus LEAD. Lines `[{size, cls, w:[[text,time],...]}]`; times are mapped (edit-timeline) seconds. `outEls(els,t)` exits upward.
- `pop(sel,t,{y,scale,x})`: scale .95 -> 1, y 26 -> 0, opacity.
- `ring(x,y,color,t,scale=2.2)`: shockwave circle on the big hits; MUST start hidden (`immediateRender:false`, CSS opacity 0).
- Count-up: tween a plain object, write text in `onUpdate` (deterministic). Pulse the number (scale 1.06) when it lands.
- Line chart: `getTotalLength()`, dash offset tied to progress `p` (`power2.in` = accelerating climb, builds suspense), dot via `getPointAtLength`, label rides the dot (keep inside the panel using `offsetWidth`), colour green -> amber -> red, ring at the top.
- Cursor click, toggle switch (knob x -184, track -> #39393d), scale/seesaw, row cascades (stagger 0.042 s per row), dim-to-26% "never used" pattern: all in the template as examples.

## Scenes already designed (reuse / extend)
$0 hero + logo (fs) | browser window "Free formation" + cursor click on green button (split) | "Technically true" pill (full) | checkout receipt with live total count-up to $216 (fs, then split "no idea how") | "2 LLCs formed / Clicked through it myself" pills (full) | price line chart (fs) | auto-renewal toggle (split) | "worth it?" seesaw Features vs $216/yr (split) | the real services menu: three glass columns, 27 features, dims except "LLC formation" (fs).

## Studio grade (baked, `GRADE` in gen.py)
`curves=master='0/0.012 0.15/0.14 0.30/0.285 0.45/0.425 0.55/0.575 0.70/0.725 0.85/0.84 0.95/0.925 1/0.97',colorbalance=bs=0.01:rm=0.012:bm=-0.012:rh=0.008:bh=-0.008,vibrance=intensity=0.08,eq=saturation=1.0` applied after the concat. Matches the media-treatment "Natural Portrait" tuned values (skin-soft .72, exposure +.08, contrast +.08, highlights -.18, shadows +.12, whites -.08, blacks -.04, temp +.04, vibrance +.06). The realtime shader grade is correct but renders ~15 s/frame on this machine: never use it for the full render. Compare original/graded/reference face crops before rendering.

## Assets
- Logo: `hf/edit30/assets/logo.png` (processed: crop + 4x Lanczos + unsharp; source only 288x87 px). Keep it small (130 px tall opening, 64 px menu) so it stays sharp.
- Site content for graphics comes from the owner's screenshots; restyle it in our system, never copy their branding.
