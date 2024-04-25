#!/bin/bash
rm -rf venv build *.c *.so *.spec dist
python3 -m venv venv
source venv/bin/activate
venv/bin/python3 -m pip install --no-cache-dir -r requirements.txt
python3 setup.py build_ext --inplace
pyinstaller --onefile mp3_slicer.py
deactivate
