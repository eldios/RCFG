# Project Name

RCFG : Random Codice Fiscale Generator

## Installation

Requirements :

1. Python 3.x
2. PyCodiceFiscale library copied/cloned in directory $(PWD)/pycodicefiscale

## Usage

usage: rcfg.py [-h] [-V] [-d] [-n FIRSTNAMES] [-l LASTNAMES] [-o OUTPUT]
               [-c COUNT] [-q]

Random CodiceFiscale Generator - Generates a list of random fake Italian people along with their CF (Codice Fiscale, italian birth data ID) and output the result as a CSV

optional arguments:

```
  -h, --help            show this help message and exit
  -V, --version         show program's version number and exit
  -d, --debug           Enable debugging info
  -n FIRSTNAMES, --firstnames FIRSTNAMES
                        *TODO* File containing a newline separated list of
                        first names. If not specified a list of 50 common
                        Italian first (male/female) names will be used
  -l LASTNAMES, --lastnames LASTNAMES
                        *TODO* File containing a newline separated list of
                        last names. If not specified a list of 50 common
                        Italian last names will be used
  -o OUTPUT, --output OUTPUT
                        Output file used to store the resulting list of random
                        CFs
  -c COUNT, --count COUNT
                        How many CF should be generated
  -q, --quiet           Only output CF without the related Person data
```

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## History

20160305 - 0.0.1 - Initial commit
20160305 - 0.0.2 - Changed city representation
20160307 - 0.0.3 - Fixed CF generation mistake, added max number of years to randomize birthdate
20160308 - 0.0.4 - updated pycodicefiscale module

## Credits

Author: Emanuele 'Lele' Calo' (eldios)

## License

The MIT License (MIT)

Copyright (c) 2016 - Emanuele 'Lele' Calo'

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
