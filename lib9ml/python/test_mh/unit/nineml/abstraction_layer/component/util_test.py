

# Automatically Generated Testing Skeleton Template:
import warnings
import unittest
import nineml




# Testing Skeleton for function:


def test_parse():
    # Signature: name(filename)
	# Left over from orignal Version. This will be deprecated

    warnings.warn('Tests not implemented')
    # raise NotImplementedError()







# Testing Skeleton for class: MathUtil

class MathUtil_test(object):
    
    def test_Constructor(self):
        pass


    def test_get_prefixed_rhs_string(self):
        # Signature: name(cls, expr_obj, prefix='', exclude=None)
		# No Docstring
        warnings.warn('Tests not implemented')
        # raise NotImplementedError()


    def test_get_rhs_substituted(self):
        # Signature: name(cls, expr_obj, namemap)
		# No Docstring
        warnings.warn('Tests not implemented')
        # raise NotImplementedError()


    def test_is_single_symbol(self):
        # Signature: name(cls, expr)
		# Returns ``True`` if the expression is a single symbol, possibly
		# surrounded with white-spaces
		# 
		# >>> is_single_symbol('hello')
		# True
		# 
		# >>> is_single_symbol('hello * world')
		# False
        warnings.warn('Tests not implemented')
        # raise NotImplementedError()


    def test_str_expr_replacement(self):
        # Signature: name(cls, frm, to, expr_string, func_ok=False)
		# replaces all occurences of name 'frm' with 'to' in expr_string
		# ('frm' may not occur as a function name on the rhs) ...
		# 'to' can be an arbitrary string so this function can also be used for
		# argument substitution.
		# 
		# Returns the resulting string. 
        warnings.warn('Tests not implemented')
        # raise NotImplementedError()








# Testing Skeleton for class: StrToExpr

class StrToExpr_test(object):
    
    def test_Constructor(self):
        pass


    def test_alias(self):
        # Signature: name(cls, alias_string)
		# Creates an Alias object from a string
        warnings.warn('Tests not implemented')
        # raise NotImplementedError()


    def test_is_alias(self):
        # Signature: name(cls, alias_string)
		# Returns True if the string could be an alias
        warnings.warn('Tests not implemented')
        # raise NotImplementedError()


    def test_state_assignment(self):
        # Signature: name(cls, state_assignment_string)
		# No Docstring
        warnings.warn('Tests not implemented')
        # raise NotImplementedError()


    def test_time_derivative(self):
        # Signature: name(cls, time_derivative_string)
		# Creates an TimeDerivative object from a string
        warnings.warn('Tests not implemented')
        # raise NotImplementedError()







