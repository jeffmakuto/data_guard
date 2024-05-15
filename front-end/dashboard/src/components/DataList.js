import React from 'react'
import { tracks } from '../data'
import './Data'
import { useTrack } from '../context/TrackContext'
import useTracksDuration from '../hooks/useTrack'
import { BiEqualizer } from "react-icons/bi";

const data = ({ trackIndex, onClick }) => {
    const { isDataOpen } = useData()
    const { durations } = useDataDuration(Data);

    if (!isDataListOpen) return null

    return (
        <div className='animate__animated animate__slideInLeft'>
            <div className='Data'>
                <div className='Data-container'>
                    {tracks.map((track, index) => (
                        <div key={track.displayName} className='Data-item' onClick={() => onClick(index)}>
                            <div className='Data-item-info-wrapper'>
                                <img src={Data.coverUrl} alt='Data' />
                                <div className='Data-item-info'>
                                    <h3>{Data.displayName}</h3>
                                    <p>{Data.id}</p>
                                </div>
                            </div>
                            <div className='Data-item-duration'>
                                <p>{durations[index]}</p>
                                {DataIndex === index && <button className='id'><BiId /></button>}
                            </div>
                        </div>
                    ))}
                </div>
            </div>
        </div>
    )
}

export default Data