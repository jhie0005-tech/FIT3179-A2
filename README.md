# Australian Public Art Collections

This repository contains introductory Vega-Lite maps for the FIT3179 assignment. They use the cleaned gallery data at `Data/processed/galleries_clean.csv` and `Data/processed/galleries_geocoded.csv`, plus the Brisbane public-art collection at `Data/public-art-brisbane-clean.csv`.

## Structure

```text
Data/                 source data and future processed datasets
Data/processed/       reduced datasets prepared for the website
css/style.css         page styling
js/visualisations.js  Vega-Lite embedding code
maps/                 readable Vega-Lite JSON specifications
index.html            web page entry point
```

## How to view

Open this URL from github pages:
https://jhie0005-tech.github.io/FIT3179-A2/ 

## Maps

`maps/map01_gallery_locator.json` draws Australia as a light reference layer, then plots each gallery using its longitude and latitude. Tooltips reveal the gallery name and address.

`maps/map02_galleries_by_state.json` aggregates galleries with valid coordinates by state and displays the totals as proportional circles at state and territory capitals.

`maps/map03_brisbane_suburb_counts.json` is a choropleth of recorded Brisbane public artworks by suburb. It joins the artwork counts to the supplied Brisbane suburb boundaries; unshaded suburbs have no record in this dataset.

`maps/map04_brisbane_installation_decades.json` plots Brisbane artworks by their recorded installation period, showing how older and newer works are distributed across the city.

`maps/chart01_installation_periods.json` is a non-map companion chart comparing the recorded installation periods in Brisbane and Melbourne. Canberra is excluded because its commissioning dates are mostly missing.

`maps/map05_brisbane_point_map.json` plots each Brisbane artwork using its longitude and latitude. Colour shows the recorded material and tooltips reveal the artwork details.

`maps/map06_melbourne_point_map.json` plots each Melbourne artwork using its geographic coordinates. The supplied CSV labels its coordinate columns in reverse, so the specification deliberately reads `latitude` as longitude and `longitude` as latitude. Colour shows the source classification and tooltips reveal the artwork details.

`maps/map07_canberra_point_map.json` plots each of the 562 Canberra artwork records using its geographic coordinates. The supplied CSV misspells the longitude column as longtitude, so the specification deliberately reads that spelling rather than correcting it. Colour shows the source classification and tooltips reveal the artwork details.

`maps/map08_three_city_comparison.json` places Brisbane, Melbourne and Canberra side by side as small multiples, using public_art_comparison.csv. Each city has its own framed panel with its own geographic context layers, and colour shows the shared category, which is a conservative crosswalk across the three councils’ different classification schemes. Brisbane has no category field, so most of its records appear as muted grey “Other / unclassified” points. Tooltips show the original source category.

`maps/map09_material_comparison.json` compares Brisbane and Canberra by the material each artwork is made from, using the grouped material field (for example Metal, Stone / concrete / brick, Timber, Paint and Tile / ceramic). Records with no material are shown as “Not recorded”. Melbourne is excluded because its data has no material field.

`maps/map10_density_maps.json` shows where public art is concentrated in Brisbane, Melbourne and Canberra by aggregating artwork points into binned counts, which avoids the overplotting in the point maps. All three cities use the same binning and colour design so their densities can be compared directly.