from numpy import log as ln
import numpy as np
#Test 10km/h
#TEST1
a1 = np.array([0.05627041, 0.05130751, 0.08187014, 0.0734666])
a2 = np.array([0.02101189, 0.01839682, 0.01191603, 0.02323148])
delta = ln(a1/a2)
T = np.array([10.8-9.76, 10.78- 9.76, 11.48-11, 11.48-11])
Theta = delta/T
Mfl= 782
Mfr= 660
Mrl= 720
Mrr= 670
i=0

c1 = 2*Theta*[Mfl,Mfr,Mrl,Mrr]

print(f'Test{i+1} : {c1} Ns/m')
i+=1


#TEST2
a1 = np.array([0.05041236, 0.0480182, 0.08162759, 0.07447942])
a2 = np.array([0.01196535, 0.01199472, 0.01623033, 0.02330101])
delta = ln(a1/a2)
T = np.array([9.98-8.96, 9.8- 8.96, 10.62-10.14, 10.62-10.14])
Theta = delta/T

c2 = 2*Theta*[Mfl,Mfr,Mrl,Mrr]

print(f'Test{i+1} : {c2} Ns/m')
i+=1


#Test 3
a1 = np.array([0.01737188, 0.0439909, 0.08394438, 0.07638204])
a2 = np.array([0.00985369, 0.01239358, 0.01874895, 0.02520788])
delta = ln(a1/a2)
T = np.array([10.68-9.88, 9.32- 8.5, 10.12-9.64, 10.12-9.64])
Theta = delta/T

c3 = 2*Theta*[Mfl,Mfr,Mrl,Mrr]

print(f'Test{i+1} : {c3} Ns/m')
i+=1

c_10 = np.mean([c1,c2,c3],axis=0)

#Test 4

a1 = np.array([0.02296091, 0.02239687, 0.06262587, 0.05836381])
a2 = np.array([0.01315211, 0.0138956, 0.01541363, 0.02566426])
delta = ln(a1/a2)
T = np.array([8.44-7.76, 8.38- 7.76, 9-8.54, 9-8.54])
Theta = delta/T

c4 = 2*Theta*[Mfl,Mfr,Mrl,Mrr]


i+=1

#Test 5

a1 = np.array([0.0230907, 0.02315691, 0.06351067, 0.05629337])
a2 = np.array([0.015758, 0.0150333, 0.01523479, 0.0239434])
delta = ln(a1/a2)
T = np.array([7.14-6.48, 7.06- 6.46, 7.7-7.24, 7.7-7.22])
Theta = delta/T

c5 = 2*Theta*[Mfl,Mfr,Mrl,Mrr]

i+=1

#Test 6

a1 = np.array([0.01883603, 0.01764598, 0.06466189, 0.05863322])
a2 = np.array([0.01416527, 0.01631257, 0.01550266, 0.025957])
delta = ln(a1/a2)
T = np.array([6.86-6.14, 6.78- 6.14, 7.44-6.96, 7.44-6.96])
Theta = delta/T

c6 = 2*Theta*[Mfl,Mfr,Mrl,Mrr]

c_15 = np.mean([c4,c5,c6],axis=0)
i+=1

#Test 7
#20km/h
a1 = np.array([0.01753577, 0.01340944, 0.0451882, 0.04921149])
a2 = np.array([0.0071837, 0.00813544, 0.01412795, 0.02077])
delta = ln(a1/a2)
T = np.array([5.62-5.12, 5.6- 5.12, 6.16-5.68, 6.14-5.68])
Theta = delta/T

c7 = 2*Theta*[Mfl,Mfr,Mrl,Mrr]

i+=1

#Test 8

a1 = np.array([0.01747297, 0.01438098, 0.04461831, 0.04684203])
a2 = np.array([0.0073684, 0.006698, 0.012475, 0.02015248])
delta = ln(a1/a2)
T = np.array([4.66-4.16, 4.66- 4.14, 5.2-4.74, 5.18-4.72])
Theta = delta/T

c8 = 2*Theta*[Mfl,Mfr,Mrl,Mrr]

i+=1

#Test 9

a1 = np.array([0.01503735, 0.01261387, 0.041538, 0.04137])
a2 = np.array([0.0101189, 0.007958, 0.01484436, 0.0204517])
delta = ln(a1/a2)
T = np.array([6.04-5.56, 6.04-5.56, 6.58-6.12, 6.56-6.1])
Theta = delta/T

c9 = 2*Theta*[Mfl,Mfr,Mrl,Mrr]

i+=1

c_20 = np.mean([c7,c8,c9],axis=0)
#25km/h
#Test 10

a1 = np.array([0.010735, 0.0115405, 0.0373709, 0.040199])
a2 = np.array([0.0069338, 0.0031897, 0.01802765, 0.0180148])
delta = ln(a1/a2)
T = np.array([3.62-3.24, 3.64-3.18, 4.16-3.7, 4.14-3.68])
Theta = delta/T

c10 = 2*Theta*[Mfl,Mfr,Mrl,Mrr]


i+=1

#Test 11

