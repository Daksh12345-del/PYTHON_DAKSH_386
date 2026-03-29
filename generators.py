##Genrator funcion give genrator object doesnt store all value but the store the resources which make the value. it provide the value one by one when we ask for it. it is more memory efficient than list because it doesn't store all the values in memory at once. it is used to generate a sequence of values on the fly, which can be useful when working with large datasets or infinite sequences.
#Yield: we can create the generator by using the ield statement in a function. when the function is called, it returns a generator object. when the next() function is called on the generator object, the function executes until it reaches the yield statement, at which point it returns the value and pauses execution. the next time next() is called, the function resumes execution from where it left off, and continues until it reaches the next yield statement or the end of the function.
#Genrator offer other type of sequences such as list,tuple,dictionary
import time
def my_gen():
    for i in range(50000000):
        #Complex Computation
        yield i
init=time.time()
t1=time.time()-init
init=time.time()
print(t1)
# print(time.time()-init)
gen=my_gen()
# print(next(gen)) # Output: 0
# print(next(gen)) # Output: 1
# print(next(gen)) # Output: 2            
# print(next(gen)) # Output: 3
# print(next(gen)) # Output: 4
# print(next(gen)) # Output: StopIteration error because there are no more values to yield.
for j in gen:
    print(j)