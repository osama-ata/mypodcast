# 🎙️ My Podcast RSS

This is the RSS feed for the **My Podcast** show, built with [Hugo](https://gohugo.io/) and hosted via GitHub Pages + Cloudflare CDN.

## 🔗 Live RSS Feed

```
https://podcast.osamata.com/index.xml
```

## ✅ Podcast Submission Checklist

### 🔧 Pre-Launch

- [x] RSS feed validates ([CastFeedValidator](https://castfeedvalidator.com))
- [x] Audio files are hosted on a reliable CDN (e.g., Cloudflare, BunnyCDN)
- [x] Each episode includes:
  - `title`, `description`, `pubDate`
  - `<enclosure>` with valid `url`, `type`, `length`
  - `itunes:duration`, `itunes:explicit`
  - `itunes:image` (HTTPS, 1400–3000 px)

### 📝 Submit Feed To

- [Apple Podcasts](https://podcasters.apple.com/)
- [Spotify for Podcasters](https://podcasters.spotify.com/)
- [Amazon Music](https://podcasters.amazon.com/)
- [Pocket Casts](https://www.pocketcasts.com/submit/)
- [Overcast](https://overcast.fm/submit)
- [Podcast Index](https://podcastindex.org/add)

### 📦 Optional

- Add `robots.txt` or `humans.txt`
- Embed a web player (e.g., Podlove Web Player or Spotify embed)
