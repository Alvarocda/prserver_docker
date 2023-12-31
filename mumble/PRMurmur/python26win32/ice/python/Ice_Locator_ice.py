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
# Generated from file `Locator.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>

import Ice, IcePy, __builtin__
import Ice_Identity_ice
import Ice_ProcessF_ice

# Included module Ice
_M_Ice = Ice.openModule('Ice')

# Start of module Ice
__name__ = 'Ice'

if not _M_Ice.__dict__.has_key('AdapterNotFoundException'):
    _M_Ice.AdapterNotFoundException = Ice.createTempClass()
    class AdapterNotFoundException(Ice.UserException):
        '''This exception is raised if an adapter cannot be found.'''
        def __init__(self):
            pass

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_name = 'Ice::AdapterNotFoundException'

    _M_Ice._t_AdapterNotFoundException = IcePy.defineException('::Ice::AdapterNotFoundException', AdapterNotFoundException, (), None, ())
    AdapterNotFoundException._ice_type = _M_Ice._t_AdapterNotFoundException

    _M_Ice.AdapterNotFoundException = AdapterNotFoundException
    del AdapterNotFoundException

if not _M_Ice.__dict__.has_key('InvalidReplicaGroupIdException'):
    _M_Ice.InvalidReplicaGroupIdException = Ice.createTempClass()
    class InvalidReplicaGroupIdException(Ice.UserException):
        '''This exception is raised if the replica group provided by the
server is invalid.'''
        def __init__(self):
            pass

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_name = 'Ice::InvalidReplicaGroupIdException'

    _M_Ice._t_InvalidReplicaGroupIdException = IcePy.defineException('::Ice::InvalidReplicaGroupIdException', InvalidReplicaGroupIdException, (), None, ())
    InvalidReplicaGroupIdException._ice_type = _M_Ice._t_InvalidReplicaGroupIdException

    _M_Ice.InvalidReplicaGroupIdException = InvalidReplicaGroupIdException
    del InvalidReplicaGroupIdException

if not _M_Ice.__dict__.has_key('AdapterAlreadyActiveException'):
    _M_Ice.AdapterAlreadyActiveException = Ice.createTempClass()
    class AdapterAlreadyActiveException(Ice.UserException):
        '''This exception is raised if a server tries to set endpoints for
an adapter that is already active.'''
        def __init__(self):
            pass

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_name = 'Ice::AdapterAlreadyActiveException'

    _M_Ice._t_AdapterAlreadyActiveException = IcePy.defineException('::Ice::AdapterAlreadyActiveException', AdapterAlreadyActiveException, (), None, ())
    AdapterAlreadyActiveException._ice_type = _M_Ice._t_AdapterAlreadyActiveException

    _M_Ice.AdapterAlreadyActiveException = AdapterAlreadyActiveException
    del AdapterAlreadyActiveException

if not _M_Ice.__dict__.has_key('ObjectNotFoundException'):
    _M_Ice.ObjectNotFoundException = Ice.createTempClass()
    class ObjectNotFoundException(Ice.UserException):
        '''This exception is raised if an object cannot be found.'''
        def __init__(self):
            pass

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_name = 'Ice::ObjectNotFoundException'

    _M_Ice._t_ObjectNotFoundException = IcePy.defineException('::Ice::ObjectNotFoundException', ObjectNotFoundException, (), None, ())
    ObjectNotFoundException._ice_type = _M_Ice._t_ObjectNotFoundException

    _M_Ice.ObjectNotFoundException = ObjectNotFoundException
    del ObjectNotFoundException

if not _M_Ice.__dict__.has_key('ServerNotFoundException'):
    _M_Ice.ServerNotFoundException = Ice.createTempClass()
    class ServerNotFoundException(Ice.UserException):
        '''This exception is raised if a server cannot be found.'''
        def __init__(self):
            pass

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_name = 'Ice::ServerNotFoundException'

    _M_Ice._t_ServerNotFoundException = IcePy.defineException('::Ice::ServerNotFoundException', ServerNotFoundException, (), None, ())
    ServerNotFoundException._ice_type = _M_Ice._t_ServerNotFoundException

    _M_Ice.ServerNotFoundException = ServerNotFoundException
    del ServerNotFoundException

