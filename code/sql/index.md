```python
query.statement.compile(compile_kwargs={"literal_binds": True})
```


```python
import logging

sqlalchemy_logger = logging.getLogger('sqlalchemy.engine')
sqlalchemy_logger.setLevel(logging.INFO)

file_handler = logging.FileHandler('application.log')  # Set log file name
sqlalchemy_logger.addHandler(file_handler)

```


