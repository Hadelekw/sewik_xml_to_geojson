## How to use?
In order to use the converter, it is necessary to have the files from the [unofficial SEWIK website](https://sewik.pl/) downloaded. Then it is just a matter of cloning the repository and running the following command:
```
python main.py input_file_path.xml output_file_path.geojson
```
By default the field names from the input file are translated from pascal case Polish into snake case English. This is done in order to maintain consistency with Python naming standards. In case the user does not want the translations, they need to edit the `settings.py` file and change the `FIELD_MAP` variable into one of the preexisting maps available in the file or `None` if none of the maps should be applied. Skipping a field in the map results in lack of that field in the resulting file.
