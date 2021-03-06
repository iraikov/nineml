"""
docstring needed

:copyright: Copyright 2010-2013 by the Python lib9ML team, see AUTHORS.
:license: BSD-3, see LICENSE for details.
"""
from itertools import chain
from nineml.exceptions import NineMLRuntimeError
from collections import defaultdict
from nineml.abstraction_layer.dynamics.validators.base import ComponentValidatorPerNamespace  # @IgnorePep8


class ComponentValidatorEventPorts(ComponentValidatorPerNamespace):

    """
    Check that each OutputEvent and OnEvent has a corresponding EventPort
    defined, and that the EventPort has the right direction.
    """

    def __init__(self, component):
        ComponentValidatorPerNamespace.__init__(self,
                                     explicitly_require_action_overrides=False)

        # Mapping component to list of events/eventports at that component
        self.event_send_ports = defaultdict(dict)
        self.event_receive_ports = defaultdict(dict)
        self.output_events = defaultdict(list)
        self.input_events = defaultdict(list)

        self.visit(component)

        # Check that each output event has a corresponding event_port with a
        # send mode:
        for ns, output_events in self.output_events.iteritems():
            for output_event in output_events:
                assert output_event in self.event_send_ports[ns], \
                          ("Can't find port definition matching OP-Event: %s" %
                           output_event)

        # Check that each input event has a corresponding event_port with a
        # recv/reduce mode:
        for ns, input_events in self.input_events.iteritems():
            for input_event in input_events:
                assert input_event in self.event_receive_ports[ns]

        # Check that each Event port emits/recieves at least one
        for ns, event_ports in chain(self.event_send_ports.iteritems(),
                                     self.event_receive_ports.iteritems()):
            for evt_port_name in event_ports.keys():

                op_evts_on_port = [ev for ev in self.output_events[ns]
                                   if ev == evt_port_name]
                ip_evts_on_port = [ev for ev in self.input_events[ns]
                                   if ev == evt_port_name]

                if len(op_evts_on_port) + len(ip_evts_on_port) == 0:
                    print ('Unable to find events generated for: ', ns,
                           evt_port_name)

    def action_eventsendport(self, port, namespace, **kwargs):  # @UnusedVariable
        assert not port.name in self.event_send_ports[namespace]
        self.event_send_ports[namespace][port.name] = port

    def action_eventreceiveport(self, port, namespace, **kwargs):  # @UnusedVariable
        assert not port.name in self.event_receive_ports[namespace]
        self.event_receive_ports[namespace][port.name] = port

    def action_outputevent(self, output_event, namespace, **kwargs):  # @UnusedVariable @IgnorePep8
        self.output_events[namespace].append(output_event.port_name)

    def action_onevent(self, on_event, namespace, **kwargs):  # @UnusedVariable
        self.input_events[namespace].append(on_event.src_port_name)


# Check that the sub-components stored are all of the
# right types:
class ComponentValidatorOutputAnalogPorts(ComponentValidatorPerNamespace):

    """
    Check that all output AnalogPorts reference a local symbol, either an alias
    or a state variable
    """

    def __init__(self, component):
        ComponentValidatorPerNamespace.__init__(self,
                                     explicitly_require_action_overrides=False)

        self.output_analogports = defaultdict(list)
        self.available_symbols = defaultdict(list)

        self.visit(component)

        for namespace, analogports in self.output_analogports.iteritems():
            for ap in analogports:
                if not ap in self.available_symbols[namespace]:
                    raise NineMLRuntimeError(
                        'Unable to find an Alias or State variable for '
                        'analog-port: %s' % ap)

    def add_symbol(self, namespace, symbol):
        assert not symbol in self.available_symbols[namespace]
        self.available_symbols[namespace].append(symbol)

    def action_analogsendport(self, port, namespace, **kwargs):  # @UnusedVariable @IgnorePep8
        self.output_analogports[namespace].append(port.name)

    def action_statevariable(self, state_variable, namespace, **kwargs):  # @UnusedVariable @IgnorePep8
        self.add_symbol(namespace=namespace, symbol=state_variable.name)

    def action_alias(self, alias, namespace, **kwargs):  # @UnusedVariable
        self.add_symbol(namespace=namespace, symbol=alias.lhs)
