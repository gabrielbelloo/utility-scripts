from shared.image.metadata import get_size, get_dimensions

def validate_image(path, max_size_bytes, expected_dimensions):
    size = get_size(path)
    dimensions = get_dimensions(path)
    if size < max_size_bytes and dimensions == expected_dimensions:
        return True
    return False