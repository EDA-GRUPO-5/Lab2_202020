import pytest 
import config

from ADT import list as lt
from DataStructures import singlelinkedlist as slt
from App.app import loadCSVFile


def test_singlelinkedlistmovies():
    details_lista = loadCSVFile(config.data_dir + "theMoviesdb/SmallMoviesDetailsCleaned.csv")
    cast_lista = loadCSVFile(config.data_dir + "theMoviesdb/MoviesCastingRaw-small.csv")

    return details_lista, cast_lista

@pytest.fixture
def load_linkedlistmovies():
    return test_singlelinkedlistmovies()