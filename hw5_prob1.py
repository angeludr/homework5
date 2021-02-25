import numpy as np
import matplotlib.pyplot as plt

def functiontoIntegrate(x):
    """Function to test"""
    return x**2
    
def analyticIntegral(a = None, b = None):
   """The analytical integral of x**2"""
   return b**3/3 - a**3/3

def relativeError(true = None, estimate = None):
    """Returns the relative percent error between
    the approximated and true value"""
    return (np.abs(true - estimate) / np.abs(true)) * 100

def lefthandRiemann(f, a = None, b = None, n = None):
    """Returns the left hand reimann sum between
    0 and 1 in step sizes of n"""
    h = (b-a)/n
    
    s = 0
    
    for n in np.arange(n):
        s += f(a + n * h) + h
        s += h
        
    return s * h

def trapezoidal(f, a = None, b = None, n = None):
    """Returns the trapezoidal sum between
    0 and 1 in step sizes of n"""
    h = (b-a)/n
    
    s = 0
    
    for n in np.arange(n):
        s += 0.5 * (f(a + n * h) + f(a + (n + 1) * h))
    
    return s * h

def simpson(f, a = None, b = None, n = None):
    """Returns the simpson's sum between
    0 and 1 in step sizes of n"""
    h = (b-a)/n
    
    s = 0
    
    for n in np.arange(n):
        s += (f(a + n * h) + (4 * (f(a + (n + 1) * h))) + f(a + (n + 2) * h)) / 3
    
    return s * h / 2

if __name__ == "__main__":
    
    # Computes analytical integral between 0 and 1
    true = analyticIntegral(0, 1)
    
    # Integral parameters
    a = 0
    b = 1
    
    print('\n')
    
    # Using integration methods to compute 0 to 1 in step sizes of 10
    # Also takes percent error of each integration method to be appended into a list to graph later
    print('Integral Methods from 0 to 1 step size 10')
    
    lhr10 = lefthandRiemann(functiontoIntegrate, a, b, 10)
    print('Left Hand Reimann:', lhr10)
    
    lhr10Err = relativeError(true, lhr10)
    
    trap10 = trapezoidal(functiontoIntegrate, a, b, 10)
    print('Trapezoidal:', trap10)
    
    trap10Err = relativeError(true, trap10)
    
    simp10 = simpson(functiontoIntegrate, a, b, 10)
    print('Simpsons:', simp10)
    
    simp10Err = relativeError(true, simp10)
    
    print('\n')
    
    # Using integration methods to compute 0 to 1 in step sizes of 100
    # Also takes percent error of each integration method to be appended into a list to graph later
    print('Integral Methods from 0 to 1 step size 100')
    
    lhr100 = lefthandRiemann(functiontoIntegrate, a, b, 100)
    print('Left Hand Reimann:', lhr100)
    
    lhr100Err = relativeError(true, lhr100)
    
    trap100 = trapezoidal(functiontoIntegrate, a, b, 100)
    print('Trapezoidal:', trap100)
    
    trap100Err = relativeError(true, trap100)
    
    simp100 = simpson(functiontoIntegrate, a, b, 100)
    print('Simpsons:', simp100)
    
    simp100Err = relativeError(true, simp100)
    
    print('\n')
    
    # Using integration methods to compute 0 to 1 in step sizes of 1000
    # Also takes percent error of each integration method to be appended into a list to graph later
    print('Integral Methods from 0 to 1 step size 1k')
    
    lhr1k = lefthandRiemann(functiontoIntegrate, a, b, 1000)
    print('Left Hand Reimann:', lhr1k)
    
    lhr1kErr = relativeError(true, lhr1k)
    
    trap1k = trapezoidal(functiontoIntegrate, a, b, 1000)
    print('Trapezoidal:', trap1k)
    
    trap1kErr = relativeError(true, trap1k)
    
    simp1k = simpson(functiontoIntegrate, a, b, 1000)
    print('Simpsons:', simp1k)
    
    simp1kErr = relativeError(true, simp1k)
    
    print('\n')
    
    # Using integration methods to compute 0 to 1 in step sizes of 10000
    # Also takes percent error of each integration method to be appended into a list to graph later
    print('Integral Methods from 0 to 1 step size 10k')
    
    lhr10k = lefthandRiemann(functiontoIntegrate, a, b, 10000)
    print('Left Hand Reimann:', lhr10k)
    
    lhr10kErr = relativeError(true, lhr10k)
    
    trap10k = trapezoidal(functiontoIntegrate, a, b, 10000)
    print('Trapezoidal:', trap10k)
    
    trap10kErr = relativeError(true, trap10k)
    
    simp10k = simpson(functiontoIntegrate, a, b, 10000)
    print('Simpsons:', simp10k)
    
    simp10kErr = relativeError(true, simp10k)
    
    print('\n')


   # There is an empty list for each integration method and each will get the respective method with the step sizes of 10, 100, 1000, 10000 appended in
    lhrErr = []
    lhrErr.append(lhr10Err) ; lhrErr.append(lhr100Err) ; lhrErr.append(lhr1kErr); lhrErr.append(lhr10kErr)
    
    trapErr = []
    trapErr.append(trap10Err) ; trapErr.append(trap100Err) ; trapErr.append(trap1kErr); trapErr.append(trap10kErr)
    
    simpErr = []
    simpErr.append(simp10Err) ; simpErr.append(simp100Err) ; simpErr.append(simp1kErr); simpErr.append(simp10kErr)


    # Creating graph for percent errors of each integration method
    plt.style.use('dark_background')
     
    plt.title('Integration Methods and their Relative Error')
    
    plt.ylabel('Relative Error Values')
    plt.xlabel('Powers of 10 of # of steps between 0 and 1')
    
    plt.yscale('log')
    
    plt.plot(lhrErr, label = 'Left Hand Reimann')
    plt.plot(trapErr, label = 'Trapezoidal Method')
    plt.plot(simpErr, label = 'Simpsons Rule')
    
    plt.legend()
    
    plt.show()
