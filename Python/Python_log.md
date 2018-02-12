#### logging level
 - DEBUG , INFO, WARNING, ERROR, CRITICAL
 - log inactive: logging.disable(logging.CRITICAL)


```python
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.basicConfig(filename='myLog.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

logging.debug('Start of program')
```

