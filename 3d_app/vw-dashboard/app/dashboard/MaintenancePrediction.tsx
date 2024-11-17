import React, { useState } from 'react';
import { Button, InputWrapper, Input, Slider, Text } from '@mantine/core';

const MaintenancePrediction = () => {
  const [mileage, setMileage] = useState(20000);
  const [engineHours, setEngineHours] = useState(1000);
  const [componentHealthScore, setComponentHealthScore] = useState(80);
  const [temperature, setTemperature] = useState(80);
  const [vibrationLevel, setVibrationLevel] = useState(0.05);
  const [prediction, setPrediction] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);

  const handlePredict = async () => {
    setLoading(true);
    try {
      const response = await fetch('/api/predict', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          mileage,
          engineHours,
          componentHealthScore,
          temperature,
          vibrationLevel,
        }),
      });

      const result = await response.json();
      setPrediction(result.prediction ? "Component Likely to Fail" : "Component Unlikely to Fail");
    } catch (error) {
      console.error("Error predicting failure:", error);
      setPrediction("Error in prediction");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="space-y-4">
      <InputWrapper label="Mileage">
        <Input value={mileage} onChange={(e) => setMileage(Number(e.target.value))} />
      </InputWrapper>

      <InputWrapper label="Engine Hours">
        <Input value={engineHours} onChange={(e) => setEngineHours(Number(e.target.value))} />
      </InputWrapper>

      <InputWrapper label="Component Health Score">
        <Slider value={componentHealthScore} onChange={setComponentHealthScore} min={0} max={100} />
      </InputWrapper>

      <InputWrapper label="Temperature">
        <Input value={temperature} onChange={(e) => setTemperature(Number(e.target.value))} />
      </InputWrapper>

      <InputWrapper label="Vibration Level">
        <Input value={vibrationLevel} onChange={(e) => setVibrationLevel(Number(e.target.value))} />
      </InputWrapper>

      <Button onClick={handlePredict} loading={loading}>Predict Failure</Button>
      {prediction && <Text>{prediction}</Text>}
    </div>
  );
};

export default MaintenancePrediction;
