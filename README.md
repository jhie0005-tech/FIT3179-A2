# Australian Public Art Collections

This repository contains an introductory Vega-Lite map for the FIT3179 assignment. The map uses the cleaned Brisbane public-art collection at `Data/public-art-brisbane-clean.csv`.

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

## First map

`maps/map05_brisbane_point_map.json` is a layered Vega-Lite map. It draws Australia as a light reference layer, then plots each Brisbane artwork using its longitude and latitude. Colour shows the recorded material and tooltips reveal the artwork details.
