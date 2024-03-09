#!/usr/bin/sh

strip_video () {
        duration=$(ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "$1")
        end_time=$(python -c "print($duration - $4)")
        ffmpeg -i $1 -ss $3 -to $end_time -c copy $2
        
}

if [[ "${#BASH_SOURCE[@]}" -eq 1 ]]; then
  strip_video "$@"
fi
