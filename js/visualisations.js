const embedOptions = {
  actions: {
    export: true,
    source: true,
    compiled: false,
    editor: false
  }
};

function embedMap(element, specification) {
  vegaEmbed(element, specification, embedOptions)
    .catch((error) => {
      document.querySelector(element).textContent = `Unable to load the map: ${error.message}`;
      console.error(error);
    });
}

embedMap("#gallery-map", "maps/map01_gallery_locator.json");
embedMap("#state-map", "maps/map02_galleries_by_state.json");
embedMap("#brisbane-suburb-map", "maps/map03_brisbane_suburb_counts.json");
embedMap("#brisbane-time-map", "maps/map04_brisbane_installation_decades.json");
embedMap("#installation-chart", "maps/chart01_installation_periods.json");
embedMap("#brisbane-map", "maps/map05_brisbane_point_map.json");
embedMap("#melbourne-map", "maps/map06_melbourne_point_map.json");
embedMap("#canberra-map", "maps/map07_canberra_point_map.json");
embedMap("#three-city-map", "maps/map08_three_city_comparison.json");
embedMap("#material-map", "maps/map09_material_comparison.json");
embedMap("#density-map", "maps/map10_density_comparison.json");
