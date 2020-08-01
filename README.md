# Tendering Excel Table Cleanup
The following program cleans up excel tables in csv format for tendering use.

Author: Y , 2020. All rights reserved

## Preparing input

In an excel program save your excel spreadsheet as an csv. Remove cells that do not belong to the table. 
You should end up with a file with the name of _tendering_file.csv_

## Doing the cleaning 

```
python direct_conversion.py tendering_file.csv
```

It should result in an output.csv file reformatted


## Options

The conversion remove header/footer specified in the config.py file, does not remove additional table head, or ignore keywords, these can all be changed using the --keep_header, --ignore_keyword, --remove_table_head options.

For example if the header needs to be kept, run 

```
python direct_conversion.py tendering_file.csv --keep_header
```

## Configuration
All configurations of ignored keyword/headers can be changed in config.py


## Help

For help, run the following command:
```
python direct_conversion.py -h
```


