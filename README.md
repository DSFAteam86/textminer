# textminer

Presented by:

![team 86](images/logoteam.png)

This repository is our project for the data science training program "Data science for all" (DS4A). This repo contains the extraction of four values from a list of pdfs with different designs. The extraction is done with contexto and tesseract and the analysis with nltk. Here's a brief description of the code:

## example

Clone the repo and execute

> python3 extract_nits.py

or

> python3 extract_cc.py

it will automatically read the files in the [sample folder](sample). Which has 21 sample files

## General Description

### config

The path of the .txt documents is the only value that can affect the execution of the entire process. That's way there is one variable to configure the path of the files to be read.

### miner

Miner does the initial mining, it searches for words and return chunks of text with the result, for more info read [the miner docs](docs/miner.md)

### proposers (notebook)

Proponentes is an algorithm to analyze the behavior of the column of selected proposals. For each process conducted by the Entity, there are a group of proposers, but just one is selected. The algorithm extract the information of this column for the whole period (2008-2020), and analyze the data.

### process

Process is in charge of reading input, it only reads pdfs

### number_reader

number_reader contains algorithms to extract numbers. For more info read [the number_reader docs](docs/number_reader.md)

### extract_nit and extract_cc

These files show the final result and provide 3 variables to work with as dataframes:

- df_error_nits_ungrouped, df_empty_nits_ungrouped, df_possible_nits_ungrouped
- df_error_cedulas_ungrouped, df_empty_cedulas_ungrouped, df_possible_cedulas_ungrouped

These variables can be treated like a regular DataFrame, they represent the 3 possible states in which data is extracted

- error: The length or format of the value was not retrieved successfully, therefore these results are not reliable
- empty: Empty values could be produced by the initial extraction due to a lack of quality in the content or because they went through the process of filtering and the outcome was just an empty string
- possible: These are the most reliable results

### order_frame.py

Order_frame contains functions to create dataframes based on the results of the mining process. For more info read [the order_frame docs](docs/order_frame.md)

## Team Members

- [Diego Fernando González Larrote](https://github.com/dfgonzalezla)
- [Erick Mora Martínez](https://github.com/egmoram-git)
- [Giovanni Sarta Valencia](https://github.com/gsarta)
- [Jhon Alexander Bernal Muñoz](https://github.com/LEXsB)
- [José Andrés Flórez Guiérrez](https://github.com/jaflorezg)
- [Jorge Iván Durango Acosta](https://github.com/duacos)
- [Diana Ximena Sarmiento Castro](https://github.com/dxsarmiento)
