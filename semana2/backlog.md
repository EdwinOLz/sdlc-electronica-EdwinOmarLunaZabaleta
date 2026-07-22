## US-01: Registrar lectura de sensor
Como operador de planta,    
quiero registrar la lectura de un sensor con su timestamp,  
para tener un historial consultable de las mediciones.  

Scenario: Registrar una lectura valida  
    Given un sensor con id "TEMP-01" registrado en el sistema   
    When envio una lectura de 24.3 C con timestamp actual   
    Then la lectura se guarda con estado "OK"   
    And puedo consultarla en el historial del sensor    

Scenario: Rechazar lectura de sensor inexistente    
    Given que no existe ningun sensor con id "GHOST-99"  
    When envio una lectura para "GHOST-99"  
    Then el sistema responde con error 404

    (complejidad 3-5 debido a que requiere una base de datos interactiva es decir que va a recibir datos en tiempo real asi como va a poder ser consultada en cualquier momento ya que no delimita su solo quiere consultarla al final del dia ese podria ser un detalle de ambiguedad)

## US-02: Alerta de problema
Como operador de planta,    
quiero recibir un mensaje de alerta si un sensor excede sus valores normales,  
para poder tener un mejor control de calidad en la planta corrigiendo problemas a tiempo.  

Scenario: enviar alerta    
    Given existe un threshold de 40 C en el sitema    
    When un sensor registrado excede el valor threshold     
    Then el sistema envia una alerta al operador   
    And puedo atender un posible problema en la planta   

Scenario: no se puede enviar alerta     
    Given no existe un valor de threshold en el sistema   
    When un sensor envie un valor el cual no puede ser comparado    
    Then el sistema responde con "error no existe limite configurado

    (complejidad 3 creo que este problema no es tan complejo ya que trata solo del envio de mensajes de alerta, el problema aqui consta con que no me queda del todo claro que tantos escenarios se pueden construir ya que estos deribaran en pytest para cada modulo creado por nuestro user storie pero veo que el hecho de mandar un mensaje de alerta puede tener varios ploblemas como que no existe un limite configurado, en el ejemplo no estoy asignando aun por que medio se enviara el mensaje, pero que pasa tambien si existe un limite pero el sensor (como en el ejemplo dado en el curso) no existe o no esta correctamente verificado, creo que esto es algo de lo que deberia encargarse otro modulo para cumplir con el principio de responsabilidad unica pero aun asi son error que me llegan a pasar por la cabeza quizas por la forma en la que estoy acostumbrado a programar que si es un poco caotica)