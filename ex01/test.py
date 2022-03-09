#!/usr/bin/env python3
from FileLoader import FileLoader
from YoungestFellah import youngfellah
loader = FileLoader()
data = loader.load('../data/athlete_events.csv')
# Output
# Loading dataset of dimensions 271116 x 15
print(youngfellah(data, 2004))
# Output
# {’f’: 13.0, ’m’: 14.0}
print(youngfellah(data, 1991))
# Output
# {’f’: ’nan’, ’m’: ’nan’}
