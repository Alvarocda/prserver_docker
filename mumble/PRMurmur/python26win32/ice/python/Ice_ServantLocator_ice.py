# **********************************************************************
#
# Copyright (c) 2003-2010 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************

# Ice version 3.4.1

# <auto-generated>
#
# Generated from file `ServantLocator.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>

import Ice, IcePy, __builtin__
import Ice_ObjectAdapterF_ice
import Ice_Current_ice

# Included module Ice
_M_Ice = Ice.openModule('Ice')

# Start of module Ice
__name__ = 'Ice'

if not _M_Ice.__dict__.has_key('ServantLocator'):
    _M_Ice.ServantLocator = Ice.createTempClass()
    class ServantLocator(object):
        '''A servant locator is called by an object adapter to
locate a servant that is not found in its active servant map.'''
        def __init__(self):
            if __builtin__.type(self) == _M_Ice.ServantLocator:
                raise RuntimeError('Ice.ServantLocator is an abstract class')

        def locate(self, curr):
            '''Called before a request is dispatched if a
servant cannot be found in the object adapter's active servant
map. Note that the object adapter does not automatically insert
the returned servant into its active servant map. This must be
done by the servant locator implementation, if this is desired.

locate can throw any user exception. If it does, that exception
is marshaled back to the client. If the Slice definition for the
corresponding operation includes that user exception, the client
receives that user exception; otherwise, the client receives
UnknownUserException.

If locate throws any exception, the Ice run time does not
call finished.

If you call locate from your own code, you
must also call finished when you have finished using the
servant, provided that locate returned a non-null servant;
otherwise, you will get undefined behavior if you use
servant locators such as the Freeze.Evictor.

Arguments:
    curr Information about the current operation for which
a servant is required.

    cookie A "cookie" that will be passed to finished.

Returns:
    The located servant, or null if no suitable servant has
been found.'''
            pass

        def finished(self, curr, servant, cookie):
            '''Called by the object adapter after a request has been
made. This operation is only called if locate was called
prior to the request and returned a non-null servant. This
operation can be used for cleanup purposes after a request.

finished can throw any user exception. If it does, that exception
is marshaled back to the client. If the Slice definition for the
corresponding operation includes that user exception, the client
receives that user exception; otherwise, the client receives
UnknownUserException.

If both the operation and finished throw an exception, the
exception thrown by finished is marshaled back to the client.

Arguments:
    curr Information about the current operation call for
which a servant was located by locate.

    servant The servant that was returned by locate.

    cookie The cookie that was returned by locate.'''
            pass

        def deactivate(self, category):
            '''Called when the object adapter in which this servant locator is
installed is deactivated.

Arguments:
    category Indicates for which category the servant locator
is being deactivated.'''
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_Ice._t_ServantLocator)

        __repr__ = __str__

    _M_Ice._t_ServantLocator = IcePy.defineClass('::Ice::ServantLocator', ServantLocator, (), True, None, (), ())
    ServantLocator._ice_type = _M_Ice._t_ServantLocator

    _M_Ice.ServantLocator = ServantLocator
    del ServantLocator

# End of module Ice
