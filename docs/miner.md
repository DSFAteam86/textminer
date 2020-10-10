# Miner
This file will serve as documentation for [miner.py](../miner.py)

    from miner import TextMiner
    import pdf2image

	pages = pdf2image.convert_from_path(
	    pdf_path = 'PDF with many pages.pdf',  
	    dpi=200, 
	    size=(1654,2340))

	page_list = process.extract_from(pages, 2)
	# This is the instance to work on an single page
	mine = TextMiner(page_list)

### get_data()
	
Returns the current state of the page_list
	
### chunks_width(word, left, right)

Find the *first* occurrence of a word or sentence in *every* page.

* **word**: the word you want to locate in every page of the PDF
* **left:** how many characters should appear before the word, *default: 20*
* **right**: how many characters should appear after the word,  *default: 20*

*Example*

	mine.get_chunks("cédula", left=0, right=40)
	mine.get_data()
	
	output<array>:
	
	['cédula de ciudadanía No. 60.371.697expe',
	 'cédula deciudadanía No. 88.269.727 de C',
	 'cédula de ciudadanía No. 17,594.750 17 d',
	 'cédula de ciudadania No. 17,595,750 , ',
	 'cédula de ciudadanía No, 88.269.727 de C',
	 'cédula de ciudadania No. 88.269.727 de C',
	 'cédula de ciudadaniaNo. 13,498,022. Est', ...]

###  get_chunks_width(word, left, right)

Similar to chunks_width(...). Find *all* occurrences of a word or sentence of every page and return a single array containing chunks of those occurrences.

* **word**: the word you want to locate in every page of the PDF
* **left:** how many characters should appear before the word, *default: 20*
* **right**: how many characters should appear after the word,  *default: 20*

*Example*

	mine.get_chunks_width("cédula", left=0, right=40)
	
	output<array>:
	
	['cédula de ciudadanía No. 60.371.697expe',
	 'cédula deciudadanía No. 88.269.727 de C',
	 'cédula de ciudadanía No. 17,594.750 17 d',
	 'cédula de ciudadania No. 17,595,750 , ',
	 'cédula de ciudadanía No, 88.269.727 de C',
	 'cédula de ciudadania No. 88.269.727 de C',
	 'cédula de ciudadaniaNo. 13,498,022. Est', ...]

###  get_chunks_in_array(arr, left, right)

Similar to get_chunks_width(...), but this method receives an array instead of a string. 

Search in every page and  find *all* occurrences of words or sentences in an array and return a single array containing chunks of those occurrences.

* **arr**: the words that you are trying to locate in every page of the PDF
* **left:** how many characters should appear before the word, *default: 20*
* **right**: how many characters should appear after the word,  *default: 20*

*Example*

	mine.get_chunks_width(["cédula", "cedula", "NIT", "C.C"], left=0, right=40)
	
	output<array>:
	
	['cédula de ciudadanía No. 60.371.697expe',
	 'cédula de ciudadaniaNo. 13,498,022. Est',
	 'cédula de ciudadanía No. 88.269.727 deC',
	 'cedula deciudadania No 88.277.358 exped',
	 'cedula de ciudadania No 88.200.502 de Cú',
	  ...
	 'cedulade ciudadania No 88.200.502 de Cú',
	 'cedula de ciudadanía No.17.595.750 de A',
	 'NIT.No. 800,103.927-7, representado leg',
	 'NIT 901350807-6 domiciliado en la ciudad',
	 'NIT-900402708-6 Participación 89%. 2. A',
	  ...
	 'C.C. 88.269.727 correo electrónicousai2',
	 'C.C. 88.200.502. Participación 1.%. C). ',
	 'cedula']


###  extract_exact(arr, left, right)

Extract a more precise portion of text. This function uses the results of get_chunks_in_array and locates specific sections. This function receives a callback or lambda which provides you with a tokenized  stop-word-free array.

* **func (word)**: This can be a function or a lambda. This function receives a *word* as a parameter, this *word* is defined inside TextMiner therefore there is no need to override it. *Word* represents every element of a tokenized version of the strings provided by get_chunks_in_array.

To better illustrate what *word* is, consider this word tokenized array:

    ["I got up at 6 AM] => ["got", "6", "AM"] // removing stop-words
In this case *word* presents every item in the array.

*Example*

	def get_cc(word):
	    # get strings that include numbers
	    if bool(re.search(r'\d', word)):
	        return word  
	        
	data = text_miner.extract_exact(get_cc)
	print(data)
	
	output<array>:
	
	'60.371.697expe',
	 '88.269.727',
	 '17,594.750',
	 '17,595,750',
	  ...
	 '68.245.507',
	 '10.954,770',
      ...
	 'NIT-900402708-8',
	 'NIT-900402708-5',
	 's27',
	  ...
	 'electrónicousai2',
	 '88.200.502',
	 '13.498,022']


