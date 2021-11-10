from fastapi import FastAPI
import numpy as np

app = FastAPI()


#mm_20k = numpy.random.random((20000,20000))
mm_big = np.random.random((5000,5000))

def matrix_inverse_trace(msize: int):
    m = np.random.random((msize, msize))
    inversemat = np.linalg.inv(m)
    trace_of_mat = np.trace(inversemat)
    return trace_of_mat

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/loads/matrixinverse")
def read_item(msize: int):
    t = matrix_inverse_trace(msize)
    return {"matrix_trace": t}