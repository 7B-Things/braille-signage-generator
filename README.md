# braille-signage-generator

[![Open On CadHub](https://img.shields.io/badge/View-Open%20On%20CadHub-ff69b4)](https://cadhub.xyz/dev-ide/cadQuery#fetch_text_v1=https://github.com/7B-Things/braille-signage-generator/blob/main/braille_signage_generator.py)

![Example Braille Sign With CadQuery Text](images/braille_signage_generator.png)
Generated "CadQuery" Braille Sign

## Intro
A CadQuery script ([braille_signage_generator.py](https://github.com/7B-Things/braille-signage-generator/blob/main/braille_signage_generator.py)) to generate 3D printable braille sign plates based on user-provided English text. This is a work in progress and may not be [standards-compliant](http://www.brailleauthority.org/sizespacingofbraille/index.html) or completely correct yet. Regulations also vary by region, so please consult with local authorities to ensure that the dot geometry and spacing provided in this script meets requirements.

## Parameters

The following are parameters that are designed to be changed by the end user. Nothing else in the script should be changed unless the user understands the original intent of the code in the script, and accepts that altering the script may produce unexpected and incorrect results.

* `text` - The `text` string variable at the top of the script can be changed to set what braille characters are generated on the sign. Spaces can be added throughout the text string, and may be desired at the beginning and end of the text as a buffer between the braille and the edge of the plate. As an example, the braille output can be changed by doing something similar to `text = "cadquery"` to `text = "[your text here]"`.

## Usage

The fastest way to get started with this design is on the CadHub.xyz website. A [live version of this model](https://cadhub.xyz/dev-ide/cadQuery#fetch_text_v1=https://github.com/7B-Things/braille-signage-generator/blob/main/braille_signage_generator.py) can be loaded in your web browser and edited there. Once the `text` variable has been changed, click the _Render_ button to see an updated view. Once the generated braille is correct, the _Download STL_ button can be clicked to download an STL file that can be 3D printed.

## Local Execution and Development

It is not necessary to install anything just to modify the text and dowload an STL, but to execute this script locally the CQ-editor GUI or the cq-cli command line tool are the two simplest options. Links to both tools are provided below.

* [CQ-editor](https://github.com/CadQuery/CQ-editor/blob/master/README.md)
* [cq-cli](https://github.com/CadQuery/cq-cli/blob/main/README.md)

## Contributing

If there are any errors, or if there are improvements to be made, please open an issue on this repository. Please be sure to follow the conduct guidelines within the [Python Community Code of Conduct](https://www.python.org/psf/conduct/) when doing so.

## Licenses

* [Apache Software License 2.0](https://www.apache.org/licenses/LICENSE-2.0.html) - Software
* [CERN-OHL-P-2.0](https://ohwr.org/cern_ohl_p_v2.txt) - Hardware
* [CC-BY-SA-4.0](https://creativecommons.org/licenses/by-sa/4.0/) - Documentation
