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
embedMap("#brisbane-map", "maps/map05_brisbane_point_map.json");
embedMap("#melbourne-map", "maps/map06_melbourne_point_map.json");
