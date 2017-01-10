import numpy as np
import matplotlib.pyplot as plt
import matplotlib.widgets as wdgt

# Reset der Slider
def reset(event):
    sfreq.reset()
    samp.reset()

# Ändern der Linienfarbe
def colorfunc(label):
    l.set_color(label)
    fig.canvas.draw_idle()

# Update des Graphen
def update(val):
    amp = samp.val
    freq = sfreq.val
    l.set_ydata(amp * np.sin(2 * np.pi * freq * t))
    fig.canvas.draw_idle()

def initMain():
	axcolor = 'white' # Hintergrundfarbe

	fig, ax = plt.subplots()
	plt.subplots_adjust(left=0.25, bottom=0.25)
	t = np.arange(0.0, 1.0, 0.001)
	a0 = 5
	f0 = 3
	s = a0 * np.sin(2 * np.pi * f0 * t)

	l, = plt.plot(t, s, lw=1, color='red')

	plt.axis([0, 1, -10, 10])
	plt.grid()
	plt.q

	axfreq = plt.axes([0.25, 0.1, 0.65, 0.03], axisbg=axcolor)
	axamp = plt.axes([0.25, 0.15, 0.65, 0.03], axisbg=axcolor)

	# Erstellen der Slider
	sfreq = wdgt.Slider(axfreq, 'Freq', 0.1, 30.0, valinit=f0)
	samp = wdgt.Slider(axamp, 'Amp', 0.1, 10.0, valinit=a0)

	sfreq.on_changed(update)
	samp.on_changed(update)

	# Erstellen des Reset-Buttons
	resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
	button = wdgt.Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')
	button.on_clicked(reset)

	rax = plt.axes([0.025, 0.5, 0.15, 0.15], axisbg=axcolor)
	radio = wdgt.RadioButtons(rax, ('red', 'blue', 'green'), active=0)
	radio.on_clicked(colorfunc)

	plt.show()