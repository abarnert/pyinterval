# pyinterval

This is a fork of Stefano Taschini's [pyinterval 1.0b21](http://pyinterval.googlecode.com/).

This library provides a Python implementation of an algebraically closed interval system on the 
extended real number set. An interval object consists of a finite union of closed, possibly 
unbound, mathematical intervals.

Unlike most interval libraries, this one contains a suite of mathematical operations, implemented
using the [CRlibm](http://lipforge.ens-lyon.fr/www/crlibm/) library (which you will have to install
first, if you want these mathematical operations).

The library has been updated for Python 3.x, for standard crlibm installation locations, and to 
make setup work properly.
