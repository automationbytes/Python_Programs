#Assignment Operator
'''
+ - addition
- - subtraction
* - multiplication
/ - division (decimal point)
// - Floor division (quotient value)
** - power off (exponentional)
% - mod (remainder)

'''

a = 10
b = 2
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)#quotient
print(a%b)#remainder
print(a**b)#10^3

#comparsion operator
'''
== - equal to
!= not equal to
<,> <= ,>=
'''
a = 5
b = 3
print(a==b)
print(a!=b)
print(a<b)
print(a>b)
print(a<=b)
print(a>=b)

#logical operator
'''
and
or
not

True and True = True
True and False = False
False and True = False
False and False = False

True or True = True
True or False = True
False or True = True
False or False = False
'''
a = 10
b = 40
c = 100
print (not(a<b and a<c))
print(a<b or a==c)

'''
Membership Operator
in
not in
'''

fruit = {"Apple","Banana","Orange"}
print("Stawberry" not in fruit)

'''
identity operator
is
not is
'''
a = 10
b = 10.0
print(a is b)
'''
assignment operator

'''
a = 5
a += 10 # a = a+10
print(a)

a //=3
print(a)

#bitwise operator

a = 5 #101
b = 3 #011
print(a & b)#001
print(a | b)#111
'''
1 & 1 = 1
1 & 0 = 0
0 & 1 = 0
0 & 0 = 0

1 | 1 = 1
1 | 0 = 1
0 | 1 = 1
0 | 0 = 0

'''