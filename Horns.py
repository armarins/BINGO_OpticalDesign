import numpy as np
def parameters(design="DR"):  
    if design=="DR":
        DH = 249.44
        DV = 240.
        B  = 138.57
        dh = 233.2
        dv = 225.2
        b  = 129.08
        horn_diam=190.
        x  = (DH-B)/2.
        return {"DH":DH,"DV":DV,"dh":dh,"dv":dv,"B":B,"b":b,"horn diam":horn_diam,'x':x}
    else:
        raise NameError
       
def including_z_func(col, type_="DR", col_="1", Np=0, including_addition_horns=True):
    if type_=="DR":
        if col_=="1":
            if   Np==0:
                if not including_addition_horns:
                    z_ = np.array([ 44.59135295, 15.71811112, 7.91709484, 23.36712928, 55.63501811, 89.67552498, 101.83138369])
                else: 
                    z_ = np.array([ 44.59135295, 15.71811112, 7.91709484, 23.36712928, 55.63501811, 89.67552498, 101.83138369,122.])
            elif Np==1:
                z_ = np.array([ 46.89534499, 44.59135295, 42.33031493, 16.97402125, 15.71811112, 14.54730681,  7.70279924,
                                 7.91709484,  8.22500848, 21.79875782, 23.36712928, 25.00398793,   53.366951, 55.63501811,
                                57.91280196, 87.90039496, 89.67552498, 91.36796053,102.28007554,101.83138369,101.17394543])
            elif Np==2:
                z_ = np.array([ 49.23853957,  46.89534499,  44.59135295,  42.33031493, 40.11585098,  18.31338828,  16.97402125,  15.71811112,
                                14.54730681,  13.46312583,   7.58257443,   7.70279924,  7.91709484,   8.22500848,  13.83844265,  20.30142971,
                                21.79875782,  23.36712928,  25.00398793,  26.70664616, 51.11325934,  53.366951  ,  55.63501811,  57.91280196,
                                60.19551241,  86.04933175,  87.90039496,  89.67552498, 91.36796053,  92.97080895, 102.5288848 , 102.28007554,
                               101.83138369, 101.17394543, 100.29876553])
            else:
                raise ValueError
        elif col_=="2":
            if Np==0:
                if not including_addition_horns:
                    z_ = np.array([ 15.20353847,  -0.12719265,   7.78022685,  36.79861354,  76.18874766, 106.59937932, 100.0672262 ])
                else:
                    z_ = np.array([ 15.20353847,  -0.12719265,   7.78022685,  36.79861354,  76.18874766, 106.59937932, 100.0672262, -20])
            elif Np==1:
                z_ = np.array([ 16.83133323,  15.20353847,  13.64397876,   0.17417651,  -0.12719265,  -0.33499533,   6.6021731 ,   7.78022685,
                                 9.04353772,  34.52639182,  36.79861354,  39.11414234,  73.74586462,  76.18874766,  78.59934696, 105.44759372,
                               106.59937932, 107.6096496 , 102.20654883, 100.0672262 ,  97.64351594])
            elif Np==2:
                z_ = np.array([ 18.52466284,  16.83133323,  15.20353847,  13.64397876,  12.15522287,   0.56851451,   0.17417651,  -0.12719265,
                                -0.33499533,  -0.44876529,   5.51088135,   6.6021731 ,   7.78022685,   9.04353772,  10.39046942,  32.30108463,
                                34.52639182,  36.79861354,  39.11414234,  41.46923938,  71.27640784,  73.74586462,  76.18874766,  78.59934696,
                                80.97182112, 104.16210537, 105.44759372, 106.59937932, 107.6096496 , 108.47046063, 104.07139892, 102.20654883,
                               100.0672262 ,  97.64351594,  94.92537156])
            else:
                raise ValueError
        elif col_=="3":
            if Np==0:
                if not including_addition_horns:
                    z_ = np.array([  9.39975644,  -0.39299988,  13.32798554,  46.28252123,  85.57837979, 109.71130313,  88.56500087])
                else:
                    z_ = np.array([  9.39975644,  -0.39299988,  13.32798554,  46.28252123,  85.57837979, 109.71130313,  88.56500087,0])
                
            elif Np==1:
                z_ = np.array([ 10.73972531,   9.39975644,   8.13750933,  -0.4681677 ,  -0.39299988,  -0.22318902,  11.81924688,  13.32798554,
                                14.91464769,  43.86002947,  46.28252123,  48.73257622,  83.30020467,  85.57837979,  87.80011714, 109.17376641,
                               109.71130313, 110.07476031,  91.90267633,  88.56500087,  84.90196337])                
            elif Np==2:
                z_ = np.array([ 1.21552414e+01,  1.07397253e+01,  9.39975644e+00,  8.13750933e+00, 6.95502713e+00, -4.48764515e-01, -4.68167704e-01, -3.92999878e-01,
                               -2.23189015e-01,  4.12055096e-02,  1.03904622e+01,  1.18192469e+01, 1.33279855e+01,  1.49146477e+01,  1.65770714e+01,  4.14692340e+01,
                                4.38600295e+01,  4.62825212e+01,  4.87325762e+01,  5.12059300e+01, 8.09718274e+01,  8.33002047e+01,  8.55783798e+01,  8.78001171e+01,
                                8.99590497e+01,  1.08470488e+02,  1.09173766e+02,  1.09711303e+02, 1.10074760e+02,  1.10255668e+02,  9.49254305e+01,  9.19026763e+01,
                                8.85650009e+01,  8.49019634e+01,  8.09029917e+01])
            else:
                raise ValueError

        elif col_=="4":
            if Np==0:
                if not including_addition_horns:
                    z_ = np.array([35.8405432 , 11.56006271,  9.70391668, 30.29793287, 64.75589628,  95.87956614, 97.85866817])
                else:
                    z_ = np.array([35.8405432 , 11.56006271,  9.70391668, 30.29793287, 64.75589628,  95.87956614, 97.85866817,0])
                
            elif Np==1:
                z_ = np.array([37.95152905, 35.8405432 , 33.78620324, 12.46697302, 11.56006271,  10.74353991,  9.11918948,  9.70391668, 10.3791311 , 28.47226336,
                               30.29793287, 32.18055088, 62.47822649, 64.75589628, 67.02333393,  94.47709183, 95.87956614, 97.17098692, 99.19683711, 97.85866817,
                               96.27498356])
            elif Np==2:
                z_ = np.array([ 40.11593496,  37.95152905,  35.8405432 ,  33.78620324,  31.7916036 ,  13.46314756,  12.46697302,  11.56006271,
                                10.74353991,  10.0183965 ,  13.83842905,   9.11918948,   9.70391668,  10.3791311 ,  11.14372293,  26.70662416,
                                28.47226336,  30.29793287,  32.18055088,  34.11690416,  60.19550893,  62.47822649,  64.75589628,  67.02333393,
                                69.27522367,  92.97085091,  94.47709183,  95.87956614,  97.17098692,  98.34393586, 100.29887986,  99.19683711,
                                97.85866817,  96.27498356,  94.43626244])
            else:
                raise ValueError
        return {"x":col.T[:][0],"y":col.T[:][1],"z":z_}#np.array([col.T[:][0],col.T[:][1],z_]) 

def PCcolfeeds(PCHref,params,nup,ndown):#PCref=Ponto Central do Hexag de ref, nsup= feeds acima da referencia, ndown=feeds abaixo da referencia
                                        #A funcao retornarah os centros dos hexagonos da coluna
    PCcol   = PCHref  #Pontos centrais da coluna
    UPfeeds = np.arange(1,1+nup)
    DOfeeds = np.arange(1,1+ndown)
    
    for n in UPfeeds:
        PCUn   = PCHref+np.array([0,+n*params['DV']])
        PCcol  = np.vstack([PCUn,PCcol])
    for n in DOfeeds:
        PCDn   = PCHref+np.array([0,-n*params['DV']])
        PCcol  = np.vstack([PCcol,PCDn])
    return PCcol

def AdditionHorns(colhorns=None, params=None, up=False, down=False , type_="dashed"):
    i1 = np.intersect1d(a[0][:],b[0][:])
    i2 = np.intersect1d(a[1][:],b[1][:])
    np.intersect1d(i1,i2)
    return None
