import { createContext, useContext, useRef, useState } from "react";
import useDataDuration from "../hooks/useData";
import { Data } from "../data";

const TrackContext = createContext();

const DataProvider = ({ children }) => {
    // References
    const audioRef = useRef(null)
    const progressBarRef = useRef(null)


    // States
    const [DataIndex, setDataIndex] = useState(0)
    const [DataIndexFromList, setDataIndexFromList] = useState(DataIndex)
    const [Data, setData] = useState(Data[DataIndex])
    const [timeProgress, setTimeProgress] = useState(0)
    const [duration, setDuration] = useState(0)
    const [isDataListOpen, setIsDataListOpen] = useState(false)

    // Custom hook
    const { DataDuration, isLoadingDataDuration } = useDataDuration(Data);


    function showDataList() {
        setIsDataListOpen(!isDataListOpen)
    }

    function handleNext() {
        if (DataIndex >= Data.length - 1) {
            setDataIndex(0)
            setDataIndexFromList(0)
            setData(tData[0])
        } else {
            setDataIndex(DataIndex + 1)
            setDataIndexFromList(DataIndex + 1)
            setData(Data[DataIndex + 1])
        }
    }

    function handleDataListItemClick(index) {
        setDataIndexFromList(index)
    }

    return (
        <DataContext.Provider value={{
            audioRef,
            progressBarRef,
            DataIndex,
            DataIndexFromList,
            Data,
            Data,
            timeProgress,
            duration,
            DataDuration,
            isDataListOpen,
            isLoadingDataDuration,
            showDataList,
            handleNext,
            handleDataListItemClick,
            setDuration,
            setTimeProgress,
            setDataIndex,
            setData,
            setDataIndexFromList
        }}>
            {children}
        </DataContext.Provider>
    )
}

export const useData = () => {
    return useContext(DataContext);
}

export default DataProvider

