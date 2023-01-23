# ConvertObjToMap
"ConvertObjToMap" is a program that converts obj files to .map format for use in Black Ops 3 mod tools/radiant. This repository contains the source code for the program, as well as a README file with instructions for use.

Latest Release: [vTiger](https://github.com/lazzm/ConvertObjToMap/releases/tag/vTiger)

## How to run:

### Standalone executable:

This .exe runs on Windows and allows for the converter to be used without the need for Python to be installed.

1. Download the zip file called ['convert_obj_to_map_vTiger.zip'](https://github.com/lazzm/ConvertObjToMap/releases/download/vTiger/convert_obj_to_map_vTiger.zip) from the latest release.
2. Extract the exe file from the zip file.
3. Place the .obj files and .exe in the same directory.
4. Run the exe file which will convert the files to map format and create the new files in the same directory.

### Python script

This build was written using Python 3.11.1. Please install the latest version of Python, but use 3.11.1 for this version if there are any problems.
Download from the Python Official Website: [Download Python](https://www.python.org/downloads/)

1. Download the source code from the latest release.
2. Extract the source code.
3. Place the .obj files and the .py file into the same directory.
4. Run the python script which will convert the files to map format and create the new files in the same directory.

### Future Updates

Hoping that future versions of this will provide the ability to retain the material information per face and the UV data.
This was looked into and the issue is that I'm not sure how Radian't works with its UVs so they are never correct. 
I'm hoping that I can find any information or figure out what conversion needs doing to UVs within an OBJ to this map format.

If there is any information you might know regarding Radiant and how it uses .map files, please let me know.
