#!/usr/bin/env python3
from FileLoader import FileLoader
from ProportionBySport import proportionBySport
loader = FileLoader()
data = loader.load('../data/athlete_events.csv')
# Output
# Loading dataset of dimensions 271116 x 15
print(proportionBySport(data, 2004, 'Tennis', 'F'))
