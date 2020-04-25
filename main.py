#!/usr/bin/env python
import os
from train import mtagtfs
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

mytrain = mtagtfs('G')
mytrain.set_api(os.getenv("API_KEY"))
mytrain.update()
