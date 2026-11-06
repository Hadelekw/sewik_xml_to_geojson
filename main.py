import json
import sys
from xml.etree import ElementTree

import settings


def _degrees_string_to_float(degrees : str|None) -> float:
    if degrees is None:
        return -1
    if '*' in degrees:
        coordinates = degrees.split('*')
        coordinates.extend(coordinates.pop().split('\''))
        coordinates = list(map(int, coordinates))
        result = coordinates[0]
        result += coordinates[1] / 60
        result += coordinates[2] / 36000
    else:
        result = float(degrees)
    return result


def convert_with_field_map(root) -> dict:
    result = {
        'type': 'FeatureCollection',
        'features': [],
    }
    for child in root[0]:
        result['features'].append(
            {
                'type': 'Feature',
                'geometry': {
                    'type': 'Point',
                    'coordinates': [],
                },
                'properties': {
                    settings.FIELD_MAP[key]: child.attrib[key] for key in child.attrib
                }
            }
        )
        for grandchild in child:
            if grandchild.tag in settings.COORDINATE_FIELDS:
                result['features'][-1]['geometry']['coordinates'].append(
                    _degrees_string_to_float(grandchild.text)
                )
            elif grandchild.tag in settings.FIELD_MAP:
                result['features'][-1]['properties'][settings.FIELD_MAP[grandchild.tag]] = grandchild.text
    return result


def convert_without_field_map(root) -> dict:
    result = {
        'type': 'FeatureCollection',
        'features': [],
    }
    for child in root[0]:
        result['features'].append(
            {
                'type': 'Feature',
                'geometry': {
                    'type': 'Point',
                    'coordinates': [],
                },
                'properties': {
                    key: child.attrib[key] for key in child.attrib
                }
            }
        )
        for grandchild in child:
            if grandchild.tag in settings.COORDINATE_FIELDS:
                result['features'][-1]['geometry']['coordinates'].append(
                    _degrees_string_to_float(grandchild.text)
                )
            else:
                result['features'][-1]['properties'][grandchild.tag] = grandchild.text
    return result


def main(input_file_path : str, output_file_path : str) -> None:
    tree = ElementTree.parse(input_file_path)
    root = tree.getroot()

    if settings.FIELD_MAP:
        result = convert_with_field_map(root)
    else:
        result = convert_without_field_map(root)


    with open(output_file_path, 'w+') as f:
        json.dump(result, f)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
