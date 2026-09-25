# What is OpenStreetMap (OSM)?

> English: OpenStreetMap · Etymology: English open + street + map

**Category:** Data  
**Last updated:** 2026-09-22

OpenStreetMap (OSM) is a free, collaborative, and open-license geographic database of the world, built and continuously updated by millions of volunteer mappers, civic contributors, and open-source cartographers.

## Definition and Etymology
Founded in 2004 by Steve Coast in response to restrictive proprietary map licensing, OpenStreetMap is often called the Wikipedia of cartography. Unlike commercial mapping providers that restrict underlying spatial data behind subscription paywalls and API meters, OSM distributes raw geographic vector data freely under the Open Database License (ODbL).

## Everyday Context and Practical Usage
Pervasive practical applications of OSM across tech:
- **Mobile Navigation Apps:** Privacy-respecting offline navigation tools like OsmAnd, Organic Maps, and MAPS.ME run entirely on OSM downloads.- **Tech Platforms:** Apple, Strava, Niantic, and Mapbox incorporate OSM geographic layers into consumer apps.- **Humanitarian Relief:** The Humanitarian OpenStreetMap Team (HOT) rapidly maps disaster zones following earthquakes and floods to guide rescue teams.

## Technical Depth and Architecture
The core data model of OpenStreetMap consists of three fundamental primitives:
- **Node:** A single geographic point defined by latitude and longitude coordinates (e.g. a bench, tree, or traffic light).- **Way:** An ordered list of nodes forming either an open polyline (a street, river, or hiking trail) or a closed polygon (a building footprint or park).- **Relation:** Groupings of nodes and ways modeling complex spatial constructs such as bus routes, turn restrictions, and multipolygon boundaries.- **Key-Value Tagging:** Universal semantic metadata attributes (e.g. highway=primary, maxspeed=50, building=yes).

## Cross-Disciplinary Perspectives
Parallels in other collaborative knowledge endeavors:
- **Encyclopedias:** The open crowd-sourced authoring and editorial review model of Wikipedia.- **Open Source Software:** The Linux kernel development ecosystem uniting hobbyists and multinational tech corporations.- **Citizen Science:** Crowd-sourced astronomical sky surveys and bird migration tracking networks.

## Analogy
It is like the Wikipedia of world maps; anyone can spot a new walking trail, fix a misspelled street name, and contribute local knowledge so that the entire globe enjoys a continuously refined, community-owned atlas.

## Frequently Asked Questions

**Is OpenStreetMap completely free to use?**  
Yes; the data is distributed under the Open Database License (ODbL), which allows free commercial and private usage as long as attribution is given.

**How does OSM maintain data quality without full-time cartographers?**  
Through community peer review, automated validation linters, and changeset monitoring tools that catch vandalism and mapping errors rapidly.

**Can developers host their own OSM tile server?**  
Yes; open-source toolchains (PostGIS, Mapnik, Osmosis) allow companies to self-host mapping infrastructure and eliminate commercial API costs.

**What distinguishes OSM from Google Maps?**  
Google Maps provides a closed proprietary service with usage meters; OSM provides raw spatial vector data that you can download, query, and modify freely.

## Related terms
- [Data Pipeline](/en/dictionary/data-pipeline/)
- [Open Source](/en/dictionary/open-source/)
- [API](/en/dictionary/api/)

---
Source: TreScout Tech Dictionary · https://trescout.com/en/dictionary/openstreetmap/
