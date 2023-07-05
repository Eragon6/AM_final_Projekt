import matplotlib.pyplot as plt
import numpy as np

def julia_Menge(h_range, w_range, max_iterationen, re, im): # c = re + im*i

	# von links oben nach rechts unten
	y, x = np.ogrid[1.4: -1.4: h_range*1j, -1.4: 1.4: w_range*1j]
	z_array = x + y*1j
	c = re + im
	iterationen_bis_zur_divergenz = max_iterationen + np.zeros(z_array.shape)
	for h in range(h_range):
		for w in range(w_range):
			z = z_array[h][w]
			for i in range(max_iterationen):
				z = z**2 + c
				if z * np.conj(z) > 4:
					iterationen_bis_zur_divergenz[h][w] = i
					break
	return iterationen_bis_zur_divergenz

fig = plt.figure(figsize=(10, 10))

ax = plt.axes()
julia = julia_Menge(h_range=500, w_range=500, max_iterationen=70, re=-0.744, im=0.148j)

ax.imshow(julia, interpolation="hanning", cmap='twilight_shifted')
plt.savefig('julia_Set.png', dpi=300, bbox_inches='tight')
plt.show()
print("ok show")