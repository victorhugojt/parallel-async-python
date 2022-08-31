# parallel-async-python
Study multi-threading programming

```sh
virtualenv venv-multi-task
```

```sh
.\venv-multi-task\Scripts\activate
```

```sh
source venv-multi-task/bin/activate
```


```python
if io_bound:
    if io_very_slow:
        print("Use Asyncio")
    else:
        print("Use Threads")
else:
    print("Multi Processing")

```