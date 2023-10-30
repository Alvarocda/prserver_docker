#!/usr/bin/env python
# -*- coding: utf-8

# Copyright (C) 2010 Stefan Hacker <dd0t@users.sourceforge.net>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:

# - Redistributions of source code must retain the above copyright notice,
#   this list of conditions and the following disclaimer.
# - Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
# - Neither the name of the Mumble Developers nor the names of its
#   contributors may be used to endorse or promote products derived from this
#   software without specific prior written permission.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# `AS IS'' AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL THE FOUNDATION OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
# PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

#
# prbf2man.py
# This small programm is for creating a possible channel/acl structure for
# the mumo prbf2 module as well as the corresponding prbf2.ini configuration file.

import os
import sys
import tempfile
import ConfigParser
from optparse import OptionParser

# Default settings


import Ice
import IcePy


if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option('-t', '--target',
                      help = 'Host to connect to', default = "127.0.0.1")
    parser.add_option('-p', '--port',
                      help = 'Port to connect to', default = "6504")
    parser.add_option('-v', '--vserver',
                      help = 'Virtual server id', default = '1')
    parser.add_option('-i', '--ice',
                      help = 'Path to slice file', default = 'Murmur.ice')
    parser.add_option('-s', '--secret',
                      help = 'Ice secret', default = '')
    parser.add_option('-d', '--slicedir',
                      help = 'System slice directory used when getSliceDir is not available', default = '/usr/share/slice')
    (option, args) = parser.parse_args()
    
    host = option.target
    slicedir = option.slicedir
    try:
        port = int(option.port)
    except ValueError:
        print "Port value '%s' is invalid" % option.port
        sys.exit(1)
        
    try:
        sid = int(option.vserver)
        if sid < 1: raise ValueError
    except ValueError:
        print "Virtual server id value '%s' invalid" % option.vserver
        sys.exit(1)
        
    prxstr = "Meta:tcp -h %s -p %d -t 1000" % (host, port)
    secret = option.secret
    
    props = Ice.createProperties(sys.argv)
    props.setProperty("Ice.ImplicitContext", "Shared")
    idata = Ice.InitializationData()
    idata.properties = props
    
    ice = Ice.initialize(idata)
    prx = ice.stringToProxy(prxstr)
    print "Done"

    def lslice(slf):
        if not hasattr(Ice, "getSliceDir"):
            Ice.loadSlice('-I%s %s' % (slicedir, slf))
        else:
            Ice.loadSlice('', ['-I' + Ice.getSliceDir(), slf])
    
    try:
        print "Trying to retrieve slice dynamically from server...",
        op = IcePy.Operation('getSlice', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, True, (), (), (), IcePy._t_string, ())
        if hasattr(Ice, "getSliceDir"):
            slice = op.invoke(prx, ((), None))
        else:
            slice = op.invoke(prx, (), None)
        (dynslicefiledesc, dynslicefilepath)  = tempfile.mkstemp(suffix = '.ice')
        dynslicefile = os.fdopen(dynslicefiledesc, 'w')
        dynslicefile.write(slice)
        dynslicefile.flush()
        lslice(dynslicefilepath)
        dynslicefile.close()
        os.remove(dynslicefilepath)
        print "Success"
    except Exception, e:
        print "Failed"
        print str(e)
        slicefile = option.ice
        print "Load slice (%s)..." % slicefile,
        lslice(slicefile)
        print "Done"
    
    print "Import dynamically compiled murmur class...",
    import Murmur
    print "Done"
    print "Establish ice connection...",
    
    if secret:
        print "[protected]...",
        ice.getImplicitContext().put("secret", secret)
    
    murmur = Murmur.MetaPrx.checkedCast(prx)
    print "Done"
    
    print "Get server...",
    server = murmur.getServer(sid)
    print "Done (%d)" % sid

    ACL = Murmur.ACL
    WA = Murmur.PermissionWrite
    EAT = Murmur.PermissionEnter | Murmur.PermissionTraverse
    TR = Murmur.PermissionTraverse
    W = Murmur.PermissionWhisper
    S = Murmur.PermissionSpeak
    MD = Murmur.PermissionMuteDeafen
    M = Murmur.PermissionMove
    C = Murmur.PermissionMakeChannel
    T = Murmur.PermissionTextMessage
    RU = Murmur.PermissionRegister
    RS = Murmur.PermissionRegisterSelf
    
    print "Creating initial channel structure:"

    print " Root"
    server.setACL(0,
              [ACL(applyHere = True,
                   applySubs = True,
                   userid = -1,
                   group = 'admin',
                   allow = WA),
               ACL(applyHere = True,
                   applySubs = True,
                   userid = -1,
                   group = 'admin',
                   allow = RU),
               ACL(applyHere = True,
                   applySubs = False,
                   userid = -1,
                   group = 'all',
                   deny = S | W),
               ACL(applyHere = True,
                   applySubs = True,
                   userid = -1,
                   group = 'all',
                   deny = RS)],
               [], True)
    
    print " PR BF2 Game Servers"
    gamechan = server.addChannel("PR BF2 Game Servers", 0)
    server.setACL(gamechan,
              [ACL(applyHere = True,
                   applySubs = True,
                   userid = -1,
                   group = 'all',
                   deny = S | W)],
               [], True)
    gamechanstate = server.getChannelState(gamechan)
    gamechanstate.position = 1
    server.setChannelState(gamechanstate)
    
    print " Lobby"
    lobby = server.addChannel("Lobby", 0)
    server.setACL(lobby,
              [ACL(applyHere = True,
                   applySubs = True,
                   userid = -1,
                   group = 'all',
                   deny = S | W)],
               [], True)
    lobbystate = server.getChannelState(lobby)
    lobbystate.position = 2
    server.setChannelState(lobbystate)

    print "Done"

