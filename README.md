[![HitCount](http://hits.dwyl.io/ro6ley/python-ocr-example.svg)](http://hits.dwyl.io/ro6ley/python-ocr-example)

# PyTesseract - Simple Python Optical Character Recognition

This repository contains the code for this [blogpost](https://stackabuse.com/pytesseract-simple-python-optical-character-recognition/).

## Getting Started

## Docs

- https://stackabuse.com/pytesseract-simple-python-optical-character-recognition/
- https://www.analyticsvidhya.com/blog/2021/06/optical-character-recognitionocr-with-tesseract-opencv-and-python/
### Prerequisites

Kindly ensure you have the following installed on your machine:

- [ ] [Python 3](https://realpython.com/installing-python/)
- [ ] [Tesseract](https://github.com/tesseract-ocr/tesseract/wiki#installation)
- [ ] [Git]()
- [ ] An IDE or Editor of your choice

### Running the Application

1. Clone the repository
```
$ git clone https://github.com/ro6ley/python-ocr-example.git
```

2. Check into the cloned repository
```
$ cd python-ocr-example
```

3. If you are using Pipenv, setup the virtual environment and start it as follows:
```
$  pip install pipenv
$ pipenv install && pipenv shell
```


```
1. Install tesseract using windows installer available at: https://github.com/UB-Mannheim/tesseract/wiki

2. Note the tesseract path from the installation. Default installation path at the time of this edit was: C:\Users\USER\AppData\Local\Tesseract-OCR. It may change so please check the installation path.

3. pip install pytesseract

4. Set the tesseract path in the script before calling image_to_string:

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\USER\AppData\Local\Tesseract-OCR\tesseract.exe'

```

```
$ pip install -r requirements.txt
```

4. Run OCR server
```
$ python app.py
```
## Test
```
http://localhost:5000/upload
```

## Contribution

Please feel free to raise issues using this [template](./.github/ISSUE_TEMPLATE.md) and I'll get back to you.

You can also fork the repository, make changes and submit a Pull Request using this [template](./.github/PULL_REQUEST_TEMPLATE.md).
