<div align="center">
  <h1>PDF Merger with Watermark</h1>
  <blockquote>Script to merge a list of PDF files and add a watermark if needed</blockquote>
</div>

## 📦 External libraries installation

```
// with Python 3
pip3 install PyPDF2
```

## ⚙️ Usage

First argument: [Y/N] depending if you want a watermark (from watermark.pdf) in the output file.
Second argument: 1 to n PDF files to merge and mark if needed.

```
python pdf-merger.py [Y/N] [PDF files]
```

## 📜 Documentation and examples

Check out the [PyPDF2 Documentation](https://pythonhosted.org/PyPDF2/).

Example:

```
python pdf-merger.py Y dummy.pdf dummy_2.pdf
```