if not _M_Ice.__dict__.has_key('LocatorRegistry'):
    _M_Ice._t_LocatorRegistry = IcePy.declareClass('::Ice::LocatorRegistry')
    _M_Ice._t_LocatorRegistryPrx = IcePy.declareProxy('::Ice::LocatorRegistry')

if not _M_Ice.__dict__.has_key('Locator'):
    _M_Ice.Locator = Ice.createTempClass()
    class Locator(Ice.Object):
        '''The Ice locator interface. This interface is used by clients to
lookup adapters and objects. It is also used by servers to get the
locator registry proxy.

The Locator interface is intended to be used by
Ice internals and by locator implementations. Regular user code
should not attempt to use any functionality of this interface
directly.'''
        def __init__(self):
            if __builtin__.type(self) == _M_Ice.Locator:
                raise RuntimeError('Ice.Locator is an abstract class')

        def ice_ids(self, current=None):
            return ('::Ice::Locator', '::Ice::Object')

        def ice_id(self, current=None):
            return '::Ice::Locator'

        def ice_staticId():
            return '::Ice::Locator'
        ice_staticId = staticmethod(ice_staticId)

        def findObjectById_async(self, _cb, id, current=None):
            '''Find an object by identity and return its proxy.

Arguments:
    id The identity.

Returns:
    The proxy, or null if the object is not active.

Exceptions:
    ObjectNotFoundException Raised if the object cannot
be found.'''
            pass

        def findAdapterById_async(self, _cb, id, current=None):
            '''Find an adapter by id and return its proxy (a dummy direct
proxy created by the adapter).

Arguments:
    id The adapter id.

Returns:
    The adapter proxy, or null if the adapter is not active.

Exceptions:
    AdapterNotFoundException Raised if the adapter cannot be
found.'''
            pass

        def getRegistry(self, current=None):
            '''Get the locator registry.

Returns:
    The locator registry.'''
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_Ice._t_Locator)

        __repr__ = __str__

    _M_Ice.LocatorPrx = Ice.createTempClass()
    class LocatorPrx(Ice.ObjectPrx):

        '''Find an object by identity and return its proxy.

Arguments:
    id The identity.

Returns:
    The proxy, or null if the object is not active.

Exceptions:
    ObjectNotFoundException Raised if the object cannot
be found.'''
        def findObjectById(self, id, _ctx=None):
            return _M_Ice.Locator._op_findObjectById.invoke(self, ((id, ), _ctx))

        '''Find an object by identity and return its proxy.

Arguments:
    id The identity.

Returns:
    The proxy, or null if the object is not active.

Exceptions:
    ObjectNotFoundException Raised if the object cannot
be found.'''
        def begin_findObjectById(self, id, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_Ice.Locator._op_findObjectById.begin(self, ((id, ), _response, _ex, _sent, _ctx))

        '''Find an object by identity and return its proxy.

Arguments:
    id The identity.

Returns:
    The proxy, or null if the object is not active.

Exceptions:
    ObjectNotFoundException Raised if the object cannot
be found.'''
        def end_findObjectById(self, _r):
            return _M_Ice.Locator._op_findObjectById.end(self, _r)

        '''Find an object by identity and return its proxy.

Arguments:
    id The identity.

Returns:
    The proxy, or null if the object is not active.

Exceptions:
    ObjectNotFoundException Raised if the object cannot
be found.'''
        def findObjectById_async(self, _cb, id, _ctx=None):
            return _M_Ice.Locator._op_findObjectById.invokeAsync(self, (_cb, (id, ), _ctx))

        '''Find an adapter by id and return its proxy (a dummy direct
proxy created by the adapter).

Arguments:
    id The adapter id.

Returns:
    The adapter proxy, or null if the adapter is not active.

Exceptions:
    AdapterNotFoundException Raised if the adapter cannot be
found.'''
        def findAdapterById(self, id, _ctx=None):
            return _M_Ice.Locator._op_findAdapterById.invoke(self, ((id, ), _ctx))

        '''Find an adapter by id and return its proxy (a dummy direct
proxy created by the adapter).

Arguments:
    id The adapter id.

Returns:
    The adapter proxy, or null if the adapter is not active.

Exceptions:
    AdapterNotFoundException Raised if the adapter cannot be
found.'''
        def begin_findAdapterById(self, id, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_Ice.Locator._op_findAdapterById.begin(self, ((id, ), _response, _ex, _sent, _ctx))

        '''Find an adapter by id and return its proxy (a dummy direct
proxy created by the adapter).

Arguments:
    id The adapter id.

Returns:
    The adapter proxy, or null if the adapter is not active.

Exceptions:
    AdapterNotFoundException Raised if the adapter cannot be
found.'''
        def end_findAdapterById(self, _r):
            return _M_Ice.Locator._op_findAdapterById.end(self, _r)

        '''Find an adapter by id and return its proxy (a dummy direct
proxy created by the adapter).

Arguments:
    id The adapter id.

Returns:
    The adapter proxy, or null if the adapter is not active.

Exceptions:
    AdapterNotFoundException Raised if the adapter cannot be
found.'''
        def findAdapterById_async(self, _cb, id, _ctx=None):
            return _M_Ice.Locator._op_findAdapterById.invokeAsync(self, (_cb, (id, ), _ctx))

        '''Get the locator registry.

Returns:
    The locator registry.'''
        def getRegistry(self, _ctx=None):
            return _M_Ice.Locator._op_getRegistry.invoke(self, ((), _ctx))

        '''Get the locator registry.

Returns:
    The locator registry.'''
        def begin_getRegistry(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_Ice.Locator._op_getRegistry.begin(self, ((), _response, _ex, _sent, _ctx))

        '''Get the locator registry.

Returns:
    The locator registry.'''
        def end_getRegistry(self, _r):
            return _M_Ice.Locator._op_getRegistry.end(self, _r)

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_Ice.LocatorPrx.ice_checkedCast(proxy, '::Ice::Locator', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_Ice.LocatorPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_Ice._t_LocatorPrx = IcePy.defineProxy('::Ice::Locator', LocatorPrx)

    _M_Ice._t_Locator = IcePy.defineClass('::Ice::Locator', Locator, (), True, None, (), ())
    Locator._ice_type = _M_Ice._t_Locator

    Locator._op_findObjectById = IcePy.Operation('findObjectById', Ice.OperationMode.Idempotent, Ice.OperationMode.Nonmutating, True, (), (((), _M_Ice._t_Identity),), (), IcePy._t_ObjectPrx, (_M_Ice._t_ObjectNotFoundException,))
    Locator._op_findAdapterById = IcePy.Operation('findAdapterById', Ice.OperationMode.Idempotent, Ice.OperationMode.Nonmutating, True, (), (((), IcePy._t_string),), (), IcePy._t_ObjectPrx, (_M_Ice._t_AdapterNotFoundException,))
    Locator._op_getRegistry = IcePy.Operation('getRegistry', Ice.OperationMode.Idempotent, Ice.OperationMode.Nonmutating, False, (), (), (), _M_Ice._t_LocatorRegistryPrx, ())

    _M_Ice.Locator = Locator
    del Locator

    _M_Ice.LocatorPrx = LocatorPrx
    del LocatorPrx

if not _M_Ice.__dict__.has_key('LocatorRegistry'):
    _M_Ice.LocatorRegistry = Ice.createTempClass()
    class LocatorRegistry(Ice.Object):
        '''The Ice locator registry interface. This interface is used by
servers to register adapter endpoints with the locator.

 The LocatorRegistry interface is intended to be used
by Ice internals and by locator implementations. Regular user
code should not attempt to use any functionality of this interface
directly.'''
        def __init__(self):
            if __builtin__.type(self) == _M_Ice.LocatorRegistry:
                raise RuntimeError('Ice.LocatorRegistry is an abstract class')

        def ice_ids(self, current=None):
            return ('::Ice::LocatorRegistry', '::Ice::Object')

        def ice_id(self, current=None):
            return '::Ice::LocatorRegistry'

        def ice_staticId():
            return '::Ice::LocatorRegistry'
        ice_staticId = staticmethod(ice_staticId)

        def setAdapterDirectProxy_async(self, _cb, id, proxy, current=None):
            '''Set the adapter endpoints with the locator registry.

Arguments:
    id The adapter id.

    proxy The adapter proxy (a dummy direct proxy created
by the adapter). The direct proxy contains the adapter
endpoints.

Exceptions:
    AdapterNotFoundException Raised if the adapter cannot
be found, or if the locator only allows
registered adapters to set their active proxy and the
adapter is not registered with the locator.

    AdapterAlreadyActiveException Raised if an adapter with the same
id is already active.'''
            pass

        def setReplicatedAdapterDirectProxy_async(self, _cb, adapterId, replicaGroupId, p, current=None):
            '''Set the adapter endpoints with the locator registry.

Arguments:
    adapterId The adapter id.

    replicaGroupId The replica group id.

    p The adapter proxy (a dummy direct proxy created
by the adapter). The direct proxy contains the adapter
endpoints.

Exceptions:
    AdapterNotFoundException Raised if the adapter cannot
be found, or if the locator only allows registered adapters to
set their active proxy and the adapter is not registered with
the locator.

    AdapterAlreadyActiveException Raised if an adapter with the same
id is already active.

    InvalidReplicaGroupIdException Raised if the given
replica group doesn't match the one registered with the
locator registry for this object adapter.'''
            pass

        def setServerProcessProxy_async(self, _cb, id, proxy, current=None):
            '''Set the process proxy for a server.

Arguments:
    id The server id.

    proxy The process proxy.

Exceptions:
    ServerNotFoundException Raised if the server cannot
be found.'''
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_Ice._t_LocatorRegistry)

        __repr__ = __str__

    _M_Ice.LocatorRegistryPrx = Ice.createTempClass()
    class LocatorRegistryPrx(Ice.ObjectPrx):

        '''Set the adapter endpoints with the locator registry.

Arguments:
    id The adapter id.

    proxy The adapter proxy (a dummy direct proxy created
by the adapter). The direct proxy contains the adapter
endpoints.

Exceptions:
    AdapterNotFoundException Raised if the adapter cannot
be found, or if the locator only allows
registered adapters to set their active proxy and the
adapter is not registered with the locator.

    AdapterAlreadyActiveException Raised if an adapter with the same
id is already active.'''
        def setAdapterDirectProxy(self, id, proxy, _ctx=None):
            return _M_Ice.LocatorRegistry._op_setAdapterDirectProxy.invoke(self, ((id, proxy), _ctx))

        '''Set the adapter endpoints with the locator registry.

Arguments:
    id The adapter id.

    proxy The adapter proxy (a dummy direct proxy created
by the adapter). The direct proxy contains the adapter
endpoints.

Exceptions:
    AdapterNotFoundException Raised if the adapter cannot
be found, or if the locator only allows
registered adapters to set their active proxy and the
adapter is not registered with the locator.

    AdapterAlreadyActiveException Raised if an adapter with the same
id is already active.'''
        def begin_setAdapterDirectProxy(self, id, proxy, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_Ice.LocatorRegistry._op_setAdapterDirectProxy.begin(self, ((id, proxy), _response, _ex, _sent, _ctx))

        '''Set the adapter endpoints with the locator registry.

Arguments:
    id The adapter id.

    proxy The adapter proxy (a dummy direct proxy created
by the adapter). The direct proxy contains the adapter
endpoints.

Exceptions:
    AdapterNotFoundException Raised if the adapter cannot
be found, or if the locator only allows
registered adapters to set their active proxy and the
adapter is not registered with the locator.

    AdapterAlreadyActiveException Raised if an adapter with the same
id is already active.'''
        def end_setAdapterDirectProxy(self, _r):
            return _M_Ice.LocatorRegistry._op_setAdapterDirectProxy.end(self, _r)

        '''Set the adapter endpoints with the locator registry.

Arguments:
    id The adapter id.

    proxy The adapter proxy (a dummy direct proxy created
by the adapter). The direct proxy contains the adapter
endpoints.

Exceptions:
    AdapterNotFoundException Raised if the adapter cannot
be found, or if the locator only allows
registered adapters to set their active proxy and the
adapter is not registered with the locator.

    AdapterAlreadyActiveException Raised if an adapter with the same
id is already active.'''
        def setAdapterDirectProxy_async(self, _cb, id, proxy, _ctx=None):
            return _M_Ice.LocatorRegistry._op_setAdapterDirectProxy.invokeAsync(self, (_cb, (id, proxy), _ctx))

        '''Set the adapter endpoints with the locator registry.

Arguments:
    adapterId The adapter id.

    replicaGroupId The replica group id.

    p The adapter proxy (a dummy direct proxy created
by the adapter). The direct proxy contains the adapter
endpoints.

Exceptions:
    AdapterNotFoundException Raised if the adapter cannot
be found, or if the locator only allows registered adapters to
set their active proxy and the adapter is not registered with
the locator.

    AdapterAlreadyActiveException Raised if an adapter with the same
id is already active.

    InvalidReplicaGroupIdException Raised if the given
replica group doesn't match the one registered with the
locator registry for this object adapter.'''
        def setReplicatedAdapterDirectProxy(self, adapterId, replicaGroupId, p, _ctx=None):
            return _M_Ice.LocatorRegistry._op_setReplicatedAdapterDirectProxy.invoke(self, ((adapterId, replicaGroupId, p), _ctx))

        '''Set the adapter endpoints with the locator registry.

Arguments:
    adapterId The adapter id.

    replicaGroupId The replica group id.

    p The adapter proxy (a dummy direct proxy created
by the adapter). The direct proxy contains the adapter
endpoints.

Exceptions:
    AdapterNotFoundException Raised if the adapter cannot
be found, or if the locator only allows registered adapters to
set their active proxy and the adapter is not registered with
the locator.

    AdapterAlreadyActiveException Raised if an adapter with the same
id is already active.

    InvalidReplicaGroupIdException Raised if the given
replica group doesn't match the one registered with the
locator registry for this object adapter.'''
        def begin_setReplicatedAdapterDirectProxy(self, adapterId, replicaGroupId, p, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_Ice.LocatorRegistry._op_setReplicatedAdapterDirectProxy.begin(self, ((adapterId, replicaGroupId, p), _response, _ex, _sent, _ctx))

        '''Set the adapter endpoints with the locator registry.

Arguments:
    adapterId The adapter id.

    replicaGroupId The replica group id.

    p The adapter proxy (a dummy direct proxy created
by the adapter). The direct proxy contains the adapter
endpoints.

Exceptions:
    AdapterNotFoundException Raised if the adapter cannot
be found, or if the locator only allows registered adapters to
set their active proxy and the adapter is not registered with
the locator.

    AdapterAlreadyActiveException Raised if an adapter with the same
id is already active.

    InvalidReplicaGroupIdException Raised if the given
replica group doesn't match the one registered with the
locator registry for this object adapter.'''
        def end_setReplicatedAdapterDirectProxy(self, _r):
            return _M_Ice.LocatorRegistry._op_setReplicatedAdapterDirectProxy.end(self, _r)

        '''Set the adapter endpoints with the locator registry.

Arguments:
    adapterId The adapter id.

    replicaGroupId The replica group id.

    p The adapter proxy (a dummy direct proxy created
by the adapter). The direct proxy contains the adapter
endpoints.

Exceptions:
    AdapterNotFoundException Raised if the adapter cannot
be found, or if the locator only allows registered adapters to
set their active proxy and the adapter is not registered with
the locator.

    AdapterAlreadyActiveException Raised if an adapter with the same
id is already active.

    InvalidReplicaGroupIdException Raised if the given
replica group doesn't match the one registered with the
locator registry for this object adapter.'''
        def setReplicatedAdapterDirectProxy_async(self, _cb, adapterId, replicaGroupId, p, _ctx=None):
            return _M_Ice.LocatorRegistry._op_setReplicatedAdapterDirectProxy.invokeAsync(self, (_cb, (adapterId, replicaGroupId, p), _ctx))

        '''Set the process proxy for a server.

Arguments:
    id The server id.

    proxy The process proxy.

Exceptions:
    ServerNotFoundException Raised if the server cannot
be found.'''
        def setServerProcessProxy(self, id, proxy, _ctx=None):
            return _M_Ice.LocatorRegistry._op_setServerProcessProxy.invoke(self, ((id, proxy), _ctx))

        '''Set the process proxy for a server.

Arguments:
    id The server id.

    proxy The process proxy.

Exceptions:
    ServerNotFoundException Raised if the server cannot
be found.'''
        def begin_setServerProcessProxy(self, id, proxy, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_Ice.LocatorRegistry._op_setServerProcessProxy.begin(self, ((id, proxy), _response, _ex, _sent, _ctx))

        '''Set the process proxy for a server.

Arguments:
    id The server id.

    proxy The process proxy.

Exceptions:
    ServerNotFoundException Raised if the server cannot
be found.'''
        def end_setServerProcessProxy(self, _r):
            return _M_Ice.LocatorRegistry._op_setServerProcessProxy.end(self, _r)

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_Ice.LocatorRegistryPrx.ice_checkedCast(proxy, '::Ice::LocatorRegistry', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_Ice.LocatorRegistryPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_Ice._t_LocatorRegistryPrx = IcePy.defineProxy('::Ice::LocatorRegistry', LocatorRegistryPrx)

    _M_Ice._t_LocatorRegistry = IcePy.defineClass('::Ice::LocatorRegistry', LocatorRegistry, (), True, None, (), ())
    LocatorRegistry._ice_type = _M_Ice._t_LocatorRegistry

    LocatorRegistry._op_setAdapterDirectProxy = IcePy.Operation('setAdapterDirectProxy', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, True, (), (((), IcePy._t_string), ((), IcePy._t_ObjectPrx)), (), None, (_M_Ice._t_AdapterNotFoundException, _M_Ice._t_AdapterAlreadyActiveException))
    LocatorRegistry._op_setReplicatedAdapterDirectProxy = IcePy.Operation('setReplicatedAdapterDirectProxy', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, True, (), (((), IcePy._t_string), ((), IcePy._t_string), ((), IcePy._t_ObjectPrx)), (), None, (_M_Ice._t_AdapterNotFoundException, _M_Ice._t_AdapterAlreadyActiveException, _M_Ice._t_InvalidReplicaGroupIdException))
    LocatorRegistry._op_setServerProcessProxy = IcePy.Operation('setServerProcessProxy', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, True, (), (((), IcePy._t_string), ((), _M_Ice._t_ProcessPrx)), (), None, (_M_Ice._t_ServerNotFoundException,))

    _M_Ice.LocatorRegistry = LocatorRegistry
    del LocatorRegistry

    _M_Ice.LocatorRegistryPrx = LocatorRegistryPrx
    del LocatorRegistryPrx

# End of module Ice
