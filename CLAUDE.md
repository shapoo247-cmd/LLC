# LLC video edit: project brief

## Goal
Edit `footage/raw_footage_1.mp4` into a finished video whose motion graphics and overall editing **beat** the reference `reference/sample_llc_1.mp4`. The reference is the quality floor, not the target.

## Files
| File | What it is | Specs |
|---|---|---|
| `footage/raw_footage_1.mp4` | Raw footage to edit | 1920x1080, 30 fps, H.264 + AAC, 2:24 (144 s) |
| `reference/sample_llc_1.mp4` | Sample edit showing the style to surpass | 1920x1080, 30 fps, H.264 + AAC, 1:18 (78 s) |

GitHub rejects files over 100 MB, so the videos are committed as <50 MB parts in `footage/parts/` and `reference/parts/`. **Run this first in every new session:**

```
bash setup.sh
```

It rebuilds `footage/raw_footage_1.mp4` and `reference/sample_llc_1.mp4` and checks them against `SHA256SUMS`. The rebuilt full files are git-ignored. Don't commit them.

## Suggested first steps
1. Break down the reference: pull frames (e.g. `ffmpeg -i reference/sample_llc_1.mp4 -vf fps=1 ref_frames/%03d.png`), then note its graphic types, text animation, transitions, color, pacing and sound design.
2. Transcribe the raw footage and mark the beats: hook, key points, CTA.
3. Plan the edit beat by beat: where each motion graphic, caption, zoom, b-roll and SFX goes. Every element should be a step up from the reference.
4. Build, render and review against the reference side by side.

## Conventions
- Final renders: 1920x1080, 30 fps, H.264 MP4 into `renders/`. Do not commit any file over 100 MB. To keep a large render in git, split it the same way (`split -b 45M -d -a 2`).
- Git LFS uploads are blocked from the cloud workspace, so don't use LFS.
- Keep intermediate frames and scratch files out of git (see `.gitignore`).
