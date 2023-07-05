# Bibliotheken importieren
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# warnings ignorieren
import warnings
warnings.filterwarnings("ignore")


def julia_Menge(h_range, w_range, max_iterationen, re, im):

	# von links oben nach rechts unten
	y, x = np.ogrid[1.4: -1.4: h_range*1j, -1.4: 1.4: w_range*1j]
	z_array = x + y*1j
	a = re + im
	iterationen_bis_zur_divergenz = max_iterationen + np.zeros(z_array.shape)
	for h in range(h_range):
		for w in range(w_range):
			z = z_array[h][w]
			for i in range(max_iterationen):
				z = z**2 + a
				if z * np.conj(z) > 4:
					iterationen_bis_zur_divergenz[h][w] = i
					break
	return iterationen_bis_zur_divergenz


fig = plt.figure(figsize=(10, 10))
ax = plt.axes()
julia = julia_Menge(h_range=500, w_range=500, max_iterationen=70, re=-0.744, im=0.148j)

ax.imshow(julia, interpolation="hanning", cmap='twilight_shifted')
plt.savefig('julia_Menge.png', dpi=300, bbox_inches='tight')
print("ok show")


########################################

frames = 2000  # Anzahl der Frames in der Animation
as_mp4 = True

# c = r*cos(a) + i*r*sin(a) = r*e^{i*a}
r = 0.7885
a = np.linspace(0, 2*np.pi, frames)

fig = plt.figure(figsize=(10, 10))
ax = plt.axes()

print("begin trigo")
def animate_trigo(i):
    ax.clear()

    re = r* np.cos(a[i])
    im = r * np.sin(a[i])*1j
    print("anim_trigo", re, im)    

    julia_trigo = julia_Menge(500, 500, 70, re=re, im=im)
    img = ax.imshow(julia_trigo, interpolation="hamming", cmap='twilight_shifted')
    return [img]

# Aufruf der Animator
anim = animation.FuncAnimation(fig, animate_trigo, frames=frames, interval=50, blit=True)

if as_mp4:
    # Die Formatierung für die Filmdateien einrichten
    Writer = animation.writers['ffmpeg']
    writer = Writer(fps=28, metadata=dict(artist='Me'), bitrate=-1)
    # Animation als mp4-Datei speichern
    anim.save('julia_Menge_trigo.mp4', writer=writer) 
    print("Trigo FINI!!!")
else:
    # Animation als gif-Datei speichern 
    anim.save('julia_Menge_trigo.gif', writer='imagemagick') 


##########################


frames = 2000  # Anzahl der Frames in der Animation
as_mp4 = True

a = np.linspace(-1.000, 1.000, frames)

fig = plt.figure(figsize=(10, 10))
ax = plt.axes()

print("begin mvre")
def animate_setim(i):
    ax.clear()

    re = a[i]    
    print("anim_mvre", re)    

    julia_mvre = julia_Menge(500, 500, 70, re=re, im=0.148j)
    img = ax.imshow(julia_mvre, interpolation="hamming", cmap='twilight_shifted')
    return [img]

# Aufruf der Animator
anim_setim = animation.FuncAnimation(fig, animate_setim, frames=frames, interval=50, blit=True)

if as_mp4:
    # Die Formatierung für die Filmdateien einrichten
    Writer = animation.writers['ffmpeg']
    writer = Writer(fps=28, metadata=dict(artist='Me'), bitrate=-1)
    # Animation als mp4-Datei speichern
    anim_setim.save('julia_animate_setim.mp4', writer=writer) 
    print("animate_setim FINI!!!")
else:
    # Animation als gif-Datei speichern 
    anim_setim.save('julia_animate_setim.gif', writer='imagemagick') 


##########################


frames = 2000  # Anzahl der Frames in der Animation
as_mp4 = True

a = np.linspace(-1.000, 1.000, frames)

fig = plt.figure(figsize=(10, 10))
ax = plt.axes()

print("begin mvim")
def animate_set_re(i):
    ax.clear()

    im = a[i]*1j    
    print("anim_mvim", im)    
    julia_mvim = julia_Menge(500, 500, 70, re=-0.748, im=im)
    img = ax.imshow(julia_mvim, interpolation="hamming", cmap='twilight_shifted')
    return [img]

# Aufruf der Animator
anim_set_re = animation.FuncAnimation(fig, animate_set_re, frames=frames, interval=50, blit=True)

if as_mp4:
    # Die Formatierung für die Filmdateien einrichten
    Writer = animation.writers['ffmpeg']
    writer = Writer(fps=28, metadata=dict(artist='Me'), bitrate=-1)
    # Animation als mp4-Datei speichern
    anim_set_re.save('julia_animate_set_re.mp4', writer=writer) 
    print("animate_set_re FINI!!!")
else:
    # Animation als gif-Datei speichern 
    anim_set_re.save('julia_animate_set_re.gif', writer='imagemagick') 

##########################


frames = 2000  # Anzahl der Frames in der Animation
as_mp4 = True

a = np.linspace(-1.000, 1.000, frames)
b = np.linspace(1.000, -1.000, frames)

fig = plt.figure(figsize=(10, 10))
ax = plt.axes()

print("begin mvre_im")
def animate_mvim_re(i):
    ax.clear()

    re = a[i]  
    im = b[i]*1j  
    print("animate_mvim_re_im", re, im)    


    julia_mvre_im = julia_Menge(500, 500, 70, re=re, im=im)
    img = ax.imshow(julia_mvre_im, interpolation="hamming", cmap='twilight_shifted')
    return [img]

# Aufruf der Animator
anim_mvim_re = animation.FuncAnimation(fig, animate_mvim_re, frames=frames, interval=50, blit=True)

if as_mp4:
    # Die Formatierung für die Filmdateien einrichten
    Writer = animation.writers['ffmpeg']
    writer = Writer(fps=28, metadata=dict(artist='Me'), bitrate=-1)
    # Animation als mp4-Datei speichern
    anim_mvim_re.save('julia_animate_animate_mvim_re.mp4', writer=writer) 
    print("animate_mvim_re FINI!!!")
else:
    # Animation als gif-Datei speichern 
    anim_mvim_re.save('julia_animate_animate_mvim_re.gif', writer='imagemagick') 