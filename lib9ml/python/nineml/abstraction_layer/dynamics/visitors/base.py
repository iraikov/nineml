"""
docstring needed

:copyright: Copyright 2010-2013 by the Python lib9ML team, see AUTHORS.
:license: BSD-3, see LICENSE for details.
"""


from itertools import chain


class ComponentVisitor(object):

    def visit(self, obj, **kwargs):
        return obj.accept_visitor(self, **kwargs)


class ActionVisitor(ComponentVisitor):

    def __init__(self, explicitly_require_action_overrides=True):
        self.explicitly_require_action_overrides = explicitly_require_action_overrides  # @IgnorePep8

    def visit_componentclass(self, component, **kwargs):
        self.action_componentclass(component, **kwargs)

        nodes = chain(component.parameters, component.ports)
        for p in nodes:
            p.accept_visitor(self, **kwargs)

        if component.dynamics:
            component.dynamics.accept_visitor(self, **kwargs)

        for subnode in component.subnodes.values():
            subnode.accept_visitor(self, **kwargs)

    def visit_dynamics(self, dynamics, **kwargs):
        self.action_dynamics(dynamics, **kwargs)
        nodes = chain(dynamics.regimes, dynamics.aliases,
                      dynamics.state_variables)
        for p in nodes:
            p.accept_visitor(self, **kwargs)

    def visit_regime(self, regime, **kwargs):
        self.action_regime(regime, **kwargs)
        nodes = chain(regime.time_derivatives, regime.on_events,
                      regime.on_conditions)
        for p in nodes:
            p.accept_visitor(self, **kwargs)

    def visit_statevariable(self, state_variable, **kwargs):
        self.action_statevariable(state_variable, **kwargs)

    def visit_parameter(self, parameter, **kwargs):
        self.action_parameter(parameter, **kwargs)

    def visit_analogsendport(self, port, **kwargs):
        self.action_analogsendport(port, **kwargs)

    def visit_analogreceiveport(self, port, **kwargs):
        self.action_analogreceiveport(port, **kwargs)

    def visit_analogreduceport(self, port, **kwargs):
        self.action_analogreduceport(port, **kwargs)

    def visit_eventsendport(self, port, **kwargs):
        self.action_eventsendport(port, **kwargs)

    def visit_eventreceiveport(self, port, **kwargs):
        self.action_eventreceiveport(port, **kwargs)

    def visit_outputevent(self, output_event, **kwargs):
        self.action_outputevent(output_event, **kwargs)

    def visit_inputevent(self, input_event, **kwargs):
        assert False, 'We should remove this'
        self.action_inputevent(input_event, **kwargs)

    def visit_assignment(self, assignment, **kwargs):
        self.action_assignment(assignment, **kwargs)

    def visit_alias(self, alias, **kwargs):
        self.action_alias(alias, **kwargs)

    def visit_timederivative(self, time_derivative, **kwargs):
        self.action_timederivative(time_derivative, **kwargs)

    def visit_condition(self, condition, **kwargs):
        self.action_condition(condition, **kwargs)

    def visit_oncondition(self, on_condition, **kwargs):
        self.action_oncondition(on_condition, **kwargs)
        nodes = chain([on_condition.trigger],
                      on_condition.event_outputs,
                      on_condition.state_assignments)
        for p in nodes:
            p.accept_visitor(self, **kwargs)

    def visit_onevent(self, on_event, **kwargs):
        self.action_onevent(on_event, **kwargs)
        nodes = chain(on_event.event_outputs, on_event.state_assignments)
        nodes = list(nodes)
        # print nodes
        for p in nodes:
            p.accept_visitor(self, **kwargs)

    def check_pass(self):
        if self.explicitly_require_action_overrides:
            assert False, "There is some over-riding missing"
        else:
            pass

    # To be overridden:
    def action_componentclass(self, component, **kwargs):  # @UnusedVariable
        self.check_pass()

    def action_dynamics(self, dynamics, **kwargs):  # @UnusedVariable
        self.check_pass()

    def action_regime(self, regime, **kwargs):  # @UnusedVariable
        self.check_pass()

    def action_statevariable(self, state_variable, **kwargs):  # @UnusedVariable @IgnorePep8
        self.check_pass()

    def action_parameter(self, parameter, **kwargs):  # @UnusedVariable
        self.check_pass()

    def action_analogsendport(self, port, **kwargs):  # @UnusedVariable
        self.check_pass()

    def action_analogreceiveport(self, port, **kwargs):  # @UnusedVariable
        self.check_pass()

    def action_analogreduceport(self, port, **kwargs):  # @UnusedVariable
        self.check_pass()

    def action_eventsendport(self, port, **kwargs):  # @UnusedVariable
        self.check_pass()

    def action_eventreceiveport(self, port, **kwargs):  # @UnusedVariable
        self.check_pass()

    def action_outputevent(self, output_event, **kwargs):  # @UnusedVariable
        self.check_pass()

    def action_assignment(self, assignment, **kwargs):  # @UnusedVariable
        self.check_pass()

    def action_alias(self, alias, **kwargs):  # @UnusedVariable
        self.check_pass()

    def action_timederivative(self, time_derivative, **kwargs):  # @UnusedVariable @IgnorePep8
        self.check_pass()

    def action_condition(self, condition, **kwargs):  # @UnusedVariable
        self.check_pass()

    def action_oncondition(self, on_condition, **kwargs):  # @UnusedVariable
        self.check_pass()

    def action_onevent(self, on_event, **kwargs):  # @UnusedVariable
        self.check_pass()
