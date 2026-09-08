# Fast and lightweight AI browser

Lightpanda is a headless browser written in Zig, specifically developed for AI and automation processes. It aims to accelerate web scraping and web automation tasks by consuming fewer resources compared to traditional browsers.

- ★ 35,072
- Zig
- GitHub Trending · 2026-09-08

## What you get
- Provides up to 16x less memory consumption compared to traditional browsers.
- Accelerates web scraping processes by processing web pages up to 9x faster.
- Offers AI agent support running directly within the browser.

## Installation
**macOS installation with Homebrew**

```
brew install lightpanda-io/browser/lightpanda
```

**Container setup with Docker**

```
docker run -d --name lightpanda -p 127.0.0.1:9222:9222 lightpanda/browser:nightly
```


## Running it
**Get web page as text**

```
./lightpanda fetch --obey-robots --dump html --log-format pretty  --log-level info https://demo-browser.lightpanda.io/campfire-commerce/
```

**Starting the CDP server**

```
./lightpanda serve --obey-robots --log-format pretty  --log-level info --host 127.0.0.1 --port 9222
```


## If you don't write code
You are a web automation expert. I want you to extract data from the specified website as efficiently as possible using the Lightpanda headless browser. Optimize memory usage, comply with robots.txt rules, and present the obtained data in a structured format. Dynamically adjust the necessary waiting times (wait-selector or wait-ms) to reduce the margin of error while performing the operation.

## Related dictionary terms

## Links
- GitHub repository →
- Read in Turkish →

---
Source: TreScout Discover · https://trescout.com/en/discover/browser/
