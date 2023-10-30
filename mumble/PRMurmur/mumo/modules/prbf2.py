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
# prbf2.py
# This module manages ACL/channel movements based on PR:BF2
# gamestate reported by PRMumble
#

from mumo_module import (MumoModule,
                         x2bool)

import re
import sys
import time
import struct


try:
    from hashlib import sha1 as hashfunc
except: # Fallback for python < 2.6
    from _sha import new as hashfunc

try:
    import json
except ImportError: # Fallback for python < 2.6
    import simplejson as json

class prbf2(MumoModule):
    default_config = {'prbf2':(
                             ('gamecount', int, 1),
                             ('secret', str, ""),
                             ),
                      lambda x: re.match('g\d+', x):(
                             ('name', str, ''),
                             ('mumble_server', int, 1),
                             ('ipport_filter_negate', x2bool, False),
                             ('ipport_filter', str, ""), # support multiple ip's per channel for weird chinese servers :|
                             #('ipport_filter', re.compile, re.compile('.*')),
                             
                             ('base', int, 0),
                             ('left', int, -1),
                             
                             ('blufor', int, -1),
                             ('blufor_commander', int, -1),
                             ('blufor_no_squad', int, -1),
                             ('blufor_first_squad', int, -1),
                             ('blufor_first_squad_leader', int, -1),
                             ('blufor_second_squad', int, -1),
                             ('blufor_second_squad_leader', int, -1),
                             ('blufor_third_squad', int, -1),
                             ('blufor_third_squad_leader', int, -1),
                             ('blufor_fourth_squad', int, -1),
                             ('blufor_fourth_squad_leader', int, -1),
                             ('blufor_fifth_squad', int, -1),
                             ('blufor_fifth_squad_leader', int, -1),
                             ('blufor_sixth_squad', int, -1),
                             ('blufor_sixth_squad_leader', int, -1),
                             ('blufor_seventh_squad', int, -1),
                             ('blufor_seventh_squad_leader', int, -1),
                             ('blufor_eighth_squad', int, -1),
                             ('blufor_eighth_squad_leader', int, -1),
                             ('blufor_ninth_squad', int, -1),
                             ('blufor_ninth_squad_leader', int, -1),
                             
                             ('opfor', int, -1),
                             ('opfor_commander', int, -1),
                             ('opfor_no_squad', int, -1),
                             ('opfor_first_squad', int, -1),
                             ('opfor_first_squad_leader', int, -1),
                             ('opfor_second_squad', int, -1),
                             ('opfor_second_squad_leader', int, -1),
                             ('opfor_third_squad', int, -1),
                             ('opfor_third_squad_leader', int, -1),
                             ('opfor_fourth_squad', int, -1),
                             ('opfor_fourth_squad_leader', int, -1),
                             ('opfor_fifth_squad', int, -1),
                             ('opfor_fifth_squad_leader', int, -1),
                             ('opfor_sixth_squad', int, -1),
                             ('opfor_sixth_squad_leader', int, -1),
                             ('opfor_seventh_squad', int, -1),
                             ('opfor_seventh_squad_leader', int, -1),
                             ('opfor_eighth_squad', int, -1),
                             ('opfor_eighth_squad_leader', int, -1),
                             ('opfor_ninth_squad', int, -1),
                             ('opfor_ninth_squad_leader', int, -1)
                             ),
                    }
    
    id_to_squad_name = ["no", "first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth"]
    
    def __init__(self, name, manager, configuration = None):
        MumoModule.__init__(self, name, manager, configuration)
        self.murmur = manager.getMurmurModule()

    def connected(self):
        cfg = self.cfg()
        manager = self.manager()
        log = self.log()
        log.debug("Register for Server callbacks")
        
        servers = set()
        for i in range(cfg.prbf2.gamecount):
            try:
                servers.add(cfg["g%d" % i].mumble_server)
            except KeyError:
                log.error("Invalid configuration. Game configuration for 'g%d' not found.", i)
                return
        
        self.sessions = {} # {serverid:{sessionid:laststate}}
        manager.subscribeServerCallbacks(self, servers)
        manager.subscribeMetaCallbacks(self, servers)
    
    def disconnected(self): pass

    def ready(self, server):
        log = self.log()
        log.debug("prbf2 ready, handling existing users")
        
        self.sessions = {}
        for index, user in server.getUsers().items():
            self.handle(server, user)
    
    #
    #--- Module specific state handling code
    #
    def update_state(self, server, oldstate, newstate):
        log = self.log()
        sid = server.id()
        
        session = newstate.session
        newoldchannel = newstate.channel
        
        try:
            opc = oldstate.parsedcontext
            ogcfgname = opc["gamename"]
            ogcfg = opc["gamecfg"]
            og = ogcfg.name
            opi = oldstate.parsedidentity
        except (AttributeError, KeyError):
            og = None
            
            opi = {}
            opc = {}
            
        if oldstate and oldstate.is_linked:
            oli = True
        else:
            oli = False
        
        try:
            npc = newstate.parsedcontext
            ngcfgname = npc["gamename"]
            ngcfg = npc["gamecfg"]
            ng = ngcfg.name
            npi = newstate.parsedidentity
        except (AttributeError, KeyError):
            ng = None
            
            npi = {}
            npc = {}
            nli = False
        
        if newstate and newstate.is_linked:
            nli = True
        else:
            nli = False
        
        try:
            
            if not oli and nli:
                log.debug("User '%s' (%d|%d) on server %d now linked", newstate.name, newstate.session, newstate.userid, sid)
                server.addUserToGroup(0, session, "bf2_linked")

            if opi and opc:
                squadname = self.id_to_squad_name[opi["squad"]]
                log.debug("Removing user '%s' (%d|%d) on server %d from groups of game %s / squad %s", newstate.name, newstate.session, newstate.userid, sid, og or ogcfgname, squadname)
                server.removeUserFromGroup(ogcfg["base"], session, "bf2_%s_game" % (og or ogcfgname))
                server.removeUserFromGroup(ogcfg[opi["team"]], session, "bf2_commander")
                server.removeUserFromGroup(ogcfg[opi["team"]], session, "bf2_squad_leader")
                server.removeUserFromGroup(ogcfg[opi["team"]], session, "bf2_%s_squad_leader" % squadname)
                server.removeUserFromGroup(ogcfg[opi["team"]], session, "bf2_%s_squad" % squadname)
                server.removeUserFromGroup(ogcfg[opi["team"]], session, "bf2_team")
                channame = "left"
                newstate.channel = ogcfg["left"]
                
            if npc and npi and self.verifyIdentity(npi["hash"], npi["pass"]):
                log.debug("Updating user '%s' (%d|%d) on server %d in game %s: %s", newstate.name, newstate.session, newstate.userid, sid, ng or ngcfgname, str(npi))
                
                squadname = self.id_to_squad_name[npi["squad"]]
                
                # Add to game group
                location = "base"
                group = "bf2_%s_game" % (ng or ngcfgname)
                server.addUserToGroup(ngcfg[location], session, group)
                log.debug("Added '%s' @ %s to group %s in %s", newstate.name, ng or ngcfgname, group, location)
                
                # Then add to team group
                location = npi["team"]
                group = "bf2_team"
                server.addUserToGroup(ngcfg[location], session, group)
                log.debug("Added '%s' @ %s to group %s in %s", newstate.name, ng or ngcfgname, group, location)
                
                # Then add to squad group
                group = "bf2_%s_squad" % squadname
                server.addUserToGroup(ngcfg[location], session, group)
                log.debug("Added '%s' @ %s to group %s in %s", newstate.name, ng or ngcfgname, group, location)
                
                channame = "%s_%s_squad" % (npi["team"], self.id_to_squad_name[npi["squad"]])
                newstate.channel = ngcfg[channame]
                
                if npi["squad_leader"]:
                    # In case the leader flag is set add to leader group
                    group = "bf2_%s_squad_leader" % squadname
                    server.addUserToGroup(ngcfg[location], session, group)
                    log.debug("Added '%s' @ %s to group %s in %s", newstate.name, ng or ngcfgname, group, location)
                    
                    group = "bf2_squad_leader"
                    server.addUserToGroup(ngcfg[location], session, group)
                    log.debug("Added '%s' @ %s to group %s in %s", newstate.name, ng or ngcfgname, group, location)
                    
                    # Override previous moves
                    channame = "%s_%s_squad_leader" % (npi["team"], self.id_to_squad_name[npi["squad"]])
                    newstate.channel = ngcfg[channame]
                
                if npi["commander"]:
                    group = "bf2_commander"
                    server.addUserToGroup(ngcfg[location], session, group)
                    log.debug("Added '%s' @ %s to group %s in %s", newstate.name, ng or ngcfgname, group, location)
                    
                    group = "bf2_squad_leader"
                    server.addUserToGroup(ngcfg[location], session, group)
                    log.debug("Added '%s' @ %s to group %s in %s", newstate.name, ng or ngcfgname, group, location)
                    
                    # Override previous moves
                    channame = "%s_commander" % npi["team"]
                    newstate.channel = ngcfg[channame]
                    
            if oli and not nli:
                log.debug("User '%s' (%d|%d) on server %d no longer linked", newstate.name, newstate.session, newstate.userid, sid)
                server.removeUserFromGroup(0, session, "bf2_linked")
                    
            if newstate.channel >= 0 and newoldchannel != newstate.channel:
                if ng == None:
                    log.debug("Moving '%s' leaving %s to channel %s", newstate.name, og or ogcfgname, channame)
                else:
                    log.debug("Moving '%s' @ %s to channel %s", newstate.name, ng or ngcfgname, channame)
                    
                server.setState(newstate)
        except:
            log.warning("Exception raised: %s", sys.exc_info()[0])
            log.warning(str(sys.exc_traceback.tb_frame.f_code.co_filename) + " on line " + str(sys.exc_traceback.tb_lineno))
            self.userDisconnected(server, oldstate)
            self.userDisconnected(server, newstate)
        
    def handle(self, server, state):
        def verify(mdict, key, vtype):
            if not isinstance(mdict[key], vtype):
                raise ValueError("'%s' of invalid type" % key)
            
        if not state:
            return
        
        cfg = self.cfg()
        log = self.log()
        sid = server.id()
        
        # Add defaults for our variables to state
        state.parsedidentity = {}
        state.parsedcontext = {}
        state.is_linked = False
        
        if sid not in self.sessions: # Make sure there is a dict to store states in
            self.sessions[sid] = {}
        
        update = False
        if state.session in self.sessions[sid] and self.sessions[sid][state.session]:
            if state.identity != self.sessions[sid][state.session].identity or \
               state.context != self.sessions[sid][state.session].context:
                # identity or context changed => update
                update = True
            else: # id and context didn't change hence the old data must still be valid
                state.is_linked = self.sessions[sid][state.session].is_linked
                state.parsedcontext = self.sessions[sid][state.session].parsedcontext
                state.parsedidentity = self.sessions[sid][state.session].parsedidentity
        else:
            if state.identity or state.context:
                # New user with engaged plugin => update
                self.sessions[sid][state.session] = None
                update = True
                
        if not update:
            self.sessions[sid][state.session] = state
            return
            
        log.info("%s (%d|%d) %s", state.name, state.session, state.userid, state.context)
        # The plugin will always prefix "Project Reality: BF2\0" to the context for the PR:BF2 plugin
        # don't bother analyzing anything if it isn't there
        splitcontext = state.context.split('\0', 1)
        if splitcontext[0] == "Project Reality: BF2":
            state.is_linked = True
            if state.identity and len(splitcontext) == 1:
                #LEGACY: Assume broken Ice 3.2 which doesn't transmit context after \0
                splitcontext.append('{"ipport":""}') # Obviously this doesn't give full functionality but it doesn't crash either ;-)

        if state.is_linked and len(splitcontext) == 2 and state.identity: 
            try:
                context = json.loads(splitcontext[1])
                verify(context, "ipport", basestring)
                
                for i in range(cfg.prbf2.gamecount):
                    # Try to find a matching game
                    gamename = "g%d" % i
                    gamecfg = getattr(cfg, gamename)
                    
                    if gamecfg.mumble_server == server.id():
                        # support multiple ip's per channel for weird chinese servers :|
                        ipports = gamecfg.ipport_filter.split(',')
                        not_matched = True
                        for ipport in ipports:
                            if ipport == context["ipport"]:
                                not_matched = False
                                break
                        #not_matched = (gamecfg.ipport_filter.match(context["ipport"]) == None)
                        #if not_matched == gamecfg.ipport_filter_negate:
                        if not not_matched:
                            break
                    gamename = None
                
                if not gamename:
                    raise ValueError("No matching game found")
                
                context["gamecfg"] = gamecfg
                context["gamename"] = gamename
                state.parsedcontext = context

            except (ValueError, KeyError, AttributeError), e:
                log.debug("Invalid context for %s (%d|%d) on server %d: %s", state.name, state.session, state.userid, sid, repr(e))
        
            try:
                identity = json.loads(state.identity)
                verify(identity, "commander", bool)
                verify(identity, "squad_leader", bool)
                verify(identity, "squad", int)
                if identity["squad"] < 0 or identity["squad"] > 9:
                    raise ValueError("Invalid squad number")
                verify(identity, "team", basestring)
                if identity["team"] != "opfor" and identity["team"] != "blufor":
                    raise ValueError("Invalid team identified")
                #LEGACY: Ice 3.2 cannot handle unicode strings
                identity["team"] = str(identity["team"])
                try:
                    identity["hash"] = str(identity["hash"])
                    identity["pass"] = str(identity["pass"])
                except: 
                    identity["hash"] = ""
                    identity["pass"] = ""
                
                state.parsedidentity = identity
                
            except (KeyError, ValueError), e:
                log.debug("Invalid identity for %s (%d|%d) on server %d: %s", state.name, state.session, state.userid, sid, repr(e))

        # Update state and remember it
        self.update_state(server, self.sessions[sid][state.session], state)
        self.sessions[sid][state.session] = state
    
    #
    #--- Server callback functions
    #
    
    def userDisconnected(self, server, state, context = None):
        try:
            sid = server.id()
            del self.sessions[sid][state.session]
        except: pass
        try:
            server.kickUser(state.session, "User Disconnected")
        except: pass
         
    def userStateChanged(self, server, state, context = None):
        self.handle(server, state)
        
    def userConnected(self, server, state, context = None):
        self.handle(server, state)
    
    def channelCreated(self, server, state, context = None): pass
    def channelRemoved(self, server, state, context = None): pass
    def channelStateChanged(self, server, state, context = None): pass
    
    #
    #--- Meta callback functions
    #

    def started(self, server, context = None):
        self.sessions[server.id()] = {}
        
        if not cfg.murmur.servers or sid in cfg.murmur.servers:
            for index, user in server.getUsers().items():
                self.handle(server, user)
        
    def stopped(self, server, context = None):
        self.sessions[server.id()] = {}



    def verifyIdentity(self, hash, password):
        log = self.log()
        cfg = self.cfg()
        secret = cfg.prbf2.secret
        if secret == "":
            log.debug("identity verification disabled")
            return True

        minutesSinceEpoch = int(time.time() / 60.0)
        # Try previous minute and next minute
        for i in range (-1, 2):
            p = struct.unpack("<i",
                    hashfunc(
                    str(minutesSinceEpoch + i) + hash + secret
                ).digest()[0:4])[0] & 0x7FFFFF
            if str(p) == password:
                log.debug("%s verified identity" % hash)
                return True

        log.warning("Failed verifying identity for %s" % hash)
        return False