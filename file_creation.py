import numpy as np
import iris

# Original file is over 1Gb, so load just one data variable.
cube = iris.load_cube('xexoc_1996_2005_grid_T.nc_nc3','Net Downward Heat Flux')

# Reduce the bounds coordinates from float64 to float32.
cube.coord('longitude').bounds = np.asanyarray(cube.coord('longitude').bounds, dtype=np.float32)
cube.coord('latitude').bounds = np.asanyarray(cube.coord('latitude').bounds, dtype=np.float32)

# Resulting file is about 62Mb.
iris.save(cube, 'nemo_025_sample_grid.nc')

