#define THERMISTOR_1_PIN A0
#define THERMISTOR_2_PIN A1
#define THERMISTOR_3_PIN A2
#define THERMISTOR_4_PIN A3
#define THERMISTOR_5_PIN A4

// define number of sample to average
#define NUMSAMPLES 8
// The beta coefficient of the thermistor (usually 3000-4000)
#define BCOEFFICIENT 3950
// the value of the 'other' resistor
#define SERIESRESISTOR 10000
// resistance at 25 degrees C
#define THERMISTORNOMINAL 2252
// temp. for nominal resistance (almost always 25 C)
#define TEMPERATURENOMINAL 25


int led = 7;
int usb = 6;

int therm1;
int therm2;
int therm3;
int therm4;
int therm5;

int therm1Pin=A0;
int therm2Pin=A1;
int therm3Pin=A2;
int therm4Pin=A3;
int therm5Pin=A4;

char trigger=' ';

void setup(){
   Serial.begin(9600);
   pinMode(led,OUTPUT);
   pinMode(usb,OUTPUT);
   analogReference(EXTERNAL);
}

void loop(){
  // While data is sent over serial assign it to the trigger
  while(Serial.available()>0){
    trigger=Serial.read();
  }

  //
  if (trigger=='y'){
    // turn LED ON
    digitalWrite(led, HIGH);
    delay(100);
    trigger=' ';
  }

  else if(trigger=='n'){
    digitalWrite(led,LOW);
    delay(100);
    trigger=' ';
  }

  else if(trigger=='u'){
    digitalWrite(usb,HIGH);
    Serial.println("usb on");
    delay(100);
    trigger=' ';
  }

  else if(trigger=='d'){
    digitalWrite(usb,LOW);
    Serial.println("usb off");
    delay(100);
    trigger=' ';
  }

  else if(trigger=='t'){
  // Reading thermistors
  //*********************************
  //therm1
   therm1=int(100*thermRead(NUMSAMPLES,THERMISTOR_1_PIN));
   therm2=int(100*thermRead(NUMSAMPLES,THERMISTOR_2_PIN));
   therm3=int(100*thermRead(NUMSAMPLES,THERMISTOR_3_PIN));
   therm4=int(100*thermRead(NUMSAMPLES,THERMISTOR_4_PIN));
   therm5=int(100*thermRead(NUMSAMPLES,THERMISTOR_5_PIN));

//   String therm=String(therm1);
   Serial.println(therm1);
   Serial.println(therm2);
   Serial.println(therm3);
   Serial.println(therm4);
   Serial.println(therm5);
   trigger=' ';
   }
}

float thermRead(int numsamples,int pin)
{  float ret_val = 0;
   int samples[numsamples];
   float R=0;
   float T=0;

   // thermistor parameters
   float A = 0.001473264;
   float B = 0.000237209;
   float C = 0.000000107;

   // Averaging over 8 measurements
   uint8_t i;
     // measurement
     for (i=0; i< numsamples; i++) {
       samples[i] = analogRead(pin);
       delay(10);
     }
     // averaging
    for (i=0; i< numsamples; i++) {
      ret_val += samples[i];
    }
    ret_val /= numsamples;

   // convert the value to resistance
     // arduino ADC transform
     R = SERIESRESISTOR / (1023/ret_val-1);
     // Steinhart-Hart equation
     T=A+B*log(R)+C*pow(log(R),3);
     T = 1/T-273.15;
     return(T);
}
