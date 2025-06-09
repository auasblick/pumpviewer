# Auasblick Pump Curve Viewer

***Note: this branch is still under construction and has not even remotely received a satisfactory state***

This is a tool that provides the opportunity to dynamically view and adjust characteristic pump curves. It can create
new curves, and modify existing ones to find the most efficient pump in its most efficient operating state for a certain
use case.

To run this tool, follow these steps:<br>

1: navigate to your target directory and clone this repository
```
git clone https://github.com/auasblick/pumpviewer.git
```

2: create a virtual environment and install the dependencies
```
py -3.13 -m venv .venv
".venv\Scripts\activate"
pip install -r requirements.txt
```

3: start the application
```
python -m pump_curve_viewer
```


### UX:
These are the tabs and their application
 - Fitting
   - viewing characteristic pump curves
   - modification of the curves
   - export possibilities
 - Tracing
   - import of media
   - creation of pump curves
   - pump curve data management

### Pump collection file definition:
to be defined