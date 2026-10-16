#!/bin/bash
# usage: mixdown.sh <picture master mp4> <out prefix>   (e.g. ../../renders/first30_apple_edit_v10_60fps.mp4 ../../renders/first30_apple_v10_final)
set -e
cd "$(dirname "$0")"
V="$1"; O="$2"
ffmpeg -v error -y -i assets/aroll.mp4 -i assets/sfx.wav -filter_complex "[0:a]volume=1[v];[1:a]volume=0.6[s];[v][s]amix=inputs=2:normalize=0:duration=longest,atrim=0:28.45[a]" -map "[a]" -ar 48000 /tmp/premix.wav
M=$(ffmpeg -hide_banner -nostats -i /tmp/premix.wav -af loudnorm=I=-16:TP=-1.5:LRA=7:print_format=json -f null - 2>&1 | python3 -c "
import sys,json
t=sys.stdin.read();j=json.loads(t[t.rindex('{'):t.rindex('}')+1]);print(':'.join(f'measured_{k}={j[\"input_\"+k]}' for k in ['i','tp','lra','thresh'])+':offset='+j['target_offset'])")
ffmpeg -v error -y -i /tmp/premix.wav -af "loudnorm=I=-16:TP=-1.5:LRA=7:$M:linear=true" -ar 48000 /tmp/final_audio.wav
ffmpeg -v error -y -i "$V" -i /tmp/final_audio.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 192k -t 28.45 "${O}_60fps.mp4"
ffmpeg -v error -y -i "${O}_60fps.mp4" -vf "tmix=frames=2:weights='1 1',select='not(mod(n,2))',setpts=N/30/TB" -r 30 -c:v libx264 -crf 16 -preset slow -pix_fmt yuv420p -c:a copy "${O}_30fps.mp4"
