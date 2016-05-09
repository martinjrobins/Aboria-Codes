import init
import matplotlib.pyplot as plt
import time
import numpy as np

#plt.plot([1,2,3,4], [1,4,9,16], 'ro')
#plt.axis([0, 6, 0, 20])
#plt.show()

# create a set of particles
particles = init.Particles()

N = 2 # number of particles

for x in range(0,N):
	# create a particle
	p = init.Particle()
	#s = np.random.normal(50,10,2)

	# set the particle position
	#p.position = [s[0],s[1],0.0]
	p.position = [45+10*x,50,0.0]


	# add your particle to the set of particles
	particles.append(p)


# setup neighbourhood searching
minbox = [-20.0, -20.0 ,0.0]
maxbox = [120.0, 120.0 ,0.0]
L = 20
periodic = [False, False, False]
particles.init_neighbour_search(minbox,maxbox,L,periodic)

#print particles[0].position[0]
#print particles[1].position[0]

epsilon = 20.0 
theta = np.linspace(0,2*np.pi,100)
X = epsilon/2*np.cos(theta)
Y = epsilon/2*np.sin(theta)




plt.axis([0, 100, 0, 100])
plt.ion()
plt.show()

for i in range(0,N):
		plt.plot(particles[i].position[0]+X,particles[i].position[1]+Y,'b')
plt.axis([0, 100 , 0, 100])
plt.draw()

#for x in range(0,20):
#	init.timestep(particles)
#	print particles[0].position

for x in range(0,5000):
	
	init.timestep(particles)
	print particles[1].id
	plt.clf()	
	for i in range(0,N):
		plt.plot(particles[i].position[0]+X,particles[i].position[1]+Y,'b')
	plt.axis([0, 100 , 0, 100])
	plt.draw()
	time.sleep(5)


#plt.axis([0, 100, 0, 100])
#plt.ion()
#plt.show()
#plt.clf()
#for i in range(0,N):
#		plt.plot(particles[i].position[0]+X,particles[i].position[1]+Y,'b')
#plt.axis([0, 100 , 0, 100])
#plt.draw()
#plt.show()
#time.sleep(1000000)






