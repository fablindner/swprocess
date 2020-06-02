"""File for derived class PeaksActive for handling peaks from active
data."""

from swprocess import Peaks

import numpy as np
import json
import logging
logger = logging.getLogger(__name__)


class PeaksActive(Peaks):
    """Spectral peaks of active-source dispersion."""

    def __init__(self, peak_data_dicts):
        super().__init__(peak_data_dicts)

    @classmethod
    def from_json(cls, fname, max_vel=1000):
        with open(fname, "r") as f:
            data = json.load(f)

        # frequency, velocity, offset = [], [], []
        # for key, value in data.items():
        #     frq = np.array(value["frequency"])
        #     vel = np.array(value["velocity"])
        #     frequency += [frq[np.where(vel<max_vel)]]
        #     velocity += [vel[np.where(vel<max_vel)]]
        #     offset += [key]
        # return cls(frequency, velocity, offset)
        return cls(data)
