
---

## 2D Turbulent Flow Simulation 1.0

---

**The Basis** 

*Greetings!*
I intend to use this platform to document (trials, tribulations and all) the creation of a two-dimensional simulation of turbulent flow after stumbling across these two pretty representations of turbulent flow on YouTube:

> * [Fluid Simulation C++ / SFML](https://www.youtube.com/watch?v=XIvO_tzBIMw)
> * [MATLAB 2D Fluid Simulation](https://www.youtube.com/watch?v=cM47L5RddsM)

---
**Establishing the Foundations** 
```python
class Foundations: 

        primary = "University-level fluid mechanics knowledge"
        secondary = "Navier-Stokes equations" 
        tertiary = "Turbulence models/PDE's"
        
        projectList = [primary, secondary, tertiary]
            
foundations = Foundations()

for i in range (0, len(foundations.projectList)):
    
    print (foundations.projectList[i])
```

---

**Methodology**

As of now, simulation will not include pertubations caused by vegetation, rocks etc. as it normally would be the case in open channel flow. This is a ***'learn-as-I-go'*** project so the focus is to first, achieve a simple version of the model *before* adding additonal features to make it a better representation of turbulent flow in real-world context. 

