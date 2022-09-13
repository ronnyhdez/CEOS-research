from typing import List, Dict

import numpy as np
import pandas as pd


def calculate_indices(images: List[np.ndarray], dates: List[str]) -> Dict[str, List[np.ndarray]]:
    """Calculates various vegetation indices from PF bands.

    Args:
        images (List[np.ndarray]): All images
        dates (List[str]): Corresponding image acquisition dates

    Returns:
        Dict[str, List[np.ndarray]]: NDVI, NIRv indices
    """
    ndvi = _generate_ndvi(images)
    nirv = _generate_nirv(images, ndvi)

    return {"date": dates, "NDVI": ndvi, "NIRv": nirv}


def _generate_ndvi(images: List[np.ndarray]) -> List[np.ndarray]:
    """Calculates NDVI.
    
    NDVI: Normalized Difference Vegetative Index
        The ratio of the difference between near infrared and red reflectance to the sum of the near infrared and red
        reflectances."""
    ndvi = []
    for image in images:
        image_ndvi = (image[3] - image[2]) / (image[3] + image[2])
        ndvi.append(image_ndvi)

    return ndvi


def _generate_nirv(images: List[np.ndarray], ndvi: List[np.ndarray]) -> List[np.ndarray]:
    """Calculates NIRv

    NIRv: The product of the NDVI and near infrared reflectances"""
    nirv = []
    for idx, image in enumerate(images):
        image_nirv = image[3] * ndvi[idx]
        nirv.append(image_nirv)

    return nirv
