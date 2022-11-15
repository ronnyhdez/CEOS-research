from ceos_indices.generate_indices import indices


def main():
    params = {
        "input_images": "data/inputs/images/",
        "input_tower": "data/inputs/tower/",
        "sensor_locations": "ceos_indices/sr_sensor_plots.gpkg",
        "output_path": "data/outputs/",
        "distributed": False,
    }

    indices(params)


if __name__ == "__main__":
    main()
