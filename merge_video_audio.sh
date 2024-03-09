#!/bin/bash

merge_video_audio() {
  # 获取文件名（不带扩展名）
  name="$1"

  # 合并视频和音频轨
  ffmpeg -i "${name}.mp4" -i "${name}.m4a" -c copy "${name}.merged.mp4"

  # 删除源文件
  rm "${name}.mp4"
  rm "${name}.m4a"

  # 重命名合并后的视频
  mv "${name}.merged.mp4" "${name}.mp4"
}

if [[ "${#BASH_SOURCE[@]}" -eq 1 ]]; then
  merge_video_audio "$@"
fi
