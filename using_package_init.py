#!/usr/bin/env python
import my_package

try:
    my_package.module_a.function_a()
    my_package.module_b.function_b()
    print()
except AttributeError as err:
    print("modules not available via my_package")


from my_package import module_a
module_a.function_a()
print()

from my_package.module_a import function_a
function_a()

