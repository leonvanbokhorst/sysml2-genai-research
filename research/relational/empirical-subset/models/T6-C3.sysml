package HeatPumpHeatingSystem {
    private import ScalarValues::*;

    attribute def Temperature;

    part def Thermostat {
        attribute indoorTemperature : Real;
        attribute targetTemperature : Real = 20.0;
    }

    part def BufferTank {
        attribute waterTemperature : Real;
        attribute volumeLitres : Real;
    }

    part def HeatPumpUnit {
        attribute isRunning : Boolean = false;
        attribute outputPowerKw : Real;
        port heatOut;
        port heatReturn;
    }

    part def UnderfloorCircuit {
        attribute supplyTemperature : Real;
        port supply;
        port return;
    }

    part def HeatingSystem {
        part heatPump : HeatPumpUnit;
        part tank : BufferTank;
        part circuit : UnderfloorCircuit;
        part thermostat : Thermostat;
    }

    part house : HeatingSystem;

    requirement def IndoorTemperatureRequirement {
        subject h : HeatingSystem;
        doc /* The heat pump shall maintain the indoor temperature at or above 20 degrees Celsius
               whenever the outside temperature is below 15 degrees Celsius. */
        attribute minimumIndoorTemperature : Real = 20.0;
        attribute outsideTemperatureThreshold : Real = 15.0;
    }

    requirement indoorTemperature : IndoorTemperatureRequirement;
    satisfy indoorTemperature by house;

    connection pumpToTank connect house.heatPump.heatOut to house.tank;
    connection tankToCircuit connect house.tank to house.circuit.supply;
    connection circuitToPump connect house.circuit.return to house.heatPump.heatReturn;
}
