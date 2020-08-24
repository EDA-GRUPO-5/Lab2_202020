import pytest 
import config

from ADT import list as lt
from DataStructures import arraylist as alt
from DataStructures import listiterator as it
from App.app import loadCSVFile


def test_arraylistmovies():
    details_lista = loadCSVFile(config.data_dir + "theMoviesdb/SmallMoviesDetailsCleaned.csv")

    cast_lista = loadCSVFile(config.data_dir + "theMoviesdb/MoviesCastingRaw-small.csv")

    return details_lista, cast_lista

@pytest.fixture
def load_arraylistmovies():
    return it.newIterator(load_arraylistmovies())
