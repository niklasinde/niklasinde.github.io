


### To run pycharm like spyder:


In settings add the following code as "Starting script":

```python
import sys;
print('Python %s on %s' % (sys.version, sys.platform))
sys.path.extend([WORKING_DIR_AND_PYTHON_PATHS])

work_dir = WORKING_DIR_AND_PYTHON_PATHS
print(work_dir)
if type(work_dir) in [list, tuple]:
    inp = int(input())
    work_dir = work_dir[inp]
```
This will create a variable work_dir so if you would like to run the file again quickly you create a makro <br>
(Edit -> Makros -> start macro recording) writing the following:
```python
runfile(__file__, wdir=work_dir)
```
You can then later in settings -> keymap set a shortcmd to this makro.
