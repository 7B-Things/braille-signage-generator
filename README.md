# braille-signage-generator

[![Open On CadHub](https://img.shields.io/badge/view-Open%20On%20CadHub-ff69b4)](https://cadhub.xyz/dev-ide/cadQuery#encoded_script_v2=eJy9Vttu4zYQfddXDLQvUuLK8S0JDKhAL2ifCuxDgQINAoGWRhY3MimT9DrZov/eGcqS7I2NFtsgBgxpDudyhuQcW24abRzkotju0LyAsJBvg+AD/FQJtUZwFX3x2YFUVhatvd1phxaEKkBAUwuH5L+XrvKrommMbowkGArtLK3UNawQ1qjQEFokgc+YQtiVDbnij0aQpw8iX71BR3yiQoMiIG/p7FSN1sKL3tFrgcY6ZsFlc60sUjKVo42DShv5RSsn6kwqh4ZzpjBNFsFnNE7mr/GvI3Ik1incfhVQS4UET24CCs0qlOuKM9xQBgYKKYg3GnZJZkGwEhYzV8n8STFvRhcBN/ubaKA0esONGZFziNPQaCudpE4S3g+KLUArqJxr7HI8RpXs5ZNskKok2qzHbI0P25Z9FI6yKEuRv9N+9KlAGD4fOthS17Xe2yVZE4A5PaYAC3rMgPr8AHcA9wHzyRpNzWYb4pjCXwHQJxThEsJJOGqtlbdG087OW3ve2cXBHi06BFukt8tDhiFm3SODV9VhPSIZOYr6dLAHj6c2ZtbZdZejRzYHjyGL6pEhj+6wHmn6TEPk9ggbPM2A9phtmR7Fuh4ZvHZt5N3ovkM+D7luO2zfdz1gz92eH8W+HPU1eH7pOyMs+JsuZIElzZzL/DRne1m4KuIhjZdtRBj65898tzc0AtbP3OH669JbPhZW3a1lSO02K7rZ5NBfc7raxxkNup1RENWo2oJwBWdH8YpGZx6/otpS+A9cfU//i+pGPGdEk0aC3qIHzzimoaLJJXX0KvkYnzQ1PdMMK8619+o+/+4RdaW/g8mlDYq9rPx60Fjf0uogqK1Etz2nEOXb5A9tnshWGMWJwdxFZ89+dGGf4Rpeq+gVqejNCHJkAIv0F1FbjE/aOPoklMfsCoxOBTKOuYkfilbSOa1XIsva2J9b0DCSwsNjIFlRA12WFr0KB3wafH7dgbRXotY5B5xK2wObj916VkvLKdg1sU0tXRSOQqLD65yVFjhp57rsO5OlX0tTlsflScNMNKHfQ1RFFJ075iuQtJkt/9HZTZ3Hwx5ifVRr+va1Zpdqzd6+1vRSrbu3rzW5VGv+bbXODuy3neLivRhcPNvb92Jw8cTv34sB3wNf6SAY1+lZJfUuklcn/rVXTv9MSkH/MKPw+z/DONkf6Wizs9VHr1YRdxAnuTR5jdHJ38Ixq2Tcq9/wHzI+yVuybrszofQLcJNMFhNqxFZ6n+nVJ5Zvzyz+B8WUcUk=)

![Example Braille Sign With CadQuery Text](images/braille_signage_generator.png)
Generated "CadQuery" Braille Sign

## Intro
A CadQuery script (_braille_signage_generator.py_) to generate 3D printable braille sign plates based on user-provided English text. This is a work in progress and may not be [standards-compliant](http://www.brailleauthority.org/sizespacingofbraille/index.html) or correct yet.

The `text` string variable at the top of the script can be changed to set what braille characters are generated on the sign. Nothing else in the script should be changed unless the user understands the original intent of the code in the script, and accepts that altering the script may produce unexpected and incorrect results.

## Usage

The fastest way to get started with this design is on the CadHub.xyz website. A [live version of this model](https://cadhub.xyz/dev-ide/cadQuery#encoded_script_v2=eJy9Vttu4zYQfddXDLQvUuLK8S0JDKhAL2ifCuxDgQINAoGWRhY3MimT9DrZov/eGcqS7I2NFtsgBgxpDudyhuQcW24abRzkotju0LyAsJBvg+AD/FQJtUZwFX3x2YFUVhatvd1phxaEKkBAUwuH5L+XrvKrommMbowkGArtLK3UNawQ1qjQEFokgc+YQtiVDbnij0aQpw8iX71BR3yiQoMiIG/p7FSN1sKL3tFrgcY6ZsFlc60sUjKVo42DShv5RSsn6kwqh4ZzpjBNFsFnNE7mr/GvI3Ik1incfhVQS4UET24CCs0qlOuKM9xQBgYKKYg3GnZJZkGwEhYzV8n8STFvRhcBN/ubaKA0esONGZFziNPQaCudpE4S3g+KLUArqJxr7HI8RpXs5ZNskKok2qzHbI0P25Z9FI6yKEuRv9N+9KlAGD4fOthS17Xe2yVZE4A5PaYAC3rMgPr8AHcA9wHzyRpNzWYb4pjCXwHQJxThEsJJOGqtlbdG087OW3ve2cXBHi06BFukt8tDhiFm3SODV9VhPSIZOYr6dLAHj6c2ZtbZdZejRzYHjyGL6pEhj+6wHmn6TEPk9ggbPM2A9phtmR7Fuh4ZvHZt5N3ovkM+D7luO2zfdz1gz92eH8W+HPU1eH7pOyMs+JsuZIElzZzL/DRne1m4KuIhjZdtRBj65898tzc0AtbP3OH669JbPhZW3a1lSO02K7rZ5NBfc7raxxkNup1RENWo2oJwBWdH8YpGZx6/otpS+A9cfU//i+pGPGdEk0aC3qIHzzimoaLJJXX0KvkYnzQ1PdMMK8619+o+/+4RdaW/g8mlDYq9rPx60Fjf0uogqK1Etz2nEOXb5A9tnshWGMWJwdxFZ89+dGGf4Rpeq+gVqejNCHJkAIv0F1FbjE/aOPoklMfsCoxOBTKOuYkfilbSOa1XIsva2J9b0DCSwsNjIFlRA12WFr0KB3wafH7dgbRXotY5B5xK2wObj916VkvLKdg1sU0tXRSOQqLD65yVFjhp57rsO5OlX0tTlsflScNMNKHfQ1RFFJ075iuQtJkt/9HZTZ3Hwx5ifVRr+va1Zpdqzd6+1vRSrbu3rzW5VGv+bbXODuy3neLivRhcPNvb92Jw8cTv34sB3wNf6SAY1+lZJfUuklcn/rVXTv9MSkH/MKPw+z/DONkf6Wizs9VHr1YRdxAnuTR5jdHJ38Ixq2Tcq9/wHzI+yVuybrszofQLcJNMFhNqxFZ6n+nVJ5Zvzyz+B8WUcUk=) can be loaded in your web browser and edited there.

## Local Execution and Development

To execute this script locally, the CQ-editor GUI or the cq-cli command line tool are the two simplest options. Links to both tools are provided below.

* [CQ-editor](https://github.com/CadQuery/CQ-editor/blob/master/README.md)
* [cq-cli](https://github.com/CadQuery/cq-cli/blob/main/README.md)

## Contributing

If there are any errors, or if there are improvements to be made, please open an issue on this repository. Please be sure to follow the conduct guidelines within the [Python Community Code of Conduct](https://www.python.org/psf/conduct/).

## Licenses

* [Apache Software License 2.0](https://www.apache.org/licenses/LICENSE-2.0.html) - Software
* [CERN-OHL-P](https://ohwr.org/cern_ohl_p_v2.txt) - Hardware
