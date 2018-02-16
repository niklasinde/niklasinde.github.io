


### To run pycharm like spyder:


In settings add the following code as "Starting script" (In settnings -> Build, Execution, Deployment -> Console -> Python Console:
```python
work_dir = WORKING_DIR_AND_PYTHON_PATHS
print(work_dir)
if type(work_dir) in [list, tuple]:
    def get_imp():
        imp = input()
        try:
            imp =int(imp)
        except:
            return get_imp()
        return imp
    inp = get_imp()
    work_dir = work_dir[inp]
```

This will create a variable work_dir so if you would like to run the file again quickly you create a makro.<br>
(Edit -> Makros -> start macro recording) writing the following:
```python
runfile(__file__, wdir=work_dir)
```
You can then later in settings -> keymap set a shortcmd to this makro.
