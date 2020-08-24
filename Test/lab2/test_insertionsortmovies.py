import config
import pytest

from Sorting import insertionsort as sort
from Test.sorting.less_greater import *
from DataStructures import listiterator as it
from ADT import list as slt
from Test.lab2.test_arraylistmovies import load_arraylistmovies
from Test.lab2.test_singlelinkedlistmovies import load_linkedlistmovies

def test_insertionsort_movies_arraylist(load_arraylistmovies):
    details, casting = load_arraylistmovies

    sort.insertionSort(details, less)
    sort.insertionSort(casting, less)

def test_insertionsort_movies_linkedlist(load_linkedlistmovies):
    details, casting = load_linkedlistmovies

    sort.insertionSort(details, less)
    sort.insertionSort(casting, less)