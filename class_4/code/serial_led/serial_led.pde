
void setup()
{
  // Setup the serial port to listen/write at 9600 baud
  Serial.begin(9600);
  // set pins 9 thru 11 to OUTPUT mode
  for( int pin = 9; pin <= 11; pin++ )
  {
    pinMode(pin, OUTPUT);
  }
}

void loop()
{
  // check if there is data in serial to read
  if(Serial.available() > 0)
  {
    // read the serial port
    int input_byte = Serial.read();
    // if we received 'a', turn leds on, if it's 'b', off
    switch(input_byte)
    {
      case 'a':
        turn_leds(HIGH);
        break;
      case 'b':
        turn_leds(LOW);
        break;
      default:
        break;
    }
  }
}

void turn_leds(int value)
{
  // loop pins 9 thru 11 and set those pins to the 
  // value passed to the function, LOW or HIGH (0 or 1)
  for(int pin = 9; pin <= 11; pin++ )
  {
    digitalWrite(pin, value);
  }
}
