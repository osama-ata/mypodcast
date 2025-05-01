---
title: "Episode {{ replaceRE `.*e([0-9]+)` `$1` .Name }}"
author: "Osama Ata"
date: {{ .Date }}
type: "episodes"
description: "Add description"
itunes_summary: "Add itunes_summary"
audio_file: "https://audio.podcast.osamata.com/{{ .Name }}.mp3"
audio_length: 0
duration: "00:00"
explicit: "no"
season: {{ replaceRE `.*s([0-9]+).*` `$1` .Name }}
episode: {{ replaceRE `.*e([0-9]+).*` `$1` .Name }}
episode_type: "full"
image: "https://podcast.osamata.com/images/{{ .Name }}.png"
keywords: []
---