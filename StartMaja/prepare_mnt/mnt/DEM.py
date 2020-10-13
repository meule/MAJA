#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Copyright (C) 2016-2020 Centre National d'Etudes Spatiales (CNES), CSSI, CESBIO  All Rights Reserved

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from StartMaja.prepare_mnt.mnt.MNTBase import MNT
import os
import logging
import math
from StartMaja.Common import FileSystem, ImageTools


class DEM(MNT):
    """
    Base class to start with custom DEM.
    """

    def __init__(self, site, **kwargs):
        """
        Initialise an SRTM-type DEM.

        :param site: The :class:`prepare_mnt.mnt.SiteInfo` struct containing the basic information.
        :param kwargs: Forwarded parameters to :class:`prepare_mnt.mnt.MNTBase`
        """
        super(DEM, self).__init__(site, **kwargs)


    def prepare_mnt(self):
        """
        Prepare the srtm files.

        :return: Path to the full resolution DEM file.gsw
        :rtype: str
        """
        # Find/Download SRTM archives:
        dem = self.raw_dem
        # Combine to image of fixed extent
        srtm_full_res = os.path.join(self.wdir, "srtm_%sm.tif" % int(self.site.res_x))
        ImageTools.gdal_warp(nodata, dst=srtm_full_res,
                             r="cubic",
                             te=self.site.te_str,
                             t_srs=self.site.epsg_str,
                             tr=self.site.tr_str,
                             dstnodata=0,
                             srcnodata=0,
                             multi=True)
        return srtm_full_res

    @staticmethod

if __name__ == "__main__":
    pass
