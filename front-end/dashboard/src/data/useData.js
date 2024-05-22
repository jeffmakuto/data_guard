import { useContext } from 'react';
import { DataContext } from './DataContext';

const useData = () => {
  const dataContext = useContext(DataContext);
  if (!dataContext) {
    throw new Error('useData must be used within a DataProvider');
  }
  return dataContext;
};

export default useData;
