const embedOptions = {
  actions: {
    export: true,
    source: true,
    compiled: false,
    editor: false
  }
};

vegaEmbed("#brisbane-map", "maps/map05_brisbane_point_map.json", embedOptions)
  .catch((error) => {
    document.querySelector("#brisbane-map").textContent = `Unable to load the map: ${error.message}`;
    console.error(error);
  });
