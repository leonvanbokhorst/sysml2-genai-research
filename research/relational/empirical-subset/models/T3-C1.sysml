package InfusionPumpSystem {

    part def FluidLine {
        attribute innerDiameter : Real;
        attribute isOccluded : Boolean = false;
    }

    part def PressureSensor {
        attribute measuredPressure : Real;
        attribute occlusionThreshold : Real;
    }

    part def Alarm {
        attribute isAudible : Boolean = false;
        attribute isVisible : Boolean = false;
    }

    part def InfusionPump {
        attribute flowRate : Real;
        attribute isDelivering : Boolean = false;
        part line : FluidLine;
        part sensor : PressureSensor;
        part alarm : Alarm;
        port outlet;
    }

    part pump : InfusionPump;

    requirement def AlarmWithinTwoSeconds {
        doc /* The pump shall raise an audible and visible alarm within 2 seconds of an occlusion
               being detected, and shall stop delivery at the same time. */
        attribute maxDelaySeconds : Real = 2.0;
    }

    requirement occlusionAlarm : AlarmWithinTwoSeconds;

    satisfy occlusionAlarm by pump;

    connection sensorToPump connect pump.sensor.measuredPressure to pump.flowRate;
}
