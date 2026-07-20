from semana1.uart_driver.parsers import ModbusParser, NMEAParser

def test_modbus_parser_reconoce_frame_valido():
    """Verifica que ModbusParser devuelva True en can_parse para un frame de bytes de tamaño 4 o mayor."""
    parser = ModbusParser()
    assert parser.can_parse(b'\x01\x03\x00\x00')


def test_modbus_parser_rechaza_frame_invalido():
    """Verifica que ModbusParser devuelva False en can_parse para un frame de menos de 4 bytes."""
    parser = ModbusParser()
    assert not parser.can_parse(b'\x01\x03\x00')


def test_nmea_parser_reconoce_sentencia_gpgga():
    """Verifica que NMEAParser devuelva True en can_parse para una trama de bytes que inicie con b'$GPGGA'."""
    parser = NMEAParser()
    assert parser.can_parse(b'$GPGGA,datos')


def test_nmea_parser_parsea_correctamente():
    """Verifica que al llamar a parse() en NMEAParser con b'$GPGGA,datos', devuelva un diccionario con la clave 'protocol' igual a 'NMEA' y la sentencia decodificada."""
    parser = NMEAParser()
    result = parser.parse(b'$GPGGA,datos')
    assert result['protocol'] == 'NMEA'
    assert result['sentence'] == '$GPGGA,datos'

def test_modbus_parser_parsea_correctamente():
    """Verifica que al llamar a parse() en ModbusParser con b'\\x01\\x03\\x00\\x00' devuelva el protocolo Modbus RTU y la data en hex."""
    parser = ModbusParser()
    result = parser.parse(b'\x01\x03\x00\x00')
    assert result['protocol'] == 'Modbus RTU'
    assert result['data'] == '01030000'