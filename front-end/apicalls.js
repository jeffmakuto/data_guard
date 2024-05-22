import React, { useState, useEffect } from 'react';

const DataguardApp = () => {
  const [data, setData] = useState(null);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    
    const fetchData = async () => {
      try {
        // Make an API call using fetch or Axios
        const response = await fetch('https://api.dataguard.com/data');
        if (!response.ok) {
          throw new Error('Failed to fetch data');
        }
        const responseData = await response.json();
        setData(responseData);
        setIsLoading(false);
      } catch (error) {
        setError(error.message);
        setIsLoading(false);
      }
    };

    fetchData(); 
  }, []); // Empty dependency array ensures that the effect runs only once on mount

  if (isLoading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>Error: {error}</div>;
  }

  return (
    <div>
      <h1>Data from Dataguard API</h1>
      {data && (
        <div>
          {/* Display data from the API */}
          <pre>{JSON.stringify(data, null, 2)}</pre>
        </div>
      )}
    </div>
  );
};

export default DataguardApp;
