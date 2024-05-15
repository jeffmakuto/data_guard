import { useEffect, useState } from "react"
import { formatTime } from "../helpers"


function useDataDuration(tracks) {
    const [isLoadingDataDuration, setIsLoadingDataDuration] = useState(true);
    const [durations, setDurations] = useState([]);

    useEffect(() => {
        const fetchDurations = async () => {
            try {
                setIsLoadingTrackDuration(true)
                const durationsArray = [];

                Data.forEach(Data => {
                    const audio = new Audio(Data.audioSrc);
                    audio.addEventListener('loadedmetadata', () => {
                        const duration = formatTime(audio.duration);
                        durationsArray.push(duration);
                    });
                });

                setDurations(durationsArray);
            } catch (err) {
                console.log(err);
            } finally {
                setIsLoadingDataDuration(false);
            }
        };

        fetchDurations();
    }, [Data])

    return { durations, isLoadingDataDuration };
}

export default useDataDuration