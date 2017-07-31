import picamera
from mpi4py import MPI
from datetime import datetime
import numpy as np
import cv2
import pylab
import os, sys

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

#cv2.imwrite("/home/pi/comades/python/gris.png",imgGris)

if rank == 0:
    hora = datetime.now().strftime('%H:%M:%S.%f')[:-3]	 
    camara = picamera.PiCamera()
    camara.capture(hora + ".jpg")
    camara.close()

    ruta = "/home/pi/comades/python/"+str(hora+".jpg")
    foto = cv2.imread(ruta)
    imgGris = cv2.cvtColor(foto,cv2.COLOR_BGR2GRAY)
    cv2.imwrite("/home/pi/comades/python/gris.png",imgGris)
    comm.send(imgGris, dest=1, tag=11)
    
elif rank == 1:
    hora = datetime.now().strftime('%H:%M:%S.%f')[:-3]
    foto = comm.recv(source=0, tag=11)
    cv2.imwrite("/home/pi/comades/python/"+str(hora+".png"),foto)
    


    
