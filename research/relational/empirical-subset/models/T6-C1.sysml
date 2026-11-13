package HeatPumpHeating {
    private import ScalarValues::*;

    attribute def Temperature;

    part def Thermostat {
        attribute indoorTemperature : Real;
        attribute setpoint : Real = 20.0;
    }

    part def BufferTank {
        attribute volumeLitres : Real;
        attribute waterTemperature : Real;
    }

    part def HeatPump {
        attribute isRunning : Boolean = false;
        attribute thermalOutputKw : Real;
        port flowOut;
        port flowReturn;
    }

    part def HeatingCircuit {
        attribute flowTemperature : Real;
        port supply;
        port return;
    }

    part def HeatingSystem {
        part pump : HeatPump;
        part tank : BufferTank;
        part circuit : HeatingCircuit;
        part thermostat : Thermostat;
    }

    part dwelling : HeatingSystem;

    requirement def IndoorTemperatureMinimum {
        doc /* The heat pump shall maintain the indoor temperature at or above 20 degrees Celsius
               whenever the outside temperature is below 15 degrees Celsius. */
        attribute minimumIndoor : Real = 20.0;
        attribute outsideThreshold : Real = 15.0;
    }

    requirement indoorMinimum : IndoorTemperatureMinimum;
    satisfy indoorMinimum by dwelling;

    flow of Temperature from dwelling.pump.flowOut to dwelling.tank;
    flow of Temperature from dwelling.tank to dwelling.circuit.supply;
    flow of Temperature from dwelling.circuit.return to dwelling.pump.flowReturn;
}
