
## 2D Fluid Simulation 1.0 :ocean:

---

**The Basis** 

*Greetings!*
After stumbling across these pretty 2D fluid simulations on YouTube:

> * [Fluid Simulation C++ / SFML](https://www.youtube.com/watch?v=XIvO_tzBIMw)
> * [MATLAB 2D Fluid Simulation](https://www.youtube.com/watch?v=cM47L5RddsM) 
> * [Kelvin-Helmholtz instability with OpenFOAM](https://www.youtube.com/watch?v=gSK76eLUn6k) 

I was compelled to try and program one myself - from scratch.  
I intend to use this platform to document (trials, tribulations and all) the creation of a 2D Kelvin-Helmhortz instability simulation. 

---

**Establishing the Foundations** 
```python
class Foundations: 

        primary = "Kelvin Helmhortz Instability"
        secondary = "Finite Volume Method"
      
        projectList = [primary, secondary]

for i in range (0, len(Foundations().projectList)):
    
    print (Foundations().projectList[i])
```

---

**Methodology**

This is a ***'learn-as-I-go'*** project so the focus is to first, achieve a simple version of the model *before* adding additional features.

