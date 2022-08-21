import numpy as np
import pandas as pd
from flask import Flask, render_template, request, redirect, url_for, flash, get_flashed_messages
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json
import bs4 as bs
import urllib.request
import pickle
import requests
from flask_sqlalchemy import SQLAlchemy

from flask_bcrypt import Bcrypt



if __name__ == '__main__':
    app.run(debug=True)