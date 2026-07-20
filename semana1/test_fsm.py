from semana1.fsm_demo import TrafficLightFSM, TrafficLightState


def test_estado_inicial_del_sistema():
    fsm = TrafficLightFSM()

    assert fsm.state == TrafficLightState.RED


def test_transicion_de_rojo_a_verde():
    fsm = TrafficLightFSM()

    assert fsm.transition() == TrafficLightState.GREEN
    assert fsm.state == TrafficLightState.GREEN


def test_ciclo_completo_vuelve_a_rojo():
    fsm = TrafficLightFSM()

    fsm.transition()
    fsm.transition()
    assert fsm.transition() == TrafficLightState.RED
    assert fsm.state == TrafficLightState.RED


def test_conteo_de_ciclos():
    fsm = TrafficLightFSM()

    fsm.transition()
    fsm.transition()
    fsm.transition()

    assert fsm._cycle_count == 3
