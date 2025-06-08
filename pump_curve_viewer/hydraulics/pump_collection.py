# this script is dedicated to the extraction of characteristic
# pump curve information

# import numpy as np
import os
from pathlib import Path
from enum import Enum
from typing import Optional


class MediaType(Enum):
    png = 1
    pdf = 2


class PumpSource:
    def __init__(self, location: Optional[Path] = None):
        self.__type: MediaType
        self.__location: Optional[Path] = None
        if location is not None:
            self.set_location(location)

    def set_location(self, location: Path):
        # sanity checks
        assert(os.path.exists(location))
        assert(os.path.isfile(location))
        _, ext = os.path.splitext(location)
        ext = ext.strip('.').lower()
        assert(ext in MediaType._member_names_)
        # assign values
        self.__location = location
        self.__type = MediaType[ext]


class PumpCollection:
    def __init__(self):
        # source properties
        self.__n_sources: int = 0           # number of sources
        self.__locations = [PumpSource]     # location array

    def add_source(self, sourcelocation):
        pass

    def get_rgb(self):
        pass
