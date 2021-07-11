
## 2D Turbulent Flow Simulation 1.0 :ocean:

---

**The Basis** 

*Greetings!*
After stumbling across these pretty 2D fluid simulations on YouTube:

> * [Fluid Simulation C++ / SFML](https://www.youtube.com/watch?v=XIvO_tzBIMw)
> * [MATLAB 2D Fluid Simulation](https://www.youtube.com/watch?v=cM47L5RddsM)  

I was compelled to try and program one myself - from scratch.  
I intend to use this platform to document (trials, tribulations and all) the creation of the 2D simulation of turbulent flow. 

---

**Establishing the Foundations** 
```python
class Foundations: 

        primary = "University-level fluid mechanics knowledge"
        secondary = "Navier-Stokes equations" 
        tertiary = "Turbulence models/PDE's"
        
        projectList = [primary, secondary, tertiary]

for i in range (0, len(Foundations().projectList)):
    
    print (Foundations().projectList[i])
```

---

**Methodology**

As of now, it will not include pertubations caused by vegetation, rocks etc., i.e. as it normally would be the case in open channel flow.  
This is a ***'learn-as-I-go'*** project so the focus is to first, achieve a simple version of the model *before* adding additional features to make it a better representation of turbulent flow in real-world context. 

