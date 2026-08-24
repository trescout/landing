# Early-access interaction measurement contract

## Status

This document defines a **local, opt-in-ready event contract** for homepage interaction work. The current implementation does not send events to an analytics provider, does not write to storage, does not set cookies, and does not add the early-access email consent to any analytics consent. A future analytics implementation must be approved separately together with its privacy notice and consent design.

## Transport boundary

Homepage interactions dispatch `CustomEvent('trescout:interaction')` on `document`. A listener may inspect the event during the current page session, but the current landing code does not register a listener that sends data anywhere. The event detail contains only the event name and non-identifying UI context. It never contains an email address, free text, IP address, browser identifier, or user-provided personal data.

The catalog fetch used by the radar and daily-flow preview is a same-origin read of `/assets/discover/catalog.json`. It is content loading, not measurement, and it does not call `/api/subscribe` or any email/delivery service.

## Event names

| Event name | When emitted | Current payload |
|---|---|---|
| `report_tasting_view` | Report tasting initializes | `language` |
| `report_tasting_tab` | A report tasting tab is activated | `language`, `tab` |
| `report_tasting_source_click` | A report tasting link is clicked | `language` |
| `discovery_radar_view` | Radar catalog finishes loading | `language`, `count` |
| `discovery_radar_filter` | A radar filter is activated | `language`, `filter` |
| `discovery_card_click` | A rendered discovery card link is clicked | `language`, `slug` |
| `discovery_radar_cta` | The radar early-access CTA is clicked | `language`, `filter` |
| `daily_flow_view` | Daily-flow preview initializes | `language` |
| `daily_flow_catalog_loaded` | Daily-flow catalog finishes loading | `language`, `count` |
| `daily_flow_preview_rendered` | The three-step preview is rendered | `language`, `topic`, `time`, `count` |
| `daily_flow_topic_select` | An example topic is selected | `language`, `topic` |
| `daily_flow_time_select` | An example time is selected | `language`, `time` |
| `daily_flow_cta` | The daily-flow early-access CTA is clicked | `language`, `topic`, `time` |
| `daily_flow_error` | The daily-flow catalog cannot be loaded | `language` |

## Interpretation rules

These events are interaction hooks, not proof of conversion or user identity. A future funnel report must distinguish page views, interaction events, and successful early-access submissions. A successful submission remains defined by the existing `/api/subscribe` contract and must not be inferred from a CTA click or from the daily-flow example controls.

Any future network measurement must be implemented only after an explicit product and privacy decision. The existing email-processing checkbox is not analytics consent, and no implementation may silently reuse it for behavioral measurement.