a1 = np.array([0.011103, 0.008725488, 0.039064, 0.03720826])
a2 = np.array([0.00990688, 0.0063198, 0.014007, 0.01534223])
delta = ln(a1/a2)
T = np.array([4.74-4.34, 4.76-4.28, 5.28-4.8, 5.26-4.8])
Theta = delta/T

c11 = 2*Theta*[Mfl,Mfr,Mrl,Mrr]


i+=1

#Test 12

a1 = np.array([0.0119378, 0.01183959, 0.03535273, 0.04448532])
a2 = np.array([0.001475, 0.0065379, 0.018408, 0.01215835])
delta = ln(a1/a2)
T = np.array([3.28-2.92, 3.4-2.84, 3.84-3.36, 3.82-3.36])
Theta = delta/T

c12 = 2*Theta*[Mfl,Mfr,Mrl,Mrr]


i+=1

c_25 = np.mean([c10,c11,c12],axis=0)

#40Km/h
#Test 13

a1 = np.array([0.01807503, 0.008360442, 0.04043492, 0.0495848])
a2 = np.array([0.0064832, 0.0073594, 0.013073, 0.0041844])
delta = ln(a1/a2)
T = np.array([3.262-2.66, 3.44-2.72, 2.82-2.28, 2.82-2.26])
Theta = delta/T

c13 = 2*Theta*[Mfl,Mfr,Mrl,Mrr]


i+=1

#Test 14

a1 = np.array([0.0215688, 0.02254201, 0.04702029, 0.055099])
a2 = np.array([0.0095479, 0.01092693, 0.00817801, 0.0065088])
delta = ln(a1/a2)
T = np.array([2.92-1.8, 2.8-1.8, 2.72-2.18, 2.72-2.16])
Theta = delta/T

c14 = 2*Theta*[Mfl,Mfr,Mrl,Mrr]

i+=1

#Test 15

a1 = np.array([0.013257, 0.02257585, 0.04914215, 0.049434])
a2 = np.array([0.01129898, 0.01801239, 0.0028, 0.0045])
delta = ln(a1/a2)
T = np.array([1.78-0.72, 1.64-0.72, 1.6-1.08, 1.6-1.06])
Theta = delta/T

c15 = 2*Theta*[Mfl,Mfr,Mrl,Mrr]

i+=1
c_40 = np.mean([c13,c14,c15],axis=0)
print ('K_FL , K_FR, K_RL, K_RR')

print(f'10km/h : {c_10} Ns/m')
print(f'15km/h : {c_15} Ns/m')
print(f'20km/h : {c_20} Ns/m')
print(f'25km/h : {c_25} Ns/m')
print(f'40km/h : {c_40} Ns/m')
# K calcul 

#Test1,2,3
print ('K_FL , K_FR, K_RL, K_RR')

FL = np.mean([2.036,1.341,1.312])
FR = np.mean([1.81,1.877,1.968])
RL = np.mean([2.174,2.372,2.286])
RR = np.mean([2.174,2.372,2.286])
j = 0 
K = np.array([Mfl*(FL*2*np.pi)**2,Mfr*(FR*2*np.pi)**2,Mrl*(RL*2*np.pi)**2,Mrr*(RR*2*np.pi)**2])

print(f'Test 10km/h : K : {K} N/m')

#Test4,5,6

FL = np.mean([1.905,2.137,2.015])
FR = np.mean([1.905,2.137,1.763])
RL = np.mean([2.554,2.598,2.606])
RR = np.mean([2.554,2.598,2.606])
j = 0 
K = np.array([Mfl*(FL*2*np.pi)**2,Mfr*(FR*2*np.pi)**2,Mrl*(RL*2*np.pi)**2,Mrr*(RR*2*np.pi)**2])

print(f'Test 15km/h : K : {K} N/m')

#Test7,8,9

FL = np.mean([2.119,10.132,2.273])
FR = np.mean([2.119,1.961,10.046])
RL = np.mean([2.273,2.543,2.517])
RR = np.mean([2.273,2.543,2.517])
j = 0 
K = np.array([Mfl*(FL*2*np.pi)**2,Mfr*(FR*2*np.pi)**2,Mrl*(RL*2*np.pi)**2,Mrr*(RR*2*np.pi)**2])

print(f'Test 20 km/h : K : {K} N/m')

#Test10,11,12

FL = np.mean([10.553,10.376,8.765])
FR = np.mean([14.224,14.111,13.921])
RL = np.mean([2.382,2.095,2.062])
RR = np.mean([2.382,2.095,2.062])
j = 0 
K = np.array([Mfl*(FL*2*np.pi)**2,Mfr*(FR*2*np.pi)**2,Mrl*(RL*2*np.pi)**2,Mrr*(RR*2*np.pi)**2])

print(f'Test 25 km/h : K : {K} N/m')

#Test13,14,15

FL = np.mean([11.114,13.147,14.066])
FR = np.mean([11.168,15.433,13.024])
RL = np.mean([2.273,2.070,2.470])
RR = np.mean([2.273,2.070,2.470])
j = 0 
K = np.array([Mfl*(FL*2*np.pi)**2,Mfr*(FR*2*np.pi)**2,Mrl*(RL*2*np.pi)**2,Mrr*(RR*2*np.pi)**2])

print(f'Test 25 km/h : K : {K} N/m')

