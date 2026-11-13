package En {
    enum def TrafficLightColor {
        enum red;
        enum yellow;
        enum green;
    }
    attribute currentColor : TrafficLightColor = TrafficLightColor::red;
}
