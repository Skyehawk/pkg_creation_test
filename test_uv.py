import UV_convert as uvc
import numpy as np

def main():

	u_vals = np.random.uniform(low=-10, high=10, size=(50,))
	v_vals = np.random.uniform(low=-10, high=10, size=(50,))

	my_data = {'u':u_vals,'v':v_vals}
	
	res = uvc.UVConvert(data=my_data, units="m/s")

	print (res.calculate_dir_mag())

if __name__ == '__main__':
	main()