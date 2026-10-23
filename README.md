# Australian Public Art Collections

This repository contains introductory Vega-Lite maps for the FIT3179 assignment. They use the cleaned gallery data at `Data/processed/galleries_clean.csv` and `Data/processed/galleries_geocoded.csv`, plus the Brisbane public-art collection at `Data/public-art-brisbane-clean.csv`.

## Structure

```text
Data/                 source data and future processed datasets
Data/processed/       reduced datasets prepared for the website
Data/boundaries/      local geographic boundaries when added
css/style.css         page styling
js/visualisations.js  Vega-Lite embedding code
maps/                 readable Vega-Lite JSON specifications
index.html            web page entry point
```

## Preview locally

Serve the project through a local web server, then open `index.html` in the browser. For example, Visual Studio Code's Live Server extension works well. Opening the file directly may prevent the browser from loading the CSV and JSON files.

## Maps

`maps/map01_gallery_locator.json` draws Australia as a light reference layer, then plots each gallery using its longitude and latitude. Tooltips reveal the gallery name and address.

`maps/map02_galleries_by_state.json` aggregates galleries with valid coordinates by state and displays the totals as proportional circles at state and territory capitals.

`maps/map05_brisbane_point_map.json` plots each Brisbane artwork using its longitude and latitude. Colour shows the recorded material and tooltips reveal the artwork details.

`maps/map06_melbourne_point_map.json` plots each Melbourne artwork using its geographic coordinates. The supplied CSV labels its coordinate columns in reverse, so the specification deliberately reads `latitude` as longitude and `longitude` as latitude. Colour shows the source classification and tooltips reveal the artwork details.
