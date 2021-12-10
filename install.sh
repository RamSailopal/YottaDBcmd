#!/bin/bash
python3 -m pip install typer
cp yottacmd /usr/local/bin
yottacmd --install-completion bash
