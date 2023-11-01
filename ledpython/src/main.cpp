#include <Arduino.h>
#include <WiFiClient.h>
#include <ESP8266WiFi.h>
#include <ESP8266WiFiMulti.h>
#include <ESP8266HTTPClient.h>
#include <ArduinoJson.h>

const char* ssid = "";
const char* password = "";
const char* serverUrl = "";

DynamicJsonDocument ardjson(1024);
// put function declarations here:
int led = D1;

void setup() {
  Serial.begin(9600);
  Serial.println();
  Serial.println();
  Serial.print("Connecting to");
  Serial.println(ssid);
  WiFi.begin(ssid,password);
  while (WiFi.status() != WL_CONNECTED){
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi Connected");

 pinMode(led, OUTPUT);
}

void loop() {
  WiFiClient client;
  HTTPClient http;

  http.begin(client, serverUrl);
  int httpResponseCode = http.GET();
  String payload = http.getString();
  Serial.println(httpResponseCode);
  Serial.println(payload);

  deserializeJson(ardjson, payload);

  if (httpResponseCode == 200){
    bool isLEDon = ardjson[0];

    digitalWrite(led, isLEDon ? HIGH : LOW);
  } else {
    Serial.println("GET Request failed");
  }
  http.end();
  delay(3000);
}

// put function definitions here: