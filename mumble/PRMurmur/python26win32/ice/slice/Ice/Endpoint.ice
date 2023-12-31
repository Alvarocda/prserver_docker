// **********************************************************************
//
// Copyright (c) 2003-2010 ZeroC, Inc. All rights reserved.
//
// This copy of Ice is licensed to you under the terms described in the
// ICE_LICENSE file included in this distribution.
//
// **********************************************************************

#ifndef ICE_ENDPOINT_ICE
#define ICE_ENDPOINT_ICE

#include <Ice/BuiltinSequences.ice>
#include <Ice/EndpointF.ice>

[["cpp:header-ext:h"]]

module Ice
{

const short TCPEndpointType = 1;
const short UDPEndpointType = 3;

/**
 *
 * Base class providing access to the endpoint details.
 *
 **/
local class EndpointInfo
{
    /**
     *
     * The timeout for the endpoint in milliseconds. 0 means
     * non-blocking, -1 means no timeout.
     *
     **/
    int timeout;

    /**
     *
     * Specifies whether or not compression should be used if
     * available when using this endpoint.
     *
     */
    bool compress;

    /**
     *
     * Returns the type of the endpoint.
     *
     **/
    ["cpp:const"] short type();

    /**
     *
     * Returns true if this endpoint is a datagram endpoint.
     *
     **/
    ["cpp:const"] bool datagram();

    /**
     *
     * Returns true if this endpoint is a secure endpoint.
     *
     **/
    ["cpp:const"] bool secure();
};

/**
 *
 * The user-level interface to an endpoint.
 *
 **/
local interface Endpoint
{
    /**
     *
     * Return a string representation of the endpoint.
     *
     * @return The string representation of the endpoint.
     *
     **/
    ["cpp:const"] string toString();

    /**
     *
     * Returns the endpoint information.
     *
     * @return The endpoint information class.
     *
     **/
    ["cpp:const"] EndpointInfo getInfo();
};

/**
 *
 * Provides access to the address details of a IP endpoint.
 *
 * @see Endpoint
 *
 **/
local class IPEndpointInfo extends EndpointInfo
{
    /**
     * 
     * The host or address configured with the endpoint.
     *
     **/
    string host;

    /**
     * 
     * The port number.
     * 
     **/
    int port;
};

/**
 *
 * Provides access to a TCP endpoint information.
 *
 * @see Endpoint
 *
 **/
local class TCPEndpointInfo extends IPEndpointInfo
{
};

/**
 *
 * Provides access to an UDP endpoint information.
 *
 * @see Endpoint
 *
 **/
local class UDPEndpointInfo extends IPEndpointInfo
{
     /**
      *
      * The protocol version supported by the endpoint.
      *
      **/
     byte protocolMajor;
     byte protocolMinor;

     /**
      *
      * The encoding version supported by the endpoint.
      *
      **/
     byte encodingMajor;
     byte encodingMinor;

    /**
     * 
     * The multicast interface.
     *
     **/
     string mcastInterface;

    /**
     *
     * The multicast time-to-live (or hops).
     *
     **/
     int mcastTtl;
};

/**
 *
 * Provides access to the details of an opaque endpoint.
 *
 * @see Endpoint
 *
 **/
local class OpaqueEndpointInfo extends EndpointInfo
{
    /**
     *
     * The raw encoding of the opaque endpoint.
     *
     **/
    Ice::ByteSeq rawBytes;
};

};

#endif
