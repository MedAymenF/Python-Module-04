#!/usr/bin/env python3
from FileLoader import FileLoader
from Komparator import Komparator

if __name__ == "__main__":
    loader = FileLoader()
    data = loader.load('../data/athlete_events.csv')
    kmp = Komparator(data)
    kmp.compare_box_plots('Medal', 'Age')
    kmp.compare_box_plots('Sex', 'Height')
    kmp.density('Medal', 'Weight')
    kmp.density('Sex', 'Height')
    kmp.compare_histograms('Medal', 'Height')
    kmp.compare_histograms('Sex', 'Height')
