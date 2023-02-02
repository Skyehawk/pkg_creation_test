import warnings
import numpy as np

class UVConvert(object):
    '''
    This module calculates the bearing and magnitude of wind(s) given U V wind components 
    * Positive U wind is from the west
    * Positive V wind is from the south
    '''
    
    # ----- Properties and setters -----
    @property
    def uv_data(self):
        if not hasattr(self,'_uv_data'):
            self._uv_data = None
            warnings.warn("UVConvert: No input data parsed on __init__", UserWarning)
        if set(self._uv_data.keys()) != {'u', 'v'}:
            raise DataInputError('dictionary keys for uv_data must be "u" and "v"')
        if len(self._uv_data['u']) != len(self._uv_data['v']):
            raise DataInputError(f'length of u and v must be equal. "u" has length {len(self._uv_data["u"])}, "v" has length {len(self._uv_data["v"])}')
        return self._uv_data
    
    @property
    def units(self):
        if not hasattr(self,'_units'):
            self._units = None
            warnings.warn("UVConvert: No input units parsed on __init__", UserWarning)
        return self._units
    
    @uv_data.setter
    def uv_data(self, value):
        self._uv_data = value
    
    @units.setter
    def units(self, value):
        self._units = value

    #----- Methods -----

    
    def __init__(self, data, units):
        '''
        Parameters
        ----------
           data : dict
               keys u and v and values of an itterable
           units : str
               string representing the input units of u and v

        '''
        
        self.uv_data = data
        self.units = units
        self.mag = np.nan
        self.theta = np.nan
        
        
    def calculate_dir_mag(self):
        '''
        perform calculation of the magnitude and theta from U V components
        
        Returns
        -------
        dict of magnitude, theta and units
        '''
        u = list(map(float, self.uv_data['u']))
        v = list(map(float, self.uv_data['v']))
               
        self.mag = np.sqrt(np.square(u)+np.square(v))
        self.theta = np.mod(180+np.rad2deg(np.arctan2(u, v)),360)
        return({'magnitude':self.mag,
                'theta':self.theta,
                'units':{"magnitude": self.units,
                         "theta":"degrees cw from North"}
               })
    
class DataInputError(Exception):
    """Input data datastructure error"""