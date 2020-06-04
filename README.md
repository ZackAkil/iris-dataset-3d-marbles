# Iris dataset 3d marbles
![bld](img/blendner_sklearn.png)
Using [Scikit-Learn](https://scikit-learn.org) with [Blender](https://www.blender.org) to render the iris dataset in 3d and create a physical simulation of a marble machine to classify the dataset.
![scene](img/1492.png)

## Installing Scikit-Learn in Blender (or any python library)
Blender 2.82 comes with python 3.7 and pip already, so you just have to find Blenders' python binary and run it's pip module.

On my mac I found it here:
```bash
cd /Applications/Blender.app/Contents/Resources/2.82/python/bin
```

Then to run that specific python binarys' `pip install` with the following:
```bash
./python3.7m -m pip install scikit-learn
```

I could also see all of Blenders' installed python packages at: `/Applications/Blender.app/Contents/Resources/2.82/python/lib/python3.7`
