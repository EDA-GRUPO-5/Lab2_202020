import config
import pytest

from Sorting import shellsort as sort
from DataStructures import listiterator as it
from Test.sorting.less_greater import *
from ADT import list as slt
from Test.lab2.test_arraylistmovies import load_arraylistmovies
from Test.lab2.test_singlelinkedlistmovies import load_linkedlistmovies

def test_insertionsort_movies_arraylist(load_arraylistmovies):
    details, casting = load_arraylistmovies

    sort.shellSort(details, less)
    sort.shellSort(casting, less)

def test_insertionsort_movies_linkedlist(load_arraylistmovies):
    details, casting = load_linkedlistmovies

    sort.shellSort(details, less)
    sort.shellSort(casting, less)