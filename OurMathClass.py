import math

# This class will try to replace the method we use
# in our method for diverse computation [not the calculator itself]
# instead of calling the regular math.<something> you will use OurMathClass.<something>
# if no implementation for the method you want to use is available:
# 1.create a field in the OurMathClass for the method you want
# 2. Make it point to the regular math.<something>
# 3. When we have an implementation for the math.<something> we will replace it in this class.


class OurMathClass:
    power = math.pow  # NOTE: will have to be changed with the power function of Zarren
    pi = math.pi
